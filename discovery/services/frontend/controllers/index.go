package controllers

import (
	"net/http"
	"log"

	"html/template"
)

type IndexController struct {
	BaseControll
}

//w http.ResponseWriter, r *http.Request
type funcHandlerRequest func(w http.ResponseWriter, r *http.Request)

func (this *IndexController) Get(w http.ResponseWriter, r *http.Request) {
	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()

	log.Println("path", r.URL.Path)

	t, err := template.ParseFiles("services/frontend/templates/index.html")
	if err != nil {
		log.Println("run ParseFiles", err)
	}
	log.Println(t.Execute(w, nil))
}

func (this *IndexController) HandlerRequest(w http.ResponseWriter, r *http.Request) {
	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()

	m := make(map[string]funcHandlerRequest)
	m["GET"] = this.Get

	method := r.Method
	if fun, ok := m[method]; ok {
		// 存在
		fun(w, r)
	} else {
		this.unknowMethod(w, r)
	}
}
