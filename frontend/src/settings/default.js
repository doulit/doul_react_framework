import axios from 'axios';

let dev_url = 'http://127.0.0.1:8000';
let qas_url = 'http://54.180.118.173:8000';
let prd_url = 'http://54.180.118.173:8000';
const gv_app = {
    app_name: '(주) 도울정보기술',
    app_url: dev_url,
    app_type: "L",
};

/**
 * Url 설정
 *      L : 로컬
 *      Q : 교육
 *      P : 운영
 */
if (window.location.href.indexOf('localhost') > -1){
    gv_app.app_url = dev_url;
    gv_app.app_type = "L";
}else if (window.location.href.indexOf('54.180.118.173') > -1){
    gv_app.app_url = qas_url;
    gv_app.app_type = "Q";
}else if (window.location.href.indexOf('localhost') > -1){
    gv_app.app_url = prd_url;
    gv_app.app_type = "P";
}else{
    gv_app.app_url = dev_url;
    gv_app.app_type = "L";
}

export function search(url) {
    return axios.get(gv_app.app_url+url);
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

export function saveData(data, type, url){
    console.log("::saveData::");
    console.log(data);
    return axios.post(gv_app.app_url+url+type+"/");
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