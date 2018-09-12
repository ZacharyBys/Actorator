import React, { Component } from 'react';
import '../styles/SearchComponent.css';

class SearchComponent extends Component {
  render() {
    return (
        <div className="search-container">
            <input className="search-input" placeholder="Enter an actor..."></input>
            <div className="search-button-container">
                <p className="search-button-text">
                    Compute Score
                </p>
            </div>
        </div>
    );
  }
}

export default SearchComponent;
