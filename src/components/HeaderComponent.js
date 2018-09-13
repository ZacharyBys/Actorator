import React, { Component } from 'react';
import SearchComponent from './SearchComponent';
import '../styles/HeaderComponent.css';

class HeaderComponent extends Component {
  render() {
    return (
      <div className="header-container">
        <h1 className="header-title">Actorator</h1>
      </div>
    );
  }
}

export default HeaderComponent;