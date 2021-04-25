# encoding=utf-8
import jieba
import json

danmuArr = []
with open('./danmu/danmu_text.json', encoding='UTF-8') as json_file:
	 danmuArr = json.load(json_file)

danmu_cutted = []
for str in danmuArr:
    seg_list = jieba.cut(str)
    danmu_cutted.append(list(seg_list))

with open('./fenci/danmu_cut.json', 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(danmu_cutted, indent=2, ensure_ascii=False))