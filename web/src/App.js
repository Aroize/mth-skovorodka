import Article from "./components/Article";
import SignUp from "./components/SignUp";
import SignIn from "./components/SignIn";
import NavBar from './components/NavBar'
import {Route, BrowserRouter } from "react-router-dom";
import Towards from './components/Towards'
import Profile from './components/Profile'
import History from './components/History'

const App = () => {
  return (
    <div>
    <BrowserRouter>
    <NavBar/>
    <Route path={'/signin'} component={SignIn} />
    <Route path={'/towards'} component={Towards} />
    <Route path={'/signup'} component={SignUp} />
    <Route path={'/article'} component={Article} />
    <Route path={'/history'} component={History} />
    <Route path={'/profile'} component={Profile} />
  </BrowserRouter>

    </div>
  );
}

export default App;