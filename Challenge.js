
import { useEffect,useState } from 'react'
import { Link, useParams } from 'react-router-dom';

function Challenges() {
  const[{data:challenge, error, status},setChallenge]=useState({
    data:null,
    error:null,
    status:"pending",

  });

  const{ id }=useParams();
  useEffect(() => {
    fetch(`http://127.0.0.1:4000/challenges/${id}`).then((r) => {
      if (r.ok) {
        r.json().then((challenge) =>
          setChallenge({data:challenge, error:null, status:"resolved"})
        );
      } else {
        r.json().then((err) =>
          setChallenge({ data:null, error:err.error, status:"rejected" })
        ); 
      }
    });
  }, [id]);

  if(status ==="pending") return <h1>Loading...</h1>
  if(status ==="rejected")return <h1>Error: {error.error}</h1>;


  return (
    <section >
      <h2>{challenge.title}</h2>
      <p>{challenge.description}</p>
      <p>
        <Link to="/my-challenges/new">Add New Challenge</Link>
      </p>
      <p>
        <Link to ={`/challenges/${challenge.id}/edit`}>Edit Challenge Description</Link>
      </p>
    </section>
  );
}

export default Challenges;
