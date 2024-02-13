import {Link} from 'react-router-dom'
import Challenges from './Challenge'

function Header() {
  return (
    <header>
      <h1>
        <Link to="/">AfyaFit Tracker App</Link>
        <Challenges/>
      </h1>
    </header>
  )
}

export default Header
