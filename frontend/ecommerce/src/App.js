import HomePage from "./pages/HomePage";
import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import LoginPage from "./pages/LoginPage";
import RegisterPage from "./pages/RegisterPage";
import './App.css';
import React from 'react';


function App() {
  return (
    <>
      <Router>
        <div className="navbar">
          <Link to='/' className="nav-item">Home</Link>
          <Link to='/login' className="nav-item">Login</Link>
          <Link to='/register' className="nav-item">Register</Link>
          <Link to='/' className="nav-item">Cart <i className="fa fa-shopping-cart" style={{background: 'transparent',padding: "0px 0px 0px 3px"}}></i></Link>
        </div>
        <Routes>
          <Route path="/" element={<HomePage />}></Route>
          <Route path="/login" element={<LoginPage/>}></Route>
          <Route path="/register" element={<RegisterPage/>}></Route>
          <Route path="*" element={<LoginPage/>}></Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
