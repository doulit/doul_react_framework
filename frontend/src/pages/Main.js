import React, { Component, useState, useEffect } from 'react';
import Table from '../components/Table';
import axios from 'axios';
import * as service from '../settings/default';

class Main extends Component {
  constructor(props) {
      super(props);
      this.state = {
        data: [],
        isloading: true
      }
  }
  componentDidMount() {
		this.callSearchApi();
  }
  callSearchApi() {
    axios.get(service.gv_app.app_url+'/blog/index/').then(res => {       
      const listData = service.getData(res.data);  
      this.setState({data: listData,isloading: false}); 			
    });
  }
  
  render() {
     if(this.state.isloading){ return(<div>...Loading</div>)}
      return ( 
          <div>
            <Table
              source={this.state.data}
            />

          </div>
      )
  }
}


export default Main;


