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

// Server implements frontend service
//type Server struct {
//	notebookClient proto.NotebookClient
//	userClient proto.UserClient
//	tracer        opentracing.Tracer
//}
//
//
//// new server
//func NewServer(nc proto.NotebookClient, uc proto.UserClient, tr opentracing.Tracer) *Server {
//
//	//srv := common.NewServer(nc, uc, tr)
//	//return srv
//	return &Server{
//		notebookClient:  nc,
//		userClient:  	uc,
//		tracer:        tr,
//	}
//}

//
//
//
//// get bookbook
//func (s *common.Server)getNotebookHandler(w http.ResponseWriter, r *http.Request){
//	w.Header().Set("Access-Control-Allow-Origin", "*")
//
//	//解析url传递的参数，对于POST则解析响应包的主体（request body）
//	r.ParseForm()
//	ctx := r.Context()
//
//	log.Println("path", r.URL.Path)
//
//	//type User struct {
//	//	Name string
//	//	IsAdmin bool
//	//	Followers uint
//	//}
//	//
//	//user := User{
//	//	Name:      "cizixs",
//	//	IsAdmin:   true,
//	//	Followers: 36,
//	//}
//	data, err := s.notebookClient.GetNotebookInfo(ctx, &proto.GetNoteBookRequest{
//		UserId: "oMNol0Yk9XeI_0jHsYuFgFsQ2h6s",
//	})
//	if err != nil {
//		http.Error(w, err.Error(), http.StatusInternalServerError)
//		log.Println("error", r.URL.Path)
//		return
//	}
//
//	//rjson := map[string]interface{}{
//	//	"type":     "FeatureCollection",
//	//	"features": data,
//	//}
//	//json.NewEncoder(w).Encode(rjson)
//	jData, err := json.Marshal(data)
//	if err != nil {
//		panic(err)
//	}
//	w.Header().Set("Content-Type", "application/json")
//	w.Write(jData)
//
//	//json.NewEncoder(w).Encode(user)
//}
//
//
//// get bookbook
//func (s *Server)getUserHandler(w http.ResponseWriter, r *http.Request){
//	w.Header().Set("Access-Control-Allow-Origin", "*")
//
//	//解析url传递的参数，对于POST则解析响应包的主体（request body）
//	r.ParseForm()
//	ctx := r.Context()
//
//	log.Println("path", r.URL.Path)
//
//	data, err := s.userClient.GetUserInfo(ctx, &proto.GetUserRequest{
//		UserId: "oMNol0Yk9XeI_0jHsYuFgFsQ2h6s",
//	})
//	if err != nil {
//		http.Error(w, err.Error(), http.StatusInternalServerError)
//		log.Println("error", r.URL.Path)
//		return
//	}
//
//	jData, err := json.Marshal(data)
//	if err != nil {
//		panic(err)
//	}
//	w.Header().Set("Content-Type", "application/json")
//	w.Write(jData)
//
//}

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

	//
	//host := ":" + strconv.Itoa(port)
	//log.Println("server" + host)
	//
	//http.HandleFunc("/", sayhelloName) //设置访问的路由
	//http.HandleFunc("/notebook", s.getNotebookHandler) //设置访问的路由
	//
	//err := http.ListenAndServe(host, nil) //设置监听的端口
	//if err != nil {
	//	log.Println("error run", err)
	//}

	return err
}
