import axios from 'axios';

const gv_app = {
    app_name: '(주) 도울정보기술',
    app_url: 'http://127.0.0.1:8000',
};

export function getTitle(id) {
    return axios.get('http://localhost:8000/blog/index/' + id);
}

export function getData(data){
    const listData = [];        
    const list = data.map(
        info => (
          listData.push(info.fields)
        )
    );  
    return listData;
}

// var Button = React.createClass({

//     rNumberGen: function(){
//         let rNumbers = [Math.random(), Math.random(), Math.random()];
//     },

//     render: function(){
//         return(
//                 <TouchableHighlight onPress={this.rNumberGen} style={styles.center}>
//                         <Text style={styles.button}>Generate!</Text>
//                 </TouchableHighlight>
//             );
//     }

// });

export { gv_app }