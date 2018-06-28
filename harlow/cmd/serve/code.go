package main

import (
	"fmt"
	"kuaibiji/registry"
)

func runCode(port int, consul *registry.Client, jaegeraddr string) error {
	fmt.Println("runCode ", port)

	//fmt.Println("start sleeping...")
	//time.Sleep(6 * time.Second)
	//fmt.Println("end sleep.")

	return nil
}
