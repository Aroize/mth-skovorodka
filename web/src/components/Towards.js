import React from 'react'
import TowardsCard from './TowardsCard';

const levelList = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]

const Towards = () => {
    return (

    levelList.map(element => 
        <TowardsCard level={element} key={element}/>)
    
)}



export default Towards
