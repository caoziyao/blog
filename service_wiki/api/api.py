# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/6/6 
@desc:
"""
from flask import Flask, request, jsonify
from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__)
CONFIG = {'AMQP_URI': "pyamqp://guest:guest@localhost"}


@app.route('/', methods=['GET'])
def root():
    return "Hello! I'm a sale management microservice system."


@app.route('/sale/sell', methods=['GET'])
def sell():
    with ClusterRpcProxy(CONFIG) as rpc:
        # .mail.send( email,"tesss!",  "Ttttt: %s" % result)
        # result = rpc.sale.sell.async(product_id)
        result = rpc.mail.send('aaa@q.com', "tesss!", "Ttttt:sdssa")
        return jsonify({'task': "ok"}), 200


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
