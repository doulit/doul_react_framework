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
          { title: 'Name', field: 'name' },
          { title: 'Surname', field: 'surname' },
          { title: 'Birth Year', field: 'birthYear', type: 'numeric' },
          {
            title: 'Birth Place',
            field: 'birthCity',
            lookup: { 34: 'İstanbul', 63: 'Şanlıurfa' },
          },
        ]
      }
  }
  componentDidMount() {
		this.callSearchApi();
  }
  callSearchApi() {
    const data = service.search('/blog/sel/1/').then(res => {       
      const listData = service.getData(res.data);  
      this.setState({data: listData,isloading: false}); 			
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
              url="/blog/save/"
            />

          </div>
      )
  }
}


export default Main;


