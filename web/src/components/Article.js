import {useState, useEffect} from 'react'
import ReactMarkdown from 'react-markdown'
import axios from 'axios';
import ArticlesRec from './ArticlesRec';

const Article = () => {
        const [article, setArticle] = useState("")
        const [rec, setRec] = useState({})
        const [isStared, setIsStared] = useState(false)

        useEffect(() => {
          let headers = new Headers()
          headers.append('Access-Control-Allow-Origin', 'http://localhost:3000');
          // axios.get('https://raw.githubusercontent.com/sherlock-project/sherlock/master/README.md')
          // .then(resp => {setArticle(resp.data.toString())}) 
          // .catch( (error) => {
          //   console.log(error);
          // });  
          axios.get('https://stark-chamber-07526.herokuapp.com/paper?p_id=1')
          .then(resp => { console.log(resp)
            axios.get(resp.data).then(res => setArticle(res.data))
            // setArticle(resp.data.toString())
            // console.log(resp)
          })
          .catch( (error) => {
            console.log(error);
          });  
        }, [article])

        // useEffect(() => {
        //   let headers = new Headers()
        //   headers.append('Access-Control-Allow-Origin', 'http://localhost:3000');
        //   axios.get('https://stark-chamber-07526.herokuapp.com/data.getStartingReommendations')
        //   .then(resp => { console.log(resp)
        //     axios.get(resp.data).then(res => setArticle(res.data))
        //     // setArticle(resp.data.toString())
        //     // console.log(resp)
        //   })
        //   .catch( (error) => {
        //     console.log(error);
        //   });  
        // }, [article])
      
      
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
