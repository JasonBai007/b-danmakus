# coding=utf-8

from bilibili_api import video
import json
from bvid import BVID

# 获取视频信息并打印
info = video.get_video_info(bvid=BVID)
print('获取视频信息BVID：'+ info['bvid'])
print('获取视频信息TITLE：'+ info['title'])

# 为视频信息生成文件
filename0 = './danmu/info.json'
with open(filename0, 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(info, indent=2, ensure_ascii=False))

# 假设这里获取 p1 的最新弹幕信息，需要取出 page_id，即每 p 都有自己的编号（其实就是视频选集）
page_id = info["pages"][0]["cid"]

# 然后开始获取弹幕
print('开始获取字幕数据...')
danmakus = video.get_danmaku(bvid=BVID, page_id=page_id)

# 写入文件
print('开始写入文件...')
filename = './danmu/danmu_all.txt'
with open(filename, 'w', encoding='utf-8') as file_object:
    # 将List类型的数据转成字符串类型，转之前需要把里面的数值型的转成字符串型的
    file_object.write('\n'.join('%s' %id for id in danmakus))

# 构建弹幕List
danTextList = []
for dm in danmakus:
    # 每条弹幕包括时间、内容等信息，是个Class
    danTextList.append(dm.text)

# 生成弹幕文本文件
filename2 = './danmu/danmu_text.txt'
with open(filename2, 'w', encoding='utf-8') as file_object:
    file_object.write('\n'.join(danTextList))

# 生成弹幕JSON文件
filename3 = './danmu/danmu_text.json'
with open(filename3, 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(danTextList, indent=2, ensure_ascii=False))

print('写入文件完毕')