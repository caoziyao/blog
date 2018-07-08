package controllers

import (
	"net/http"
	"log"

	"html/template"
	"encoding/json"
)

type IndexController struct {

}

//w http.ResponseWriter, r *http.Request
type funcHandlerRequest func(w http.ResponseWriter, r *http.Request)

func unknowMethod(w http.ResponseWriter, r *http.Request)  {
	m := make(map[string] string)
	m["data"] = "unkonw request method"


	jData, err := json.Marshal(m)
	if err != nil {
		panic(err)
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(jData)
}

func (this *IndexController)Get(w http.ResponseWriter, r *http.Request){
	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()

	log.Println("path", r.URL.Path)

	t, err := template.ParseFiles("services/frontend/templates/index.html")
	if err != nil {
		log.Println("run ParseFiles", err)
	}
	log.Println(t.Execute(w, nil))
}

func (this *IndexController)POST(w http.ResponseWriter, r *http.Request){
	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()

	log.Println("path", r.URL.Path)

	t, err := template.ParseFiles("services/frontend/templates/index.html")
	if err != nil {
		log.Println("run ParseFiles", err)
	}
	log.Println(t.Execute(w, nil))
}

func (this *IndexController)PUT(w http.ResponseWriter, r *http.Request){
	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()

	log.Println("path", r.URL.Path)

	t, err := template.ParseFiles("services/frontend/templates/index.html")
	if err != nil {
		log.Println("run ParseFiles", err)
	}
	log.Println(t.Execute(w, nil))
}

func (this *IndexController)DEL(w http.ResponseWriter, r *http.Request){
	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()

	log.Println("path", r.URL.Path)

	t, err := template.ParseFiles("services/frontend/templates/index.html")
	if err != nil {
		log.Println("run ParseFiles", err)
	}
	log.Println(t.Execute(w, nil))
}


func (this *IndexController)HandlerRequest(w http.ResponseWriter, r *http.Request){
	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()

	m := make(map[string] funcHandlerRequest)
	m["GET2"] = this.Get
	m["PUST"] = this.POST
	m["PUT"] = this.PUT
	m["DEL"] = this.DEL

	method :=  r.Method
	if fun, ok := m[method]; ok {
		// 存在
		fun(w, r)
	} else {
		unknowMethod(w, r)
	}
}



