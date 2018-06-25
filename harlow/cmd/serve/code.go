package main

import (
	"fmt"
	"time"
)

func runCode(port int) error {
	fmt.Println("runCode ", port)

	fmt.Println("start sleeping...")
	time.Sleep(6 * time.Second)
	fmt.Println("end sleep.")

	return nil
}
