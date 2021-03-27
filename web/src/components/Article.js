import {useState, useEffect} from 'react'
import ReactMarkdown from 'react-markdown'
import axios from 'axios';
import ArticlesRec from './ArticlesRec';

const Article = () => {
        const [article, setArticle] = useState("")

        useEffect(() => {
          axios.get('https://raw.githubusercontent.com/sherlock-project/sherlock/master/README.md')
          .then(resp => {setArticle(resp.data.toString())}) 
          .catch( (error) => {
            console.log(error);
          });  
        }, [article])
      
      
        return (
          <div>
          <ReactMarkdown children={article}></ReactMarkdown>
          <ArticlesRec/>
          </div>
          );
    
}

export default Article
