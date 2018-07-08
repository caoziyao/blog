package serve

import (
	"fmt"
	"kuaibiji/registry"
	"kuaibiji/services/frontend"

	"kuaibiji/tracing"
	"kuaibiji/dialer"

	//"kuaibiji/services/notebook"
	proto "kuaibiji/services/proto"
	//user "kuaibiji/services/proto/user"
	//user "kuaibiji/services/proto/user"
	//"github.com/hashicorp/consul/agent/consul"
	"google.golang.org/grpc"
	"github.com/opentracing/opentracing-go"

	"kuaibiji/services/frontend/common"
)

func clientNoteBook(consul *registry.Client, tracer opentracing.Tracer) *grpc.ClientConn{
	// dial search srv
	sc, err := dialer.Dial(
		notebookSrvName,
		dialer.WithTracer(tracer),
		dialer.WithBalancer(consul.Client),
	)
	if err != nil {
		fmt.Errorf("dialer error: %v", err)
	}

	return sc
}

func clientUser(consul *registry.Client, tracer opentracing.Tracer) *grpc.ClientConn{
	// dial search srv
	sc, err := dialer.Dial(
		userSrvName,
		dialer.WithTracer(tracer),
		dialer.WithBalancer(consul.Client),
	)
	if err != nil {
		fmt.Errorf("dialer error: %v", err)
	}

	return sc
}

func runFrontend(port int, consul *registry.Client, jaegeraddr string) error {
	fmt.Println("runFrontend ", port)

	tracer, err := tracing.Init("frontend", jaegeraddr)
	if err != nil {
		return fmt.Errorf("tracing init error: %v", err)
	}

	// dial search srv
	//sc, err := dialer.Dial(
	//	notebookSrvName,
	//	dialer.WithTracer(tracer),
	//	dialer.WithBalancer(consul.Client),
	//)
	//if err != nil {
	//	return fmt.Errorf("dialer error: %v", err)
	//}
	sc := clientNoteBook(consul, tracer)
	su := clientUser(consul, tracer)


	srv := common.NewServer(
		proto.NewNotebookClient(sc),
		proto.NewUserClient(su),
		tracer,
	)
	//return srv.Run(port)
	return frontend.Run(srv, port)
}
