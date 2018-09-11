package main

import (
	"context"
	"github.com/micro/go-micro"
	proto "kuaibiji/services/proto"
	"fmt"
)


// go run client.go
// docker:
// docker exec kuaibiji_api_1 go run client/client.go
func main() {
	// Create a new service. Optionally include some options here.
	service := micro.NewService(micro.Name("greeter.client"))
	service.Init()

	// Create new greeter client
	greeter := proto.NewGreeterClient("greeter", service.Client())

	// Call the greeter
	rsp, err := greeter.Hello(context.TODO(), &proto.HelloRequest{Name: "i am client!"})
	if err != nil {
		fmt.Println(err)
	}

	// Print response
	fmt.Println(rsp.Greeting)
}
