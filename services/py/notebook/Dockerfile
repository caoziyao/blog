FROM python:3.7
COPY services/python_app/pip.conf /root/.pip/pip.conf
COPY services/python_app/requirements.txt /code/requirements.txt
RUN python3 -m pip install -r /code/requirements.txt

WORKDIR /code
#COPY micro_service /data/www/micro_service

CMD ["python3", "main.py"]
