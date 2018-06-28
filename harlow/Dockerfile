#FROM golang:1.9
#COPY . /go/src/kuaibiji
#WORKDIR /go/src/kuaibiji
#RUN go install -ldflags="-s -w" ./cmd/...


############################################################
# 创建Python WSGI应用容器的Dockerfile
# 基于Ubuntu
############################################################

# 设置Ubuntu为打底镜像
FROM ubuntu:latest

# 文件作者/维护者
MAINTAINER Maintaner Name

# 添加软件资源库的URL
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

# 更新资源列表
RUN apt-get update

RUN apt-get install -y golang-go
RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get install -y python3 python3-pip

RUN python3 -m pip install grpcio
RUN python3 -m pip install grpcio-tools


COPY . /root/go/src/kuaibiji
WORKDIR /root/go/src/kuaibiji

RUN ls /root/go/src/kuaibiji
RUN ls /root/go/src/kuaibiji/services
RUN ls /root/go/src/kuaibiji/services/notebook
RUN ls /root/go/src/kuaibiji/services/notebook/greeter_server.py
# RUN  python3 /root/go/src/kuaibiji/services/notebook/greeter_server.py
# CMD ["python3", "/root/go/src/kuaibiji/services/notebook/greeter_server.py" , "-g", "daemon off;"]

# 要运行的默认命令
# 该命令在新容器创建时开始执行
# 比如启动CherryPy来运行服务
RUN go install -ldflags="-s -w" ./cmd/...

ENTRYPOINT ["/root/go/bin/serve"]
