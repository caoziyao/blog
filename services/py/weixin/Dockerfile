FROM python:3.7
COPY pip.conf /root/.pip/pip.conf
COPY requirements.txt /data/requirements.txt
RUN python3 -m pip install -r /data/requirements.txt

WORKDIR /code
#COPY micro_service /data/www/micro_service

#CMD ["python3", "main.py", "weixin"]
CMD ["python3", "weixin/app.py"]
