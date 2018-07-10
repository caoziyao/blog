package common

import (
	"kuaibiji/services/proto"
	"github.com/opentracing/opentracing-go"
)

type Server struct {
	notebookClient proto.NotebookClient
	userClient     proto.UserClient
	tracer         opentracing.Tracer
}

// new server
func NewServer(nc proto.NotebookClient, uc proto.UserClient, tr opentracing.Tracer) *Server {

	return &Server{
		notebookClient: nc,
		userClient:     uc,
		tracer:         tr,
	}
}

// return client
func (s *Server) GetNotebookClient() proto.NotebookClient {
	return s.notebookClient
}

func (s *Server) GetUserClient() proto.UserClient {
	return s.userClient
}
