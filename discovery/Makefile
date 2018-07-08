# .PHONY 目标：避免和同名文件冲突，改善性能。
.PHONY: proto data run

SRC_DIR = .
DST_DIR = .

proto:
		# protoc -I=$SRC_DIR --go_out=$DST_DIR $SRC_DIR/addressbook.proto
		for f in services/**/proto/*.proto; do \
			protoc --go_out=plugins=grpc:. $$f; \
			echo compiled: $$f; \
		done

install:
		#rm /Users/Shared/go/bin/serve
		#go install -ldflags="-s -w" ./cmd/...
		go install -ldflags="-s -w" .
