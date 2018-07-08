package route

import (
	"log"
	//"net/http"

	"kuaibiji/services/frontend/controllers"
	"fmt"
	"reflect"
	"net/http"

	"kuaibiji/services/frontend/common"
)

type interfaceControl interface {
	HandlerRequest(w http.ResponseWriter, r *http.Request)
}

func Router(path string, control interfaceControl) {
	fmt.Println("type:", reflect.TypeOf(control))
	fmt.Println(control)

	http.HandleFunc(path, control.HandlerRequest)

}

func RigisterRoutes(srv *common.Server) {
	log.Println("route /")
	//http.HandleFunc("/", &controllers.IndexController{}) //设置访问的路由
	Router("/", &controllers.IndexController{}) //设置访问的路由

	c := controllers.NewNoteBookController(srv.GetNotebookClient())

	Router("/notebook", c) //设置访问的路由

}
