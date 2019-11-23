import React, { Component } from 'react'
import { BrowserRouter, Route} from 'react-router-dom'
import Main from './pages/Main'
import Table from './pages/Table'
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
                <Route path="/" exact component={Table}/>                    
                <Route path="/Main" exact component={Main}/> 
                <Route path="/Table" exact component={Table}/>      
                <Route path="/Left" component={SwipeableTemporaryDrawer}/>               
            </BrowserRouter>

        )
    }
}

export default Router;

