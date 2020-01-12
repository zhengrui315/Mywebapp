import React from 'react';
import { Route, Link, BrowserRouter as Router, Switch } from 'react-router-dom'

import HomePage from './components/HomePage';
import MachineLearning from './components/MachineLearning';
import CampSite from './components/CampSite';
import AddCampSite from './components/AddCampSite';
import NBAMap from './components/NBAMap';
import DateSlider from './components/DateSlider/DateSlider';
import NavBar from './components/NavBar';
import NoMatch from './components/NoMatch';

import './../css/main.css';

const App = () => {
    return (
        <Router>
            <NavBar />
            <div className="main-container">
                <Switch>
                    <Route exact path='/' component={HomePage} />
                    <Route exact path='/machinelearning/' component={MachineLearning} />
                    <Route exact path='/campsites/' component={CampSite} />
                    <Route exact path='/campsite_add/' component={AddCampSite} />
                    <Route exact path='/nba/' component={NBAMap} />
                    <Route exact path='/test/' component={DateSlider} />
                    <Route component={NoMatch} />
                </Switch>
            </div>
        </Router>
    )
}

export default App;