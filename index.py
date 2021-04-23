# 导入模块
from bilibili_api import video
import json

# B站视频编号（示例）
# 在每个视频URL里面（如下所示）：
# https://www.bilibili.com/video/BV1g5411a7vC
BVID = "BV1zz4y117Ly"

# 获取视频信息
info = video.get_video_info(bvid=BVID)
# 打印视频信息
print(info)

# 假设这里获取 p1 的最新弹幕信息，需要取出 page_id，即每 p 都有自己的编号
page_id = info["pages"][0]["cid"]

# 然后开始获取弹幕
danmakus = video.get_danmaku(bvid=BVID, page_id=page_id)

# 写入文件
filename = 'res_all.txt'
with open(filename, 'w', encoding='utf-8') as file_object:
    # 将List类型的数据转成字符串类型，转之前需要把里面的数值型的转成字符串型的
    file_object.write('\n'.join('%s' %id for id in danmakus))

# 构建弹幕List
danTextList = []
for dm in danmakus:
    # print(str(dm))
    danTextList.append(dm.text)

# 生成弹幕文本文件
filename2 = 'res_text.txt'
with open(filename2, 'w', encoding='utf-8') as file_object:
    file_object.write('\n'.join(danTextList))

# 生成弹幕JSON文件
filename3 = 'res_text.json'
with open(filename3, 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(danTextList, indent=2, ensure_ascii=False))