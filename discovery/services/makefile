
install:
		cp /Users/Shared/dbj/api.kuaibi/micro_service/notebook/proto/*.proto /Users/Shared/go/src/kuaibiji/services/proto
		cp /Users/Shared/dbj/api.kuaibi/micro_service/user/proto/*.proto /Users/Shared/go/src/kuaibiji/services/proto
		
		protoc --go_out=plugins=grpc:. proto/notebook.proto
		protoc --go_out=plugins=grpc:. proto/user.proto
