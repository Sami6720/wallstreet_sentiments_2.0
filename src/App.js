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
      <Grid item xs={12} sm={6} md={6} lg={4}>
        <DataCard name={"Today's Data"}></DataCard>
      </Grid>
      <Grid item xs={12} sm={6} md={6} lg={4}>
        <DataCard name={"Yesterday's Data"}></DataCard>
      </Grid>
      <Grid item xs={12} lg={4}>
        <DataCard name={"This Month's Data"}></DataCard>
      </Grid>
      <Grid item xs={12} sm={12} md={12} lg={12}>
        <DataCard name={"Top voted comments"}></DataCard>
      </Grid>
    </Grid>
  );
}

export default App;
