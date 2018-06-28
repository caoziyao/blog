package main

import (
	"fmt"
	"kuaibiji/registry"
	"kuaibiji/services/frontend"

	"kuaibiji/tracing"
	"kuaibiji/dialer"

	//"kuaibiji/services/notebook"

	notebook "kuaibiji/services/notebook/proto"
)

func runFrontend(port int, consul *registry.Client, jaegeraddr string) error {
	fmt.Println("runFrontend ", port)

	tracer, err := tracing.Init("frontend", jaegeraddr)
	if err != nil {
		return fmt.Errorf("tracing init error: %v", err)
	}

	// dial search srv
	sc, err := dialer.Dial(
		notebookSrvName,
		dialer.WithTracer(tracer),
		dialer.WithBalancer(consul.Client),
	)
	if err != nil {
		return fmt.Errorf("dialer error: %v", err)
	}



	srv := frontend.NewServer(
		notebook.NewNotebookClient(sc),
		tracer,
	)
	return srv.Run(port)
}
