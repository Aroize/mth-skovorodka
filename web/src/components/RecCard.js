import React from 'react'
import {Link } from "react-router-dom";

const RecCard = ({name, id}) => {
    console.log(name, id)
    return (
        <div>
        <h3><Link to={`/article/${id}`}>{name}</Link></h3>
        </div>
    )
}

export default RecCard
