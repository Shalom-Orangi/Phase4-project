import { useEffect, useState } from "react";
import { useParams,useHistory } from "react-router-dom";

function ChallengesEditForm() {
  const[{data:challenge,errors,status},setChallenge]=useState({
    data:null,
    errors:[],
    status:"pending",
  });
  const [description, setDescription] = useState("");
  const history= useHistory();
  const {id} =useParams();

  useEffect(()=> {
    fetch(`http://127.0.0.1:4000/challenges/${id}`).then((r)=>{
        if(r.ok){
            r.json().then((challenge)=>{
                setChallenge({data:challenge,errors:[],status:"resolved"});
                setDescription(challenge.description);
            });
        } else{
            r.json().then((err)=>
                setChallenge({data:null,errors:[err.error],status:"rejected"})
            );
        }
    });
  },[id]);

  if (status === "pending") return <h1>Loading...</h1>;

  function handleSubmit(e){
    e.preventDefault();
    fetch(`http://127.0.0.1:4000/challenges/${challenge.id}`, {
        method: "PATCH",
        headers:{
            "Content-Type":"application/json",
        },
        body: JSON.stringify({
            description,
        }),
    }).then((r)=>{
        if (r.ok){
            history.push(`http://127.0.0.1:4000/challenges/${challenge.id}`);
        } else{
            r.json().then((err)=>
                setChallenge({data:challenge, errors:err.errors, status:"rejected" })
            );
        }
    });
  }

  return (
    <form onSubmit={handleSubmit}>
        <h2>Editing{challenge.title}</h2>
        <label htmlFor="description">Description:</label>
        <textarea
            id="description"
            name="description"
            rows={4}
            value={description}
            onChange={(e) =>setDescription(e.target.value)}
        />
        {errors.length > 0
            ?   errors.map((err)=>(
                    <p key={err} style={{color:"red"}}>
                        {err}
                    </p>
                ))
            :null}
        <button type="submit">Update Challenge</button>

      
    </form>
  );
}

export default ChallengesEditForm;
