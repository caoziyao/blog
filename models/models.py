"""
用户
用户ID、姓名、email、github、密码

文章
文章ID、title、时间、用户ID、内容

标签
标签ID、标签name

关联表Article_has_Tags
ID、文章ID、标签ID

评论
评论ID、用户ID、文章ID、内容


# 定义一个关系
# foreign_keys 有时候可以省略, 比如现在...
# 自动关联 不用手动查询就有数据
# 通过topic查找comment：c = t.comments
# 也可以通过comment查找topic： t = c.topic
comments = db.relationship('Comment', backref='topic')
user = db.relationship('User', backref='topic')
"""