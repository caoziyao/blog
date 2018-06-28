package notebook

import (
	"fmt"
	"net"
	"log"
	"google.golang.org/grpc"
	"strconv"

	pb "kuaibiji/services/notebook/proto"
	"golang.org/x/net/context"
	"github.com/grpc-ecosystem/grpc-opentracing/go/otgrpc"

	opentracing "github.com/opentracing/opentracing-go"
)

// 定义服务端实现约定的接口
type Server struct {
	tracer     opentracing.Tracer
}

// new server
func NewServer(tr opentracing.Tracer) *Server {
	return &Server{
		tracer:     tr,
	}
}

// 实现 interface
func (s *Server) GetNotebookInfo(ctx context.Context, req *pb.NotebookRequest) (*pb.NotebookResponse, error) {
	name := req.Name
	log.Println("in GetNotebookInfo")
	// 模拟在数据库中查找用户信息
	// ...
	resp := pb.NotebookResponse{
		Id:    233,
		Name:  name,
		Age:   20,
		Title: []string{"Gopher", "PHPer"}, // repeated 字段是 slice 类型
	}

	return &resp, nil
}


// Run the server
func (s *Server) Run(port int) error {
	srv := grpc.NewServer(
		grpc.UnaryInterceptor(
			otgrpc.OpenTracingServerInterceptor(s.tracer),
		),
	)
	pb.RegisterNotebookServer(srv, s)

	host := ":" + strconv.Itoa(port)
	l, err := net.Listen("tcp", host)
	if err != nil {
		log.Fatalf("listen error: %v\n", err)
	}
	fmt.Printf("listen %s\n", host)


	// 将 Server 注册到 gRPC
	// 注意第二个参数 Server 是接口类型的变量
	// 需要取地址传参
	return srv.Serve(l)
}
