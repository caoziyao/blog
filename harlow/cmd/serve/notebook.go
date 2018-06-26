package main

import (
	"fmt"
	"kuaibiji/registry"
	"kuaibiji/services/notebook"
)

func runNotebook(port int, consul *registry.Client) error {
	fmt.Println("runNotebook ", port)

	srv := notebook.NewServer()
	return srv.Run(port)
}

