
install:
		cp /Users/Shared/dbj/api.kuaibi/micro_service/proto/*.proto /Users/Shared/go/src/kuaibiji/services/proto

		protoc --go_out=plugins=grpc:. proto/notebook.proto
		protoc --go_out=plugins=grpc:. proto/user.proto
		protoc --go_out=plugins=grpc:. proto/weixin.proto
