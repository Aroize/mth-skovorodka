import {useState} from 'react'
import ReactMarkdown from 'react-markdown'
import axios from 'axios';

const Article = () => {
        const [article, setArticle] = useState("")

        axios.get('https://raw.githubusercontent.com/sherlock-project/sherlock/master/README.md')
        .then(resp => {setArticle(resp.data.toString())}) 
        .catch( (error) => {
          console.log(error);
        });  

        console.log(article)
      
        return (<ReactMarkdown children={article}></ReactMarkdown>);
    
}

export default Article
