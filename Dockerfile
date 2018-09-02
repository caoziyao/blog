FROM golang:1.10
COPY . /go/src/kuaibiji
WORKDIR /go/src/kuaibiji
RUN go install -ldflags="-s -w" ./cmd/...


RUN which go
#RUN ls /usr/local/bin


#ENTRYPOINT ["/go/bin/serve"]
CMD ["/usr/local/go/bin/go", "run", "main.go"]

#RUN go run main.go