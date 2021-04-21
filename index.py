# 导入模块
from bilibili_api import video

# B站视频编号（示例）
BVID = "BV1g5411a7vC"

# 获取视频信息
info = video.get_video_info(bvid=BVID)
# 打印视频信息
print(info)

# 假设这里获取 p1 的最新弹幕信息，需要取出 page_id，即每 p 都有自己的编号
page_id = info["pages"][0]["cid"]

# 然后开始获取弹幕
danmakus = video.get_danmaku(bvid=BVID, page_id=page_id)

# 打印弹幕
for dm in danmakus:
    print(str(dm))

# 写入文件
filename = 'result.txt'
with open(filename, 'w', encoding='utf-8') as file_object:
    file_object.write('\n'.join('%s' %id for id in danmakus))