package main

//import (
//	"time"
//	"fmt"
//)
//
//func main()  {
//	print("aaaaaaaaaa")
//
//	fmt.Println("start sleeping...")
//	time.Sleep(time.Second * 1000)
//	fmt.Println("end sleep.")
//}
//
import (
	"fmt"
	"os"
	"flag"
	"kuaibiji/registry"
	"kuaibiji/cmd/serve"
)


// 程序入口
func main() {

	// setting
	var (
		port       = flag.Int("port", 5000, "The server port")
		jaegeraddr = flag.String("jaeger_addr", "0.0.0.0:6831", "Jaeger address")
		consuladdr = flag.String("consul_addr", "consul:8500", "Consul address")

		//// 声明了一个整数 flag，解析结果保存在 *int 指针 port 里
		//port = flag.Int("port", 5000, "The server port")
		////jaegeraddr = flag.String("jaeger_addr", "jaeger:6831", "Jaeger address")
		//jaegeraddr = flag.String("jaeger_addr", "0.0.0.0:6831", "Jaeger address")
		//// Service Discovery
		//consuladdr = flag.String("consul_addr", "0.0.0.0:8500", "Consul address")
		////consuladdr = flag.String("consul_addr", "consul:8500", "Consul address")
	)

	// 解析命令行参数写入注册的 flag 里
	flag.Parse()

	run := serve.RunAll

	consul, err := registry.NewClient(*consuladdr)
	if err != nil {
		fmt.Fprintf(os.Stderr, "%v\n", err)
		os.Exit(1)
	}


	if err := run(*port, consul, *jaegeraddr); err != nil {
		fmt.Fprintf(os.Stderr, "%v\n", err)
		os.Exit(1)
	}
}

