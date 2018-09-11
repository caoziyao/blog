package main

import (
	"github.com/micro/go-micro"
	"context"
	proto "kuaibiji/services/proto"
	"fmt"
)

// 注册handler来处理请求
// func(ctx context.Context, req interface{}, rsp interface{}) error

type Greeter struct {
}

// Greeter的handler实现
func (g *Greeter) Hello(ctx context.Context, req *proto.HelloRequest, rsp *proto.HelloResponse) error {
	rsp.Greeting = "hello " + req.Name
	return nil
}

func main() {

	fmt.Println("hello server main")

	service := micro.NewService(
		micro.Name("srv-greeter"),
		micro.Version("latest"),

	)

	// Init will parse the command line flags.
	service.Init()

	// handler需要注册到某个服务
	//proto.RegisterGreeterServer(service.Server(), new(Greeter))
	proto.RegisterGreeterHandler(service.Server(), new(Greeter))

	// Run the server
	// 这会让服务监听一个随机端口，这个调用也会让服务将自身注册到注册器，当服务停止运行时，会在注册器注销自己
	if err := service.Run(); err != nil {
		fmt.Println(err)
	}
}


