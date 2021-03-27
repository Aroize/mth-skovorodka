import React from 'react'
import {Link} from "react-router-dom";

const NavBar = () => {
    return (
<nav>
  <ul>
    <li><Link to='/article'>Home</Link></li>
    <li><Link to='/signin'>Войти</Link></li>
    <li><Link to='/towards'>Достижения</Link></li>
    <li><Link to='/history'>История</Link></li>
    <li><Link to='/signup'>Зарегистрироваться</Link></li>
    <li><Link to='/rec'>Рек</Link></li>
  </ul>
</nav>
    )
}

export default NavBar
