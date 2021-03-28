import {useState, useEffect} from 'react'
import ReactMarkdown from 'react-markdown'
import axios from 'axios';
import ArticlesRec from './ArticlesRec';

const Article = () => {
        const [article, setArticle] = useState("")
        const [isStared, setIsStared] = useState(false)

        useEffect(() => {
          axios.get('https://raw.githubusercontent.com/sherlock-project/sherlock/master/README.md')
          .then(resp => {setArticle(resp.data.toString())}) 
          .catch( (error) => {
            console.log(error);
          });  
        }, [article])
      
      
        return (
          <div>
          <div class="article">
          <button class="star" onClick={() => setIsStared(!isStared)}>{isStared ? "+" : "-"}</button>
          <ReactMarkdown children={article}></ReactMarkdown>
          </div>
          <div class="rec-wrapper">
          <ArticlesRec/>
          </div>
          </div>
          );
    
}

export default Article
