import React from 'react'

const Profile = () => {

    const tags = ["Вселенная", "наука", "материалы", "жизнь"]

    return (
        <div class="profile-card">
            <img src="../avatar.png" alt="avatar"></img>
            <h2>Иванов Иван (17 лет)</h2>
            <div class="tags">
Tags: 
            {
                tags.map((element, index) =>
                    (<span class="tag" key={index}>{element}</span>)
                    )
                }
                </div>
                <div class= "ways">
                    <button class = "A">Маршрут А</button>
                    <button class = "B">  Маршрут Б</button>
                    <button class = "C">Маршрут В</button>
                    <button class = "D">Маршрут Г</button>
                </div>
        </div>
    )
            }

export default Profile
