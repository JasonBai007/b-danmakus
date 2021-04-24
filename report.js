const resultArr = require('./result.json')

let p = resultArr.filter(obj => obj.sentiment === 2)
let m = resultArr.filter(obj => obj.sentiment === 1)
let n = resultArr.filter(obj => obj.sentiment === 0)

let report = `正面：${p.length}条，负面：${n.length}条，中性：${m.length}条`

console.log(report)