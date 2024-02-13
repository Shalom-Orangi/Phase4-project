import { useEffect,useState } from "react";
import {Link,useParams} from "react-router-dom";

function User(){
    
    const [{data: user, error,status }, setUser]=useState({
        data:null,
        error:null,
        status:"pending",
    });
    const {id} =useParams();

    useEffect(()=>{
        fetch(`http://127.0.0.1:5555/users/${id}`).then((r)=>{
            if (r.ok){
                r.json().then((user)=>
                    setUser({data:user,error:null , status:"resolved"})
                );
            } else {
                r.jsoon().then((err)=>
                setUser({data:null, error:err.error, status:"rejected"})
                );
            }
        });
    },[id]);

    if (status ==="pending")return <h1>Loading...</h1>;
    if(status === "rejected") return <h1>Error: {error.error}</h1>

    return (
    <section>
      <h2>{user.username}</h2>
      <h2>{user.fitness_goals}</h2>

      <h3>Challenges:</h3>
      <ul>
        {user.challenges.map((challenge)=>(
            <li key={user.id}>
                <Link to={`/challenges/${challenge.id}`}>{challenge.title}</Link>
            </li>
        ))}
      </ul>

      <Link to="my-challenges/new">Add New Challenge </Link>
        </section>
    );
}

export default User;
