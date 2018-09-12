import React, { Component } from 'react';
import '../styles/SearchComponent.css';
import axios from 'axios';
import Suggestions from './Suggestions';

const TMDB_URL = 'https://api.themoviedb.org/3/search/person';
const { REACT_APP_TMDB_KEY }  = process.env;

class SearchComponent extends Component {
    state = {
        query: '',
        results: []
    }
     
    handleInputChange = () => {
        this.setState({
            query: this.search.value
        }, () => {
            if (this.state.query && this.state.query.length > 1) {
                if (this.state.query.length % 2 === 0) {
                    this.getInfo()
                }
            } else if (!this.state.query) {
                this.state.results = []
            }
        })
    }

    getInfo = () => {
        axios.get(`${TMDB_URL}?api_key=${REACT_APP_TMDB_KEY}&query=${this.state.query}`)
        .then(({ data }) => {
            this.setState({
              results: data.results                           
            })
        })
    }

    render() {
        return (
            <div className="search-container">
                <input className="search-input" 
                placeholder="Enter an actor..."
                ref={input => this.search = input}
                onChange={this.handleInputChange}
                />
                <Suggestions results={this.state.results}/>
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
