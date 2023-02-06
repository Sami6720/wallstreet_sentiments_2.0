import logo from "./logo.svg";
import "./App.css";
import Grid from "@mui/material/Grid"; // Grid version 1
import Navbar from "./components/Navbar";
import { Toolbar } from "@mui/material";
import DataCard from "./components/DataCard";
import { useEffect, useState } from "react";

function App() {
  // Code to update live data columns

  const [df2, changedf2] = useState(
    // df2 refers to past df
    [
      { id: 1, stocks: "sami", total_compound_x: 35, change: 5 },
      { id: 2, stocks: "orthy", total_compound_x: 35, change: 5 },
    ]
  );

  const [yesterdayDf, changeyesterdayDf] = useState(
    // df2 refers to past df
    [
      { id: 1, stocks: "sami", total_compound: 35, change: 5 },
      { id: 2, stocks: "orthy", total_compound: 35, change: 5 },
    ]
  );

  // useEffect for fetching real-time data
  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch("http://localhost:9874/live/");
      const json = await response.json();
      console.log(json);
      changedf2(json);
    };
    fetchData(); // to run fetchData immidiately after the component is mounted.
    const intervalId = setInterval(fetchData, 10 * 60 * 1000); // 5 minutes in milliseconds
    const currentTime = new Date();
    return () => clearInterval(intervalId);
  }, []);

  // useEffect to run everyday at 23:55:00:00 hours
  useEffect(() => {
    // important to set different functio names in useEffects
    const fetchYesData = async () => {
      const response = await fetch("http://localhost:9874/live/");
      const json = await response.json();
      changeyesterdayDf(json);
    };

    const desiredTime = new Date();
    desiredTime.setHours(8, 15, 0, 0); // 23:55:00:00 hours
    let timeToWait = desiredTime - new Date();
    if (timeToWait < 0) {
      timeToWait += 86400000; // 24 hours in milliseconds
    }

    setTimeout(() => {
      fetchYesData();
      setInterval(fetchYesData, 86400000); // 24 hours in milliseconds
    }, timeToWait);
  }, []);

  return (
    <Grid container spacing={2}>
      <Grid item xs={12} md={12} lg={12}>
        <Navbar></Navbar>
        <Toolbar></Toolbar>
        {/* The empty toolbar component makes sure that  */}
      </Grid>
      <Grid item xs={12} sm={6} md={6} lg={6}>
        <DataCard name={"In the last ten mins"} rows={df2}></DataCard>
      </Grid>
      <Grid item xs={12} sm={6} md={6} lg={6}>
        <DataCard name={"Yesterday's end of day"} rows={yesterdayDf}></DataCard>
      </Grid>

      <Grid item xs={12} sm={12} md={12} lg={12}>
        <DataCard name={"Top voted comments"} rows={df2}></DataCard>
      </Grid>
    </Grid>
  );
}

export default App;
