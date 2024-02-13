import './App.css';
import Navbar from './components/pages/Navbar';
import { BrowserRouter as Routes,Route, Router } from 'react-router-dom'
import Header from './components/pages/Header';
import User from "./components/pages/User";
import MyChallenges from './components/pages/MyChallenges';
import Challenges from './components/pages/Challenge';
import ChallengesEditForm from './components/pages/ChallengesEditForm';


function App() {
  return (
      <div >
        <Router>
          <Navbar/>
          <Routes>
            <Route path="/" element={<Header/>}/>
            <Route path="/my-challenges/new" element={<MyChallenges/>}/>
            <Route path="/challenges/:id/edit" element={<ChallengesEditForm/>}/>
            <Route path="/challenges/:id" element={<Challenges/>}/>
            <Route psth="users/:id" element={<User/>}/>
          </Routes>
        </Router>
      </div>
  );
}

export default App;
