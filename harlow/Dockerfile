FROM golang:1.9
COPY . /go/src/local-kuaibiji/go-micro-services
WORKDIR /go/src/local-kuaibiji/go-micro-services
RUN go install -ldflags="-s -w" ./cmd/...
