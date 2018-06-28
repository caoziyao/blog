package main

import (
	"fmt"
	"sync"

	"kuaibiji/registry"
)

func waitOherCoro() {
	select {}

	fmt.Println("coroutine over")
}

// run goroutine
func wgRun(coroFunc func(port int, registry *registry.Client) error, port int, registry *registry.Client, wg *sync.WaitGroup) error {
	coroFunc(port, registry)
	wg.Done()

	return nil
}

func runAll(port int, registry *registry.Client, jaegeraddr string) error {
	fmt.Println("runAll ", port)

	//go runCode(8001, registry, jaegeraddr)
	go runNotebook(8004, registry, jaegeraddr)

	return runFrontend(5000, registry, jaegeraddr)
}

func backRun() {
	//var wg sync.WaitGroup

	// 因为有两个动作，所以增加2个计数
	//wg.Add(1)

	// 表达式go f(x, y, z)会启动一个新的 goroutine 运行函数f(x, y, z)
	//go func() {
	//	runCode(port)
	//	wg.Done()
	//}()

	//go wgRun(runCode, port, registry,  &wg)
	//go wgRun(runFrontend, port, registry,  &wg)

	// 等待，直到计数为0
	//wg.Wait()
}


