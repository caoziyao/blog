FROM golang:1.9
COPY . /go/src/kuaibiji
WORKDIR /go/src/kuaibiji
RUN go install -ldflags="-s -w" ./cmd/...
