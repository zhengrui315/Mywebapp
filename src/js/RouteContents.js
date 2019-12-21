import React from 'react';
import { Switch, Route } from 'react-router-dom';
import HomePage from './components/HomePage';

const RouteContents = () => {
    <div>
        <Switch>
            <Route exact path='/' component = {HomePage} />
        </Switch>
    </div>
}

export default RouteContents;