package frontend

import (
	"net/http"
	"html/template"
	"log"
	"strconv"
)

// Server implements frontend service
type Server struct {

}

// new server
func NewServer() *Server {
	return &Server{

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

// Run the server
func (s *Server) Run(port int) error {

	host := ":" + strconv.Itoa(port)
	log.Println("server" + host)

	http.HandleFunc("/", sayhelloName) //设置访问的路由
	err := http.ListenAndServe(host, nil) //设置监听的端口
	if err != nil {
		log.Println("error run", err)
	}

	return err
}

