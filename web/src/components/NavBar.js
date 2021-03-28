import React, {useState} from 'react'
import {Link} from "react-router-dom";

const NavBar = () => {
    const [Auth, setAuth] = useState(false)

    return (
<nav>
  <ul>
    <li><Link to='/article'>Home</Link></li>
    <li><Link to='/towards'>Достижения</Link></li>
    <li><Link to='/history'>История</Link></li>
    <li><Link to='/rec'>Рек</Link></li>
    <span class="right-text">
    {Auth && (
    <div>
    <li><Link to='/signup'>Зарегистрироваться</Link></li>
    <li><Link to='/signin'>Войти</Link></li>
    </div>
    )}
    {!Auth && (
    <div>
    <li><Link to='/profile'>Профиль</Link></li>
    <li><Link onClick={() => setAuth(!Auth)}>Выйти</Link></li>
    </div>
    )}
    </span>
  </ul>
</nav>
    )
}

export default NavBar
