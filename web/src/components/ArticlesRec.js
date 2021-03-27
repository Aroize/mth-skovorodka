import React from 'react'
import RecCard from './RecCard'
const ArticlesRec = () => {

    const dataRec = [{id: 1, name: "Article 1"}, {id: 2, name: "Article 2"}]

    return (
        dataRec &&
        dataRec.map((rec) => (
              <RecCard
              key={rec.id}
              id={rec.id}
                name={rec.name}
              />
            ))
    
        
    )
}

export default ArticlesRec
