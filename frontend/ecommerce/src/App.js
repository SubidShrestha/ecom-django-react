import HomePage from "./pages/HomePage";
import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import LoginPage from "./pages/LoginPage";
import './App.css';


function App() {
  return (
    <>
      <Router>
        <div className="navbar">
          <Link to='/' className="nav-item">Home</Link>
          <Link to='/login' className="nav-item">Login</Link>
        </div>
        <Routes>
          <Route path="/" element={<HomePage />}></Route>
          <Route path="/login" element={<LoginPage/>}></Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
