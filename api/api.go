package main

import (
	"context"
	hello "go-micro-docker-demo/services/proto"
	"github.com/micro/go-micro"
	api "github.com/micro/micro/api/proto"

	"log"
	"github.com/micro/go-micro/errors"
	"strings"
	"encoding/json"
)

type Greetera struct {
	Client hello.GreeterClient
}

// Greeter的handler实现
// docker exec go-micro-docker-demo_api_1 go run api/api.go
// curl -H 'Content-Type: application/json' -d '{"name": "john"}' http://localhost:8080/api/gua/height\?name\=121
// curl -H 'Content-Type: application/json' -d '{"name": "john"}' http://localhost:8080/api/greetera/helloa\?name\=121
func (s *Greetera) Helloa(ctx context.Context, req *api.Request, rsp *api.Response) error {
	log.Print("Received Say.Hello API request")

	name, ok := req.Get["name"]
	if !ok || len(name.Values) == 0 {
		return errors.BadRequest("====go.micro.api.greeter", "Name cannot be blank")
	}

	response, err := s.Client.Hello(ctx, &hello.HelloRequest{
		Name: strings.Join(name.Values, " "),
	})

	if err != nil {
		return err
	}

	rsp.StatusCode = 200
	b, _ := json.Marshal(map[string]string{
		"message": response.Greeting,
	})
	rsp.Body = string(b)

	return nil
}

type Gua struct {
}

func (s *Gua) Height(ctx context.Context, req *api.Request, rsp *api.Response) error {
	log.Print("Received Say.Hello API request")

	name, ok := req.Get["name"]
	if !ok || len(name.Values) == 0 {
		return errors.BadRequest("====gua", "Name cannot be blank")
	}

	rsp.StatusCode = 200
	b, _ := json.Marshal(map[string]string{
		"message": "gua 169m",
	})
	rsp.Body = string(b)

	return nil
}


func main()  {
	service := micro.NewService(
		// 默认 go.micro.api.xxx
		micro.Name("go.micro.api.api"),
	)

	// parse command line flags
	service.Init()

	service.Server().Handle(
		service.Server().NewHandler(
			// &Greetera{Client: hello.NewGreeterClient("greeter", service.Client())},
			&Greetera{Client: hello.NewGreeterClient("srv-greeter", service.Client())},
			//&Greeter{Client: hello.NewGreeterClient("go.micro.srv.greeter", service.Client())},
		),
	)
	//hello.RegisterGreeterHandler(service.Server(), )

	//service.Server().Handle(
	//	service.Server().NewHandler(
	//		&Gua{},
	//		//&Greeter{Client: hello.NewGreeterClient("go.micro.srv.greeter", service.Client())},
	//	),
	//)

	if err := service.Run(); err != nil {
		log.Fatal(err)
	}

	// handler需要注册到某个服务
	//proto.RegisterGreeterServer(service.Server(), new(Greeter))
	//hello.RegisterGreeterHandler(service.Server(), new(Greeter))

}
