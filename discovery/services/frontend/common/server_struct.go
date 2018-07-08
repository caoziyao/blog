package common

import (
	"kuaibiji/services/proto"
	"github.com/opentracing/opentracing-go"
)

type Server struct {
	notebookClient proto.NotebookClient
	userClient proto.UserClient
	tracer        opentracing.Tracer
}


// new server
func NewServer(nc proto.NotebookClient, uc proto.UserClient, tr opentracing.Tracer) *Server {

	//srv := common.NewServer(nc, uc, tr)
	//return srv
	return &Server{
		notebookClient:  nc,
		userClient:  	uc,
		tracer:        tr,
	}
}

func (s *Server)GetNotebookClient()  proto.NotebookClient{
	return s.notebookClient
}
