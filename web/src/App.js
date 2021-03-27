import Article from "./components/Article";
import SignUp from "./components/SignUp";
import SignIn from "./components/SignIn";
import NavBar from './components/NavBar'
import {Route, BrowserRouter } from "react-router-dom";
import ArticlesRec from "./components/ArticlesRec";
import Towards from './components/Towards'
import Profile from './components/Profile'

const App = () => {
  return (
    <div>
    <BrowserRouter>
    <NavBar/>
    <Route path={'/signin'} component={SignIn} />
    <Route path={'/towards'} component={Towards} />
    <Route path={'/signup'} component={SignUp} />
    <Route path={'/article'} component={Article} />
    <Route path={'/rec'} component={ArticlesRec} />
    <Route path={'/profile'} component={Profile} />
  </BrowserRouter>

    </div>
  );
}

export default App;
