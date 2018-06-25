package main

import (
	"fmt"
	"sync"
)

func waitOherCoro() {
	select{
	}

	fmt.Println("coroutine over")
}

// run goroutine
func wgRun(coroFunc func(port int) error, port int, wg *sync.WaitGroup) error {
	coroFunc(port)
	wg.Done()

	return nil
}

func runAll(port int) error {
	fmt.Println("runAll ", port)

	var wg sync.WaitGroup

	// 因为有两个动作，所以增加2个计数
	wg.Add(1)

	// 表达式go f(x, y, z)会启动一个新的 goroutine 运行函数f(x, y, z)
	//go func() {
	//	runCode(port)
	//	wg.Done()
	//}()

	go wgRun(runCode, port, &wg)


	// 等待，直到计数为0
	wg.Wait()

	return nil
}