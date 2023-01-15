import logo from './logo.svg';
import './App.css';
import Grid from '@mui/material/Grid'; // Grid version 1
import Navbar from './components/Navbar';

function App() {
  return (
    <div className="App">
      
      <Navbar></Navbar>
      <Grid container spacing={2}>
        <Grid item>
        </Grid>
      </Grid>
    </div>
  );
}

export default App;
