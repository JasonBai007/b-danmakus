# coding=utf-8

import json
from bvid import BVID
from bilibili_api.video import get_comments_g

# 此处会立即返回一个生成器
comments_generator = get_comments_g(BVID, order='like')

# 获取原始评论数据
comments = []
for comment in comments_generator:
    # 将评论项目加入列表，也就是普通的所有评论爬虫
    comments.append(comment)

# 构建精简版列表
comments_lite = []
for c in comments:
    if c['replies'] is not None:
        comments_lite.append({
            'content':c['content']['message'],
            'like':c['like']
        })
        for r in c['replies']:
            comments_lite.append({
                'content':r['content']['message'],
                'like':r['like']
            })
    else:
        comments_lite.append({
            'content':c['content']['message'],
            'like':c['like']
        })

# 对精简版列表进行排序
def likeSort(obj):
    return obj['like']

comments_lite.sort(key=likeSort, reverse=True)

# 写入文件
print('已获取' + str(len(comments_lite)) + '条评论')
with open('./comments/comments_raw.json', 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(comments, indent=2, ensure_ascii=False))


with open('./comments/comments_lite.json', 'w', encoding='utf-8') as file_object:
    file_object.write(json.dumps(comments_lite, indent=2, ensure_ascii=False))

print('评论写入文件成功')

