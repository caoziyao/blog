package route

import (
	"log"
	//"net/http"
	ctr "kuaibiji/services/frontend/controllers"
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
	http.HandleFunc(path, control.HandlerRequest)
}

func RigisterRoutes(srv *common.Server) {
	log.Println("route /")
	//http.HandleFunc("/", &controllers.IndexController{}) //设置访问的路由

	notebookClient := srv.GetNotebookClient()
	userClient := srv.GetUserClient()

	Router("/", &ctr.IndexController{})
	Router("/notebook", ctr.NewNoteBookController(notebookClient, userClient))

}
