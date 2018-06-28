package main

import (
	"fmt"
	"kuaibiji/registry"

	"os/exec"
	"os"
	"strings"
)

const notebookSrvName = "srv-notebook"


func runNotebook(port int, consul *registry.Client, jaegeraddr string) error {
	fmt.Println("runNotebook ", port)

	//tracer, err := tracing.Init("notebook", jaegeraddr)
	//if err != nil {
	//	return fmt.Errorf("tracing init error: %v", err)
	//}

	// service registry
	id, err := consul.Register(notebookSrvName, port)
	if err != nil {
		return fmt.Errorf("failed to register service: %v", err)
	}
	defer consul.Deregister(id)

	//var cmd *exec.Cmd
	// 执行单个shell命令时, 直接运行即可
	var  whoami []byte
	var cmd *exec.Cmd
	cmd = exec.Command("python3", "/root/go/src/kuaibiji/services/notebook/greeter_server.py")
	if whoami, err = cmd.Output(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	// 默认输出有一个换行
	fmt.Println(string(whoami))
	// 指定参数后过滤换行符
	fmt.Println(strings.Trim(string(whoami), "\n"))

	fmt.Println("====")
	//if whoami, err = cmd.Output(); err != nil {
	//	fmt.Println(err)
	//	os.Exit(1)
	//}
	//fmt.Println(string(whoami))

	//srv := notebook.NewServer(tracer)
	//return srv.Run(port)
	return nil

}
