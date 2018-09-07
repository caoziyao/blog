# import sys
# import os
# sys.path.append(os.path.join(os.path.abspath(__file__), '..', '..'))
#
# from werkzeug.wrappers import Request, Response
# from werkzeug.serving import run_simple
# import requests
# # import sidecar
#
# print(os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..')))
# from python_app import sidecar
# from jsonrpc import JSONRPCResponseManager, dispatcher
#
# import uuid
#
#
# service = {
#     "name": "go.micro.srv.pyapp",
#     "nodes": [{
#         "id": "go.micro.srv.greeter-" + str(uuid.uuid4()),
#         "address": "srv-pyapp",
#         "port": 4000,
#     }],
# }
#
# @Request.application
# def application(request):
#     print('s,')
#     dispatcher["Say.Hello"] = lambda s: "greeting=" + s["name"] + "!"
#     response = JSONRPCResponseManager.handle(request.data, dispatcher)
#     s = Response(response.json, mimetype='application/json')
#     return s
#
# if __name__ == '__main__':
#     sidecar.register(service)
#     run_simple('0.0.0.0', 4000, application)
#     sidecar.deregister(service)

