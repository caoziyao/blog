package notebook

import (
	"fmt"
	"net"
	"log"
	"google.golang.org/grpc"
	"strconv"

	pb "kuaibiji/services/notebook/proto"
	"golang.org/x/net/context"
)

// 定义服务端实现约定的接口
type Server struct {
}

// new server
func NewServer() *Server {
	s := &Server{

	}
	return s
}

// 实现 interface
func (s *Server) GetNotebookInfo(ctx context.Context, req *pb.NotebookRequest) (resp *pb.NotebookResponse, err error) {
	name := req.Name

	// 模拟在数据库中查找用户信息
	// ...
	if name == "wuYin" {
		resp = &pb.NotebookResponse{
			Id:    233,
			Name:  name,
			Age:   20,
			Title: []string{"Gopher", "PHPer"}, // repeated 字段是 slice 类型
		}
	}
	err = nil
	return resp, nil
}

// Run the server
func (s *Server) Run(port int) error {

	host := ":" + strconv.Itoa(port)
	l, err := net.Listen("tcp", host)
	if err != nil {
		log.Fatalf("listen error: %v\n", err)
	}
	fmt.Printf("listen %s\n", host)
	srv := grpc.NewServer()

	// 将 Server 注册到 gRPC
	// 注意第二个参数 Server 是接口类型的变量
	// 需要取地址传参
	pb.RegisterNotebookServiceServer(srv, s)
	srv.Serve(l)

	return err
}
