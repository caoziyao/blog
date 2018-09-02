package serve

import (
	"fmt"
	"kuaibiji/registry"
)

const userSrvName = "srv-user"


func runUser(port int, consul *registry.Client, jaegeraddr string) error {
	fmt.Println("runNotebook ", port)


	_, err := consul.Register(userSrvName, port)
	if err != nil {
		return fmt.Errorf("failed to register service: %v", err)
	}

	return nil

}
