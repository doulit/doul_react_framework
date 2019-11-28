import React, { Component, useState, useEffect } from 'react';
import Table from '../components/Table';
import axios from 'axios';
import '../styles/index.css';
import * as service from '../settings/default';
import CircularProgress from '@material-ui/core/CircularProgress';

class Main extends Component {
  constructor(props) {
      super(props);
      this.state = {
        data: [],
        isloading: true,
        columns: [
          { title: 'name', field: 'name' },
          { title: 'code', field: 'code' },
          { title: 'level', field: 'level', type: 'numeric' },
        ]
      }
  }
  componentDidMount() {
		this.callSearchApi();
  }
  callSearchApi() {
    const data = service.search('/blog/menu/sel/').then(res => {       
      this.setState({data: res.data,isloading: false}); 			
    });
  }

  render() {
     if(this.state.isloading){ return(<div className="loading"><CircularProgress disableShrink /></div>)}
      return ( 
          <div>
            <Table
              source={this.state.data}
              columns={this.state.columns}
              title="조회화면"
              model="blog/menu"
            />

          </div>
      )
  }
}


export default Main;


