import React from 'react';
import { Route, Link, BrowserRouter as Router, Switch } from 'react-router-dom'

import HomePage from './components/HomePage';
import MachineLearning from './components/MachineLearning';
import CampSite from './components/CampSite';
import AddCampSite from './components/AddCampSite';
import NavBar from './components/NavBar';

import './../css/main.css';

const App = () => {
    return (
        <div>
            <NavBar />
            <div className="main-container">
                <Router>
                    <Route exact path='/' component={HomePage} />
                    <Route exact path='/machinelearning/' component={MachineLearning} />
                    <Route exact path='/campsites/' component={CampSite} />
                    <Route exact path='/add/campsite/' component={AddCampSite} />
                </Router>
            </div>
        </div>
    )
}

export default App;