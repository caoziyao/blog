FROM python:3.7

COPY micro_service /data/www/micro_service

WORKDIR /data/www/micro_service

RUN python3 -m pip install -r requirements.txt


CMD ["python3", "main.py"]