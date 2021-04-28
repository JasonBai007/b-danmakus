# coding=utf-8
# 获取视频信息和字幕数据

import json
from bilibili_api import video
from bvid import BVID, EPISODE

# 获取视频信息并打印
info = video.get_video_info(bvid=BVID)
print('视频BVID：'+ info['bvid'])
print('视频TITLE：'+ info['title'])

# 为视频信息生成文件
filename0 = './danmu/info.json'
with open(filename0, 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(info, indent=2, ensure_ascii=False))

# 视频选集：默认第1集
page_id = info["pages"][EPISODE]["cid"]

# 然后开始获取弹幕
print('开始获取字幕数据...')
danmakus = video.get_danmaku(bvid=BVID, page_id=page_id)

# 写入文件
print('开始写入文件...')
filename = './danmu/danmu_raw.txt'
with open(filename, 'w', encoding='utf-8') as file_object:
    # 将List类型的数据转成字符串类型，转之前需要把里面的数值型的转成字符串型的
    file_object.write('\n'.join('%s' %id for id in danmakus))

# 构建弹幕List
danTextList = []
for dm in danmakus:
    # 每条弹幕包括时间、内容等信息，是个Class
    danTextList.append(dm.text)

# 生成弹幕JSON文件
filename3 = './danmu/danmu_text.json'
with open(filename3, 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(danTextList, indent=2, ensure_ascii=False))

print('写入文件完毕')