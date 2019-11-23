import React, { Component } from 'react'
import { BrowserRouter, Route} from 'react-router-dom'
// import { Router as BrowserRouter, Route, IndexRoute, Link, browserHistory } from 'react-router';
import Main from './pages/Main'
import NoMatch from './pages/NoMatch'
import SearchAppBar from './components/SearchAppBar'
import SwipeableTemporaryDrawer from './components/SwipeableTemporaryDrawer'


class Router extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return ( 
            <BrowserRouter>
                <SearchAppBar/>
                <Route path="/" exact component={Main}/>                    
                <Route path="/Left" component={SwipeableTemporaryDrawer}/>               
            </BrowserRouter>

        )
    }
}

export default Router;
