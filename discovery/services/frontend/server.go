package frontend

import (
	"net/http"
	"log"

	//"kuaibiji/tracing"
	//"fmt"
	//"strconv"
	//"encoding/json"
	"kuaibiji/services/frontend/route"

	//"kuaibiji/services/frontend/common"

	"kuaibiji/services/frontend/common"
)


func tem() {
	//host := ":" + strconv.Itoa(port)
	//log.Println("server" + host)
	//
	//mux := tracing.NewServeMux(s.tracer)
	//mux.Handle("/", http.FileServer(http.Dir("services/frontend/templates")))
	//mux.Handle("/notebook", http.HandlerFunc(s.getNotebookHandler))
	//mux.Handle("/user", http.HandlerFunc(s.getUserHandler))
	//
	//return http.ListenAndServe(fmt.Sprintf(":%d", port), mux)
}

// Run the server
func Run(srv *common.Server, port int) error {
	route.RigisterRoutes(srv)

	//views.RigisterRoutes()
	//http.HandleFunc("/", sayhelloName) //设置访问的路由
	//http.HandleFunc("/notebook", s.getNotebookHandler) //设置访问的路由
	err := http.ListenAndServe(":5000", nil) //设置监听的端口
	if err != nil {
		log.Fatal("ListenAndServe: ", err)
	}

	return err
}
