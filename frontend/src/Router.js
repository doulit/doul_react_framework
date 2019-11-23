import React, { Component } from 'react'
import { BrowserRouter, Route, Switch, Link } from 'react-router-dom'
import Main from './pages/Main'
import SearchAppBar from './components/SearchAppBar'
import './settings/default'
const routes = [
    {
        path: '/',
        menuName: '수업관리',
        menuId: 'sub1',
        children: [
            {
                path: '/LectureSchedule',
                menuName: '공학 교수계획표 관리',
                key: '1',
            },
        ],
    },
    {
        path: '/',
        menuName: 'sub2',
        menuId: 'sub2',
    },
    {
        path: '/',
        menuName: 'sub3',
        menuId: 'sub3',
    },
];



class Router extends Component {
    constructor(props) {
        super(props);
    }



    render() {
        return (            
            <BrowserRouter>   
                <SearchAppBar/>    
                <Route path="/" component={Main} />
                <Route path="/Main" component={Main} />
                <Route path="/lionking" component={Main} />
                <Route path="/spiderman" component={Main} />
            </BrowserRouter>
        )
    }
}

export default Router;