import HomePage from "./pages/HomePage";
import {BrowserRouter as Router,Routes,Route} from 'react-router-dom';


function App() {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/:page" element={<HomePage />}></Route>
        </Routes>
      </Router>
    </>
  );
}

export default App;
