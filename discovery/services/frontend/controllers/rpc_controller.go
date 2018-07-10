package controllers

import (
	"net/http"
	"context"
	"log"
	"google.golang.org/grpc"
)

type RPCController struct {

}


func Fetch(fun func(ctx context.Context, args *interface{}, opts ...grpc.CallOption) (*interface{}, error),
	ctx context.Context, w http.ResponseWriter, args *interface{})  (interface{}, error) {
	data, err := fun(ctx, args)

	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println("error path")
		return data, err
	}

	return data, err
}