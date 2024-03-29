const fs = require('fs')
const path = require('path')
const videoInfo = require('./danmu/info.json')
const resultArr = require('./sentiment/danmu_sentiment.json')
const keyword = require('./report_keywords.js')

let p = resultArr.filter(obj => obj.sentiment === 2)
let m = resultArr.filter(obj => obj.sentiment === 1)
let n = resultArr.filter(obj => obj.sentiment === 0)

let total = resultArr.length

let pNum = p.length
let nNum = n.length
let mNum = m.length

let pRatio = (pNum / total * 100).toFixed(2)
let nRatio = (nNum / total * 100).toFixed(2)
let mRatio = (mNum / total * 100).toFixed(2)

console.log(`《${videoInfo.title}》弹幕情感分析报告：`)
console.log(`该视频总计 ${total} 条弹幕`)
console.log(`正面情感弹幕 ${pNum} 条，占比 ${pRatio}%`)
console.log(`负面情感弹幕 ${nNum} 条，占比 ${nRatio}%`)
console.log(`中性情感弹幕 ${mNum} 条，占比 ${mRatio}%`)
console.log(`生成测试报告中...`)



fs.writeFile(path.resolve(__dirname, './report/positive.json'), JSON.stringify(p, null, 4), { encoding: 'utf8' }, err => {
    console.log('抽离正面数据成功！')
})
fs.writeFile(path.resolve(__dirname, './report/negative.json'), JSON.stringify(n, null, 4), { encoding: 'utf8' }, err => {
    console.log('抽离负面数据成功！')
})

if (mNum > 0) {
    fs.writeFile(path.resolve(__dirname, './report/neutral.json'), JSON.stringify(m, null, 4), { encoding: 'utf8' }, err => {
        console.log('抽离中性数据成功！')
    })
}

// 生成TOP20关键词数据
let top20 = keyword.generateKeywordReport()
let topStr = top20.map(arr=> arr[0]+' '+ arr[1] + '\n').join('')

let report = `《${videoInfo.title}》弹幕情感分析报告：\n\n 该视频总计 ${total} 条弹幕 \n 正面情感弹幕 ${pNum} 条，占比 ${pRatio}% \n 负面情感弹幕 ${nNum} 条，占比 ${nRatio}% \n 中性情感弹幕 ${mNum} 条，占比 ${mRatio}% \n\n前20名关键词和频次： \n${topStr}`
fs.writeFile(path.resolve(__dirname, './report/report.txt'), report, { encoding: 'utf8' }, err => {
    console.log('分析报告生成完成！')
})