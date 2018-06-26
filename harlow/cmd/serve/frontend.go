package main

import (
	"fmt"
	"kuaibiji/registry"
	"kuaibiji/services/frontend"
)

func runFrontend(port int, consul *registry.Client) error {
	fmt.Println("runFrontend ", port)

	srv := frontend.NewServer()
	return srv.Run(port)
}
