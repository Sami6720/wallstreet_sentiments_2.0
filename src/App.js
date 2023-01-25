import logo from "./logo.svg";
import "./App.css";
import Grid from "@mui/material/Grid"; // Grid version 1
import Navbar from "./components/Navbar";
import { Toolbar } from "@mui/material";
import DataCard from "./components/DataCard";
import { useState } from "react";

function App() {
  // Code to update live data columns

  const [df2, changef2] = useState(
    // df2 refers to past df
    [
      { id: 1, stocks: "sami", total_compound_x: 35, change: 5 },
      { id: 2, stocks: "orthy", total_compound_x: 35, change: 5 },
    ]
  );

  // function to run every 10 mins and call on end point

  return (
    <Grid container spacing={2}>
      <Grid item xs={12} md={12} lg={12}>
        <Navbar></Navbar>
        <Toolbar></Toolbar>
        {/* The empty toolbar component makes sure that  */}
      </Grid>
      <Grid item xs={12} sm={6} md={6} lg={6}>
        <DataCard name={"In the last five mins"} rows={df2}></DataCard>
      </Grid>
      <Grid item xs={12} sm={6} md={6} lg={6}>
        <DataCard name={"Yesterday's end of day"} rows={df2}></DataCard>
      </Grid>

      <Grid item xs={12} sm={12} md={12} lg={12}>
        <DataCard name={"Top voted comments"} rows={df2}></DataCard>
      </Grid>
    </Grid>
  );
}

export default App;
