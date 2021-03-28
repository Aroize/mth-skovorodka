import React from 'react'
import TowardsCard from './TowardsCard';

const levelList = [0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 12]

const Towards = () => {
    return (
        <div class="towards-wrapper">
            {
            levelList.map( (element, index) =>  
                <TowardsCard level={element} key={index} id={index}/>
            )
            }
        </div>
        
    )
}

export default Towards
