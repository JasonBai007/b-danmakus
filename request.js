const fs = require('fs')
const path = require('path')
const axios = require('axios')
const danmu = require('./res/test.json')
const base_url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify'
const access_token = '' // your access token
const charset = 'UTF-8' // 必须是这种编码
const request_url = `${base_url}?access_token=${access_token}&charset=${charset}`
const file_path = path.resolve(__dirname, './result.json')

/* 最多并发两个请求，所以下面的方法会导致接口报错：
{ error_code: 18, error_msg: 'Open api qps request limit reached' } */

// let request_queue = danmu.map(str => {
//     return axios.post(request_url, { text: str })
// })

// Promise.all(request_queue).then(function (resArr) {
//     console.log(resArr)
// });

function generateFile(data) {
    // 异步写入数据到文件
    fs.writeFile(file_path, JSON.stringify(data, null, 4), { encoding: 'utf8' }, err => { })
}

let resArr = []
let danmu_index = 0
let intervalId = null
intervalId = setInterval(() => {
    axios.post(request_url, { text: danmu[danmu_index] }).then(res => {
        resArr.push({
            text: res.data.text,
            ...res.data.items[0]
        })
        danmu_index++;
        if (danmu_index >= danmu.length) {
            clearInterval(intervalId)
            console.log(`Request ${danmu_index} times, done`)
            generateFile(resArr)
        }
    })

}, 500);


