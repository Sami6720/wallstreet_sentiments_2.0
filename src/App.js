import logo from "./logo.svg";
import "./App.css";
import Grid from "@mui/material/Grid"; // Grid version 1
import Navbar from "./components/Navbar";
import { Toolbar } from "@mui/material";
import DataCard from "./components/DataCard";

function App() {
  return (
    <Grid container spacing={2}>
      <Grid item xs={12} md={12} lg={12}>
        <Navbar></Navbar>
        <Toolbar></Toolbar>
        {/* The empty toolbar component makes sure that  */}
      </Grid>
      <Grid item xs={12} sm={6} md={6} lg={6}>
        <DataCard name={"In the last five mins"}></DataCard>
      </Grid>
      <Grid item xs={12} sm={6} md={6} lg={6}>
        <DataCard name={"Yesterday's end of day"}></DataCard>
      </Grid>

      <Grid item xs={12} sm={12} md={12} lg={12}>
        <DataCard name={"Top voted comments"}></DataCard>
      </Grid>
    </Grid>
  );
}

export default App;
