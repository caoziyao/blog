# .PHONY 目标：避免和同名文件冲突，改善性能。
.PHONY: proto data run

# python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. ./notebook.proto
proto:
		for f in proto/*.proto; do \
			python3 -m grpc_tools.protoc -I./ --python_out=. --grpc_python_out=. $$f; \
			echo compiled: $$f; \
		done

run:
		docker-compose build
		docker-compose up --remove-orphans
