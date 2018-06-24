# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/6/6 
@desc:
"""


from flask import Flask, jsonify

# 初始化app
app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

def main():
    setting = dict(
        port=5002,
        host='localhost',
    )
    app.run(**setting)

if __name__ == '__main__':
    main()