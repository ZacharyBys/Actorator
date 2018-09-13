import React, { Component } from 'react';
import SearchComponent from './SearchComponent';
import HeaderComponent from './HeaderComponent';
import '../styles/FrontPage.css';

class FrontPage extends Component {
  render() {
    return (
        <div className="front-page-container">
            <HeaderComponent/>
            <SearchComponent/>
        </div>
    );
  }
}

export default FrontPage;