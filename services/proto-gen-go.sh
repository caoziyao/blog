#!/usr/bin/env bash

# go-micro 插件，而不是 gRPC 插件
python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. proto/*.proto

protoc --go_out=plugins=micro:. proto/greeter.proto
