import React from 'react'

const Profile = () => {

    const tags = ["science", "art", "DIY", "selfie"]

    return (
        <div class="profile-card">
            <img src="../avatar.png" alt="avatar"></img>
            <h2>Иванов Иван</h2>
            <div class="tags">
Tags: 
            {
                tags.map((element, index) =>
                    (<span class="tag" key={index}>{element}</span>)
                    )
                }
                </div>
        </div>
    )
}

export default Profile
