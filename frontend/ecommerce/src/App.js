import HomePage from "./pages/HomePage";
import {BrowserRouter as Router,Routes,Route} from 'react-router-dom';
import LoginPage from "./pages/LoginPage";


function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<HomePage />}></Route>
          <Route path="/?:page" element={<HomePage />}></Route>
          <Route path="/login" element={<LoginPage/>}></Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
