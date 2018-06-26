# .PHONY 目标：避免和同名文件冲突，改善性能。
.PHONY: proto data run

proto:
		for f in services/**/proto/*.proto; do \
			protoc --go_out=plugins=grpc:. $$f; \
			echo compiled: $$f; \
		done

run:
		docker-compose build
		docker-compose up --remove-orphans
