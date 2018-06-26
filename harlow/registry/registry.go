package registry



import (
	consul "github.com/hashicorp/consul/api"
)

// 服务发现
func NewClient(addr string) (*Client, error)  {
	cfg := consul.DefaultConfig()
	cfg.Address = addr

	c, err := consul.NewClient(cfg)
	if err != nil {
		return nil, err
	}

	return &Client{c}, nil
}

type Client struct {
	*consul.Client
}