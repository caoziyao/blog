package serve

import (
	"fmt"
	"kuaibiji/registry"
)

const weixinSrvName = "srv-weixin"

func runWeixin(port int, consul *registry.Client, jaegeraddr string) error {
	fmt.Println("weixinSrvName ", port)

	// service registry
	_, err := consul.Register(weixinSrvName, port)
	if err != nil {
		return fmt.Errorf("failed to register service: %v", err)
	}

	return nil
}
