import React from 'react';
import '../styles/Suggestions.css';

const Suggestions = (props) => {
  const options = props.results.map(r => (
    <li key={r.id}>
      {r.name}
    </li>
  ))
  return <div className="suggestions-container"><ul className="suggestions-list">{options}</ul></div>
}

export default Suggestions