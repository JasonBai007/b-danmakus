const fs = require('fs')
const path = require('path')
const keywordsArr = require('./fenci/danmu_keyword.json')

exports.generateKeywordReport = function () {
    // 扁平化：二维数组 --> 一维数组
    let _arr = keywordsArr.flat()
    // 提取出现次数
    let _obj = {}
    _arr.forEach(str => {
        if (!_obj[str]) {
            _obj[str] = 1
        } else {
            _obj[str]++
        }
    });
    // 对象转二维数组
    let twoLevelArr = Object.entries(_obj)
    // 根据权重排序
    twoLevelArr.sort((a, b) => {
        return b[1] - a[1]
    })
    fs.writeFile(path.resolve(__dirname, './report/keywords.json'), JSON.stringify(twoLevelArr, null, 4), { encoding: 'utf8' }, err => {
        console.log('生成关键词数据成功！')
    })
}