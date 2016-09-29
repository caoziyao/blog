# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import json

# import time
# import json



# db = SQLAlchemy(app)

# def init_db():
#     # 先 drop_all 删除所有数据库中的表
#     # 再 create_all 创建所有的表
#     db.drop_all()
#     db.create_all()
#     print('rebuild database')


# if __name__ == '__main__':
#     init_db()
#     # """
#     # select * from users where id=1
#     #
#     # update users set password='pwd' where id=1
#     #
#     # SELECT
#     #     todos.id AS todos_id,
#     #     todos.task AS todos_task,
#     #     todos.created_time AS todos_created_time,
#     #     todos.user_id AS todos_user_id
#     # FROM
#     #     todos
#     # WHERE
#     #     todos.user_id = :user_id_1
#     # """
#     # u = User.query.get(1)
#     # # u.password = 'pwd'
#     # # u.save()
#     # print('sql', Todo.query.filter_by(user_id=u.id))
#     # ts = Todo.query.filter_by(user_id=u.id).all()
#     # print('todos', ts)