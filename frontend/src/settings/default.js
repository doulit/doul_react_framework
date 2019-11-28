import axios from 'axios';

let dev_url = 'http://127.0.0.1:8000';
let qas_url = 'http://54.180.118.173:8000';
let prd_url = 'http://54.180.118.173:8000';
const gv_app = {
    app_name: '(주) 도울정보기술',
    app_url: dev_url,
    app_type: "L",
};

const axios_headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json;charset=UTF-8'
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
}else if (window.location.href.indexOf('54.180.118.173') > -1 || window.location.href.indexOf('ec2-54-180-118-173.ap-northeast-2.compute.amazonaws.com') > -1){
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
    let options = {
        method: 'POST',
        url: gv_app.app_url+url+type+"/",
        headers: axios_headers,
        data: {
            id: 1
          }
    };
    // let response = axios(options);
    // let responseOK = response && response.status === 200 && response.statusText === 'OK';
    // if (responseOK) {
    //     let data = response.data;
    //     // do something with data
    // }

    // return response;
    // return axios.post(gv_app.app_url+url+type+"/", {
    //             data: {
    //                 data
    //             }
    //         });

    return axios({
        method:'post',
        url: gv_app.app_url+url+type+"/",
        data: data
    });
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