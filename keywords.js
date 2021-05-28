const keyword = require('./report_keywords.js')

// 生成TOP20关键词数据
let top20 = keyword.generateKeywordReport()
let topStr = top20.map(arr=> arr[0]+' '+ arr[1] + '\n').join('')

console.log(topStr)