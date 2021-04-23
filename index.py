# 导入模块
from bilibili_api import video
import json
from bvid import BVID

# 获取视频信息并打印
info = video.get_video_info(bvid=BVID)
print(info)
filename0 = './res/info.json'
with open(filename0, 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(info, indent=2, ensure_ascii=False))

# 假设这里获取 p1 的最新弹幕信息，需要取出 page_id，即每 p 都有自己的编号（我也不知道是啥意思）
page_id = info["pages"][0]["cid"]

# 然后开始获取弹幕
danmakus = video.get_danmaku(bvid=BVID, page_id=page_id)

# 写入文件
filename = './res/res_all.txt'
with open(filename, 'w', encoding='utf-8') as file_object:
    # 将List类型的数据转成字符串类型，转之前需要把里面的数值型的转成字符串型的
    file_object.write('\n'.join('%s' %id for id in danmakus))

# 构建弹幕List
danTextList = []
for dm in danmakus:
    # 每条弹幕包括时间、内容等信息，是个Class
    danTextList.append(dm.text)

# 生成弹幕文本文件
filename2 = './res/res_text.txt'
with open(filename2, 'w', encoding='utf-8') as file_object:
    file_object.write('\n'.join(danTextList))

# 生成弹幕JSON文件
filename3 = './res/res_text.json'
with open(filename3, 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(danTextList, indent=2, ensure_ascii=False))