const fs = require('fs')
const path = require('path')
const axios = require('axios')
const danmu = require('./danmu/danmu_text.json') // 弹幕JSON数据
const base_url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify'
const access_token = '' // your access token
const charset = 'UTF-8' // 必须是这种编码
const request_url = `${base_url}?access_token=${access_token}&charset=${charset}`
const file_path = path.resolve(__dirname, './sentiment/danmu_sentiment.json')

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
    fs.writeFile(file_path, JSON.stringify(data, null, 4), { encoding: 'utf8' }, err => {
        console.log('附带情感值的弹幕数据 danmu_sentiment.json 已生成')
        console.log('执行 node report.js 生成分析报告')
    })
}

let resArr = []
let danmu_index = 0
let danmuLength = danmu.length
let intervalId = null
intervalId = setInterval(() => {
    axios.post(request_url, { text: danmu[danmu_index] }).then(res => {
        console.log(`正在分析第 ${danmu_index + 1}/${danmuLength} 条弹幕数据...`)
        resArr.push({
            id: danmu_index,
            text: res.data.text,
            ...res.data.items[0]
        })
        danmu_index++;
        if (danmu_index >= danmuLength) {
            clearInterval(intervalId)
            console.log(`分析完毕，写入文件中...`)
            generateFile(resArr)
        }
    })

}, 1000);


