import React from 'react'
import RecCard from './RecCard'
const ArticlesRec = () => {

    const dataRec = [{id: 1, name: "Article 1"}, {id: 2, name: "Article 2"}, {id: 3, name: "Article 3"}, {id: 4, name: "Article 4"}, , {id: 5, name: "Article 5"}]

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
