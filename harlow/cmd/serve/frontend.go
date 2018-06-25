package main

import (
	"fmt"
	"time"
)

func runFrontend(port int) error {
	fmt.Println("runFrontend ", port)

	fmt.Println("start sleeping...")
	time.Sleep(6 * time.Second)
	fmt.Println("end sleep.")

	return nil
}
