# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/7 
@desc:
"""
import requests
import json

def main():
    url = "http://localhost:8081/rpc"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
	"service": "go.micro.srv.pyapp",
        "method": "Say.Hello",
        "request": {"name": "sssssss"},
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers)

    print('response', response.content)
    # r = requests.post(
    #     url, data=json.dumps(payload), headers=headers)

    return response
    # response.


if __name__ == "__main__":
    main()