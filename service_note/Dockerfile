############################################################
# 创建Python WSGI应用容器的Dockerfile
# 基于Ubuntu
############################################################

# 设置Ubuntu为打底镜像
FROM ubuntu:latest



# 添加软件资源库的URL
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

# 更新资源列表
RUN apt-get update

RUN apt-get install -y tar git curl nano wget dialog net-tools build-essential
RUN apt-get install -y python3 python3-pip

RUN python3 -m pip install requirements.txt



COPY . /data/www/services/serverice_code
WORKDIR /data/www/services/serverice_code



# RUN  python3 /root/go/src/kuaibiji/services/notebook/greeter_server.py
# CMD ["python3", "/root/go/src/kuaibiji/services/notebook/greeter_server.py" , "-g", "daemon off;"]

# 要运行的默认命令
# 该命令在新容器创建时开始执行
## 比如启动CherryPy来运行服务
#RUN go install -ldflags="-s -w" ./cmd/...
#
#ENTRYPOINT ["/root/go/bin/serve"]
