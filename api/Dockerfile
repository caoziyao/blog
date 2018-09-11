FROM golang:1.10
#FROM microhq/micro

#RUN go get -u github.com/micro/micro
#RUN go get -u github.com/golang/protobuf/{proto,protoc-gen-go}
COPY . /go/src/kuaibiji
WORKDIR /go/src/kuaibiji


CMD ["go", "run", "api/api.go"]
#CMD ["go", "run", "./services/go/srv-greeter/main.go"]

