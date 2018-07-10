package serve

import (
	"fmt"
	"kuaibiji/registry"

)

const apiSrvName = "srv-api"



func runApi(port int, consul *registry.Client, jaegeraddr string) error {
	fmt.Println("apiSrvName ", port)

	// service registry
	_, err := consul.Register(apiSrvName, port)
	if err != nil {
		return fmt.Errorf("failed to register service: %v", err)
	}

	return nil

}
