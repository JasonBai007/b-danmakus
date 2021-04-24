const videoInfo = require('./res/info.json')
const resultArr = require('./result.json')

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