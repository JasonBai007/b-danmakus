const fs = require('fs')
const path = require('path')
const keywordsArr = require('./fenci/danmu_keyword.json')

// 来自echarts的主题色
// https://echarts.apache.org/zh/theme-builder.html
const theme = [
    "#2ec7c9",
    "#b6a2de",
    "#5ab1ef",
    "#ffb980",
    "#d87a80",
    "#8d98b3",
    "#e5cf0d",
    "#97b552",
    "#95706d",
    "#dc69aa",
    "#07a2a4",
    "#9a7fd1",
    "#588dd5",
    "#f5994e",
    "#c05050",
    "#59678c",
    "#c9ab00",
    "#7eb00a",
    "#6f5553",
    "#c14089"
]

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
    fs.writeFileSync(path.resolve(__dirname, './report/keywords.json'), JSON.stringify(twoLevelArr, null, 4), { encoding: 'utf8' })
    console.log('生成关键词数据成功！')

    let top20Str = twoLevelArr.slice(0, 20).map((arr, i) => arr[0] + '|' + arr[1] + '|' + theme[i] + '|-|0').join('\n')
    fs.writeFileSync(path.resolve(__dirname, './report/yiciyun.txt'), top20Str, { encoding: 'utf8' })
    console.log('生成易词云数据成功！')

    // 返回前20名关键词
    let top20 = twoLevelArr.slice(0, 20)
    return top20
}