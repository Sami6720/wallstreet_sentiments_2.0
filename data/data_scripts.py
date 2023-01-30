import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import warnings
import time
import praw
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from datetime import date


def stringify_col(x):
    if np.isnan(x):
        return 'NEW'
    else:
        return str(x)

def get_data(df2, reddit, stocks, time):
    
    # Includes common words and words used on wsb that are also stock names
    blacklist = {'I', 'ELON', 'WSB', 'THE', 'A', 'ROPE', 'YOLO', 'TOS', 'CEO', 'DD', 'IT', 'OPEN', 'ATH', 'PM', 'IRS', 'FOR','DEC', 'BE', 'IMO', 'ALL', 'RH', 'EV', 'TOS', 'CFO', 'CTO', 'DD', 'BTFD', 'WSB', 'OK', 'PDT', 'RH', 'KYS', 'FD', 'TYS', 'US', 'USA', 'IT', 'ATH', 'RIP', 'BMW', 'GDP', 'OTM', 'ATM', 'ITM', 'IMO', 'LOL', 'AM', 'BE', 'PR', 'PRAY', 'PT', 'FBI', 'SEC', 'GOD', 'NOT', 'POS', 'FOMO', 'TL;DR', 'EDIT', 'STILL', 'WTF', 'RAW', 'PM', 'LMAO', 'LMFAO', 'ROFL', 'EZ', 'RED', 'BEZOS', 'TICK', 'IS', 'PM', 'LPT', 'GOAT', 'FL', 'CA', 'IL', 'MACD', 'HQ', 'OP', 'PS', 'AH', 'TL', 'JAN', 'FEB', 'JUL', 'AUG', 'SEP', 'SEPT', 'OCT', 'NOV', 'FDA', 'IV', 'ER', 'IPO', 'MILF', 'BUT', 'SSN', 'FIFA', 'USD', 'CPU', 'AT', 'GG', 'Mar'}

    # Adding wsb/reddit flavor to vader to improve sentiment analysis, score: 4.0 to -4.0
    new_words = {
        'citron': -4.0,  
        'hidenburg': -4.0,        
        'moon': 4.0,
        'highs': 2.0,
        'mooning': 4.0,
        'long': 2.0,
        'short': -2.0,
        'call': 4.0,
        'calls': 4.0,    
        'put': -4.0,
        'puts': -4.0,    
        'break': 2.0,
        'tendie': 2.0,
         'tendies': 2.0,
         'town': 2.0,     
         'overvalued': -3.0,
         'undervalued': 3.0,
         'buy': 4.0,
         'sell': -4.0,
         'gone': -1.0,
         'gtfo': -1.7,
         'paper': -1.7,
         'bullish': 3.7,
         'bearish': -3.7,
         'bagholder': -1.7,
         'stonk': 1.9,
         'green': 1.9,
         'money': 1.2,
         'print': 2.2,
         'rocket': 2.2,
         'bull': 2.9,
         'bear': -2.9,
         'pumping': -1.0,
         'sus': -3.0,
         'offering': -2.3,
         'rip': -4.0,
         'downgrade': -3.0,
         'upgrade': 3.0,     
         'maintain': 1.0,          
         'pump': 1.9,
         'hot': 1.5,
         'drop': -2.5,
         'rebound': 1.5,  
         'crack': 2.5,
    }
    
    start_time = time.time()
    # Set program parameters
    subs = ['wallstreetbets', 'stocks', 'investing', 'stockmarket']     # sub-reddit to search
    post_flairs = {'Daily Discussion', 'Weekend Discussion', 'Discussion'}    # posts flairs to search || None flair is automatically considered
    goodAuth = {'AutoModerator'}   # authors whom comments are allowed more than once
    uniqueCmt = True                # allow one comment per author per symbol
    ignoreAuthP = {'example'}       # authors to ignore for posts 
    ignoreAuthC = {'example'}       # authors to ignore for comment 
    upvoteRatio = 0.95         # upvote ratio for post to be considered, 0.70 = 70% TASK: Revert back to 70%
    ups = 20       # define # of upvotes, post is considered if upvotes exceed this
    limit = 10      # define the limit, comments 'replace more' limit TASK: 
    upvotes = 2     # define # of upvotes, comment is considered if upvotes exceed this 
    picks = 10     # define # of picks here, prints as "Top ## picks are:"
    picks_ayz = 10   # define # of picks for sentiment analysis

    posts, count, c_analyzed, tickers, titles, a_comments = 0, 0, 0, {}, [], {}
    cmt_auth = {}

    for sub in subs:
        subreddit = reddit.subreddit(sub)
        hot_python = subreddit.hot() # sorting posts by hot
        # Extracting comments, symbols from subreddit
        for submission in hot_python:
            flair = submission.link_flair_text
            author = submission.author.name

            # Checking: post upvote ratio # of upvotes, post flair, and author
            if submission.upvote_ratio >= upvoteRatio and submission.ups > ups and (flair in post_flairs or flair is None) and author not in ignoreAuthP:
                submission.comment_sort = 'new'
                comments = submission.comments
                titles.append(submission.title)
                posts += 1
                submission.comments.replace_more(limit = limit)
                for comment in comments:
                    # try except for deleted account? # TASK: What is this peice of code accomplishing?
                    try:
                        auth = comment.author.name
                    except:
                        pass
                    c_analyzed += 1

                    # checking: comment upvotes and author
                    if comment.score > upvotes and auth not in ignoreAuthC:
                        split = comment.body.split(' ')
                        for word in split:
                            word = word.replace("$", "")
                            # upper = ticker, length of ticker <= 5, excluded words
                            if word.isupper() and len(word) <= 5 and word not in blacklist and word in stocks:

                                # unique comments, try/except for key errors
                                if uniqueCmt and auth not in goodAuth:
                                    try:
                                        if auth in cmt_auth[word]:
                                            break
                                    except:
                                        pass

                                # counting tickers
                                if word in tickers:
                                    tickers[word] += 1
                                    a_comments[word].append(comment.body)
                                    cmt_auth[word].append(auth)
                                    count += 1
                                else:
                                    tickers[word] = 1
                                    cmt_auth[word] = [auth]
                                    a_comments[word] = [comment.body]
                                    count += 1

    # sorts the dictionary
    symbols = dict(sorted(tickers.items(), key=lambda item: item[1], reverse = True))
    top_picks = list(symbols.keys())[0:picks]
    time = (time.time() - start_time)

    # print top picks
    print("It took {t:.2f} seconds to analyze {c} comments in {p} posts in {s} subreddits.\n".format(t=time,
                                                                                                    c=c_analyzed,
                                                                                                    p=posts,
                                                                                                    s=len(subs)))
    # Applying sentiment analysis
    scores, s = {}, {}

    vader = SentimentIntensityAnalyzer()
    
    # adding custom words from data.py
    vader.lexicon.update(new_words)
    
    picks_sentiment = list(symbols.keys())[0: picks_ayz]
    for symbol in picks_sentiment:
        stock_comments = a_comments[symbol]
        for cmnt in stock_comments:
            score = vader.polarity_scores(cmnt)
            if symbol in s:
                s[symbol][cmnt] = score
            else:
                s[symbol] = {cmnt: score}
            if symbol in scores:
                for key, _ in score.items():
                    scores[symbol][key] += score[key]
            else:
                scores[symbol] = score

        # calculating averages
        for key in score:
            scores[symbol][key] = scores[symbol][key] / symbols[symbol]
            scores[symbol][key] = "{pol:.3f}".format(pol=scores[symbol][key])

    # Printing sentiment analysis
    print(f"\nSentiment analysis of top {picks_ayz} picks:")
    df = pd.DataFrame(scores)
    df=df.T
    df['stocks']=df.index
    df=df.reset_index().drop(['index'], axis=1)
    df=df[['stocks','neg', 'neu', 'pos', 'compound']]
    df.columns = ['stocks','bearish', 'neutral', 'bullish', 'total_compound'] 
    df_merged=df.merge(df2, on='stocks', how='left') # Left join
    df_merged[['total_compound_x', "total_compound_y"]] = df_merged[["total_compound_x", "total_compound_y"]].apply(pd.to_numeric) # Convert total_compound_x and total_compound_y to numeric
    df_merged['change']=100*(df_merged['total_compound_x']-df_merged['total_compound_y'])/(df_merged['total_compound_y'])
    df_merged=df_merged.sort_values(
        by="total_compound_x",
        ascending=False
    ).reset_index().drop(['index'], axis=1) # percentage change column added
    print(df)
    df_merged=df_merged[['stocks', 'total_compound_x', 'change']]
    df_merged.columns=['stocks', 'total_compound', 'change']
    df_merged['change']=df_merged['change'].apply(lambda x: 0 if x==0 else x) # prevent -0.0 in change
    df_merged['change']=df_merged['change'].apply(lambda x: round(x, 2)) # round change to 2 dp
    df_merged['change']=df_merged['change'].apply(stringify_col) # stringify change
    df_merged['total_compound']=df_merged['total_compound'].apply(lambda x: round(x, 2)) # round total_compound to 2 dp
    df_merged['total_compound']=df_merged['total_compound'].apply(stringify_col) # stringify total_compound
    df_merged['id']=df_merged.index # add id column

    return df_merged.to_json(orient='records')