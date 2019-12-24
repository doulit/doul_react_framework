import React, { Component } from 'react'
import { BrowserRouter, Route} from 'react-router-dom'
import Main from './pages/Main'
import Menu from './pages/Menu'
import NoMatch from './pages/NoMatch'
import SearchAppBar from './components/SearchAppBar'


class Router extends Component {
    constructor(props) {
        super(props);
    }
    render() {
        return ( 
            <BrowserRouter>
                <SearchAppBar/>
                <Route path="/" exact component={Main}/>                    
                <Route path="/Main" exact component={Main}/>   
                <Route path="/Menu" exact component={Menu}/>         
            </BrowserRouter>

        )
    }
}

export default Router;

