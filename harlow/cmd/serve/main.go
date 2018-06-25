package main

import (
	"fmt"
	"os"
	"flag"
	"strings"
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
func runUsage(port int) error {

	usage()
	fmt.Println("tmpFunc ", port)
	return nil
}

// 根据参数返回对应的 函数
func runFromArgs() (func(port int) error) {
	var run func(port int) error

	//解析命令参数
	arg := strings.ToLower(os.Args[1])

	if arg == "all" {
		run = runAll
	} else if arg == "code" {
		run = runCode
	} else {
		run = runUsage
	}

	return run
}

// 程序入口
func main() {

	// setting
	var (
		// 声明了一个整数 flag，解析结果保存在 *int 指针 port 里
		port = flag.Int("port", 5001, "The server port")
	)

	// 解析命令行参数写入注册的 flag 里
	flag.Parse()

	// 参数
	if len(os.Args) < 2 {
		usage()
		os.Exit(1)
	}
	logArgs()

	// run
	run := runFromArgs()

	run(*port)
}
