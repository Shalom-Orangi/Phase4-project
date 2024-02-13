import React from "react";
import"../styles/Navbar.css";
import logo from "../assets/logo.png";
import { Link } from "react-router-dom";


const Navbar=()=>{
    
    return(
        <div className="navbar">
            <div className="leftSide">
                <img src={logo} alt='logo'/>
                <header><h1>AfyaFit Tracker App</h1></header>
            </div>
            <div className="rightSide">
                <Link className="navLink" to="/" >Home</Link> 
                <Link className="navLink" to="/challenges">Challenges</Link>
                <Link className="navLink" to="/my-challenges">My-Challenges</Link>
                <Link className="navLink" to= "/LoginSignup">Login</Link>
            </div>  

        </div>
    )
}

export default Navbar;