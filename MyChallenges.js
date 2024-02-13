import {useEffect,useState} from "react";
import {useHistory} from "react-router-dom";


function MyChallenges() {
    const[users, setUsers]=useState([]);
    const[challenges, setChallenges]=useState([]);
    const[userId, setUserId]=useState("");
    const[challengeId, setChallengeId]=useState("");
    const[completed,setCompleted]=useState("");
    const[formErrors, setFormErrors]=useState([]);
    const history=useHistory();

    useEffect(()=>{
        fetch("http://127.0.0.1:4000/users")
            .then((r)=>r.json())
            .then (setUsers);
    },[]);

    useEffect(()=>{
        fetch("http://127.0.0.1:4000/challenges")
        .then((r)=>r.json())
        .then(setChallenges);
    },[]);
    
    function handleSubmit(e) {
        e.preventDefault();
        const formData ={
            user_id: userId,
            challenge_id: challengeId,
            completed,
        };
        fetch ("http://127.0.0.1:4000/my-challenges",{
            method:"POST",
            headers:{
                "Content-Type": "application/json",
            },
            body:JSON.stringify(formData),
        }).then((r)=>{
            if(r.ok) {
                history.push(`/users/${userId}`);
            }else {
                r.json().then((err)=> setFormErrors(err.errors));
            }
        });
    }

  return (
    <form onSubmit={handleSubmit}>
        <label htmlFor="challenge_id">Challenge:</label>
        <select
            id="challenge_id"
            name="challenge_id"
            value={challengeId}
            onChange={(e)=> setChallengeId(e.target.value)}
        >
            <option value="">Select a challenge</option>
            {challenges.map((challenge)=>(
                <option key={challenge.id} value={challenge.id}>
                    {challenge.title}
                </option>
            ))}
        </select>
        <label htmlFor="user_id">User:</label>
        <select
            id="user_id"
            name="user_id"
            value={userId}
            onChange={(e) => setUserId(e.target.value)}
        >
            <option value="">Select a User</option>
            {users.map((user)=>(
                <option key={user.id} value={user.id}>
                    {user.username}
                </option>
            ))}
        </select>
        <label htmlFor="completed">Completed:</label>
        <input
            type="text"
            id="completed"
            name="completed"
            value={completed}
            onChange={(e)=>setCompleted(e.target.value)}
        />
        {formErrors.length > 0
            ?   formErrors.map((err)=>(
                    <p key={err} style={{color:"red"}}>
                        {err}
                    </p>
                ))
            :null}
        <button type="submit">Add User Challenge Progress</button>
    </form>
  );
}

export default MyChallenges;
