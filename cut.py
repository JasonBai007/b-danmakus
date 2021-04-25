# encoding=utf-8
import json
import jieba
import jieba.analyse

# 从JSON文件获取弹幕文本数据
danmuArr = []
with open('./danmu/danmu_text.json', encoding='UTF-8') as json_file:
	 danmuArr = json.load(json_file)

# 分词并写入文件
danmu_cutted = []
for str in danmuArr:
    seg_list = jieba.cut(str)
    danmu_cutted.append(list(seg_list))

with open('./fenci/danmu_cut.json', 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(danmu_cutted, indent=2, ensure_ascii=False))

# 提取关键词，并写入文件
danmu_keyword = []
for str in danmuArr:
    # textrank算法把词汇都过滤掉了，extract_tags更靠谱
    # topK 表示返回最大权重关键词的个数，None表示全部
    # withWeight表示是否返回权重，是的话返回(word,weight)的list
    # allowPOS仅包括指定词性的词，默认为空即不筛选
    # key_word = jieba.analyse.textrank(str, topK=10, withWeight=False, allowPOS=['ns','n','vn','v'], withFlag=False)
    key_word = jieba.analyse.extract_tags(str, withWeight=False, withFlag=False)
    danmu_keyword.append(key_word)

with open('./fenci/danmu_keyword.json', 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(danmu_keyword, indent=2, ensure_ascii=False))
