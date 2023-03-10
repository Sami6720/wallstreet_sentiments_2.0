from flask import Flask, jsonify, request
from flask_cors import CORS

# For get_data function
from data_scripts import get_data, stringify_col
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

app = Flask(__name__)
CORS(app)

'''includes US stock symbols with market cap > 100 Million, and price above $3. 
Download the csv file:
https://www.nasdaq.com/market-activity/stocks/screener?exchange=nasdaq&letter=0&render=download 
for all of the NYSE, NASDAQ and NYSEAMERICAN public traded companies.
'''

stocks = pd.read_csv('tickers.csv')

# Last Sale column is an object, let's convert to float
stocks['Last Sale'] = stocks['Last Sale'].str.replace('$', '')
stocks['Last Sale'] = pd.to_numeric(stocks['Last Sale'], downcast='float')
type(stocks['Last Sale'][0])

# Filter out stocks >$3 and > $100 million cap
price_filter = stocks['Last Sale'] >= 3.00
cap_filter = stocks['Market Cap'] >= 100000000

# make set of symbols
stocks = set(stocks[(price_filter) & (cap_filter)]['Symbol'])

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
     'crack': 2.5,}

# Instantiate praw object
reddit = praw.Reddit(
    user_agent = "Comment Extraction",
    client_id = "QktIf3FZ10C5jg",
    client_secret = "52XN7-d-s7tBO8Wld9mPQ19PMaV8HA"
)

# temporary df2
df2=pd.read_csv('E:\walstreet_sentiments_two\walstreet_2.0\data_exploration\some_data.csv').drop(['Unnamed: 0.1', 'Unnamed: 0'], axis=1)

# endpoints follow
@app.route('/live/', methods=['GET'])
def get_item():
    # Your code to fetch the item from the database goes here
    try:
        df=get_data(df2=df2, reddit=reddit, stocks=stocks, time=time)
        return df
    except Exception as e:
        return jsonify(message=str(e)), 400        


if __name__ == '__main__':
    app.run( host='localhost', port=9874,debug=True)