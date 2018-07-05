package main

import (
	"fmt"
	"os"
	"flag"
	"strings"

	"kuaibiji/registry"
)

// 用法
func usage() {
	fmt.Println(os.Stderr, "USAGE\n")
}

// 打印 args
func logArgs() {

	fmt.Println("===logArgs===")

	i := 0
	l := len(os.Args)

	for i = 0; i < l; i++ {
		fmt.Println(os.Args[i])
	}
}

// 打印 setting
func logSetting() {

}

// tmp
func runUsage(port int, consul *registry.Client, jaegeraddr string) error {

	usage()
	fmt.Println("tmpFunc ", port)
	return nil
}

// 根据参数返回对应的 函数
func runFromArgs() (func(port int, consul *registry.Client, jaegeraddr string) error) {
	var run func(port int, consul *registry.Client, jaegeraddr string) error

	//解析命令参数
	arg := strings.ToLower(os.Args[1])

	if arg == "all" {
		run = runAll
	} else if arg == "code" {
		run = runCode
	} else {
		//run = runUsage
		run = runAll
	}

	return run
}

// 程序入口
func main() {

	// setting
	var (
		// 声明了一个整数 flag，解析结果保存在 *int 指针 port 里
		port = flag.Int("port", 5000, "The server port")
		//jaegeraddr = flag.String("jaeger_addr", "jaeger:6831", "Jaeger address")
		jaegeraddr = flag.String("jaeger_addr", "0.0.0.0:6831", "Jaeger address")
		// Service Discovery
		consuladdr = flag.String("consul_addr", "0.0.0.0:8500", "Consul address")
		//consuladdr = flag.String("consul_addr", "app_net:8500", "Consul address")
		//consuladdr = flag.String("consul_addr", "consul:8500", "Consul address")
	)

	// 解析命令行参数写入注册的 flag 里
	flag.Parse()

	//// 参数
	//if len(os.Args) < 2 {
	//	usage()
	//	os.Exit(1)
	//}
	//logArgs()
	run := runAll

	consul, err := registry.NewClient(*consuladdr)
	if err != nil {
		fmt.Fprintf(os.Stderr, "%v\n", err)
		os.Exit(1)
	}

	// run
	//run := runFromArgs()

	if err := run(*port, consul, *jaegeraddr); err != nil {
		fmt.Fprintf(os.Stderr, "%v\n", err)
		os.Exit(1)
	}
}
