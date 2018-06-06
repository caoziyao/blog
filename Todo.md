
- 使用用脚本执行所有部署流程（包括开发环境）
- 通过单一命令运行部署


使用sanic异步框架，简单，轻量，高效。
使用uvloop为核心引擎，使sanic在很多情况下单机并发甚至不亚于Golang。
使用asyncpg为数据库驱动，进行数据库连接，执行sql语句执行。
使用aiohttp为Client，对其他微服务进行访问。
使用peewee为ORM，但是只是用来做模型设计和migration。
使用opentracing为分布式追踪系统。
使用unittest做单元测试，并且使用mock来避免访问其他微服务。
使用swagger做API标准，能自动生成API文档。


用Flask开发一个RESTful API 服务
实践测试驱动开发(TDD)
在本地用Docker和Docker Compose配置和运行服务
将代码挂载到一个容器中去
在容器中运行单元测试和集成测试
不同容器的服务间的交互
在Docker容器中运行Python和Flask应用
安装Flask、Nginx和Gunicorn

flask-microservices-main - Docker Compose 文件、Nginx、Admin 脚本
flask-microservices-users - 管理用户和认证的Flask 应用
flask-microservices-client - 客户端，React 应用
flask-microservices-swagger - Swagger API 文档

todo
微服务：

- [x] 目录树
- 新增文件夹/文件
- 拖动
- 新建笔记
- tree 状态存储，tree 遍历，结构体改变
- [x] 自动保存
- [x] markdown 编辑
- heightlight
- 多屏查看
- 代码编辑器
- 运行 python
- 搜索功能，全局搜，单文件搜

- 搜索入口
- 爬虫
- 网盘搜索
- 代理功能
- 优惠信息
- 新资讯
- mm图片展示
- 视频展示
- 私密空间
- [x] 书架功能，手动收藏
- 收藏购买测评
- 游戏链接

- 随笔

- 运动功能，饮食记录
- 在线视频播放，只需链接即可，能播放 bilibili
- you-get
- 在线音乐播放
- 在线看书功能
- bilibili 爬虫
- 第三方 qq 音乐

- [x] 发送 email

- 登录注册
- 访客登录
- 随机登录
- 用户权限
- 邮箱验证
- 随机头像
- qq/微信登录，了解 oauth 流程
- 手机短信登录
- https

- 兼容手机访问
- 统计访问数量

- mysql
- mongodb
- redis
-----------------
高并发实验改进
思路：
本地模拟高并发网站架构，2个即可
- 两个文件夹，2份代码，2个端口。代表在不同地方的 2 台服务器
- 本地建 2 个数据库。一个主，一个从，读写分离
- 第三个文件夹，存放静态资源。代表资源服务器


- 把代码丢到一个地方（进阶： 版本控制）
- 使用用脚本执行所有部署流程（包括开发环境）
- 通过单一命令运行部署
- 把可变信息注入配置文件

- 自动化
- 实时监控
- log 日志

- 反向代理
- CDN

- 服务器系统
- 本地缓冲

- 数据库系统
- [x] 存数据库
- 数据库备份
- 异步数据库
- 读写分离，主从复制

- 缓存系统
- [x] redis 缓存
- 集群
- 异步redis

- 文件系统
- 文件上传

- nosql
- 搜索引擎

- 消息队列服务器
