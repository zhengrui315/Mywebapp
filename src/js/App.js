import React from 'react';
import { Route, Link, BrowserRouter as Router } from 'react-router-dom'

import HomePage from './components/HomePage';
import MachineLearning from './components/MachineLearning';

const App = () => {
    return (
        <div className="main-container">
            <Router>
                <Route exact path='/' component={HomePage} />
                <Route exact path='/ml' component={MachineLearning} />
            </Router>
        </div>
    )
}

export default App;