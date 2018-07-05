package frontend

import (
	"net/http"
	"html/template"
	"log"
	"encoding/json"

	"kuaibiji/services/notebook/proto"
	"github.com/opentracing/opentracing-go"

	"kuaibiji/tracing"
	"fmt"
	"strconv"
)

// Server implements frontend service
type Server struct {
	notebookClient notebook.NotebookClient
	tracer        opentracing.Tracer
}

// new server
func NewServer(nc notebook.NotebookClient, tr opentracing.Tracer) *Server {
	return &Server{
		notebookClient:  nc,
		tracer:        tr,
	}
}

func sayhelloName(w http.ResponseWriter, r *http.Request){
	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()

	log.Println("path", r.URL.Path)

	t, err := template.ParseFiles("services/frontend/templates/index.html")
	if err != nil {
		log.Println("run ParseFiles", err)
	}
	log.Println(t.Execute(w, nil))
}

// get bookbook
func (s *Server)getNotebookHandler(w http.ResponseWriter, r *http.Request){
	w.Header().Set("Access-Control-Allow-Origin", "*")

	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()
	ctx := r.Context()

	log.Println("path", r.URL.Path)

	//type User struct {
	//	Name string
	//	IsAdmin bool
	//	Followers uint
	//}
	//
	//user := User{
	//	Name:      "cizixs",
	//	IsAdmin:   true,
	//	Followers: 36,
	//}

	user, err := s.notebookClient.GetNotebookInfo(ctx, &notebook.NotebookRequest{
		Name: "helloname",
	})
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println("error", r.URL.Path)
		return
	}

	data := map[string]interface{}{
		"type":     "FeatureCollection",
		"features": user,
	}

	json.NewEncoder(w).Encode(data)
}


// Run the server
func (s *Server) Run(port int) error {

	host := ":" + strconv.Itoa(port)
	log.Println("server" + host)

	mux := tracing.NewServeMux(s.tracer)
	mux.Handle("/", http.FileServer(http.Dir("services/frontend/templates")))
	mux.Handle("/notebook", http.HandlerFunc(s.getNotebookHandler))

	return http.ListenAndServe(fmt.Sprintf(":%d", port), mux)

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

	//return err
}

