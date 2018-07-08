package controllers

import (
	"net/http"
	"log"
	"kuaibiji/services/proto"
	"encoding/json"
)

type NoteBookController struct {
	notebookClient	proto.NotebookClient

}

func NewNoteBookController(nc proto.NotebookClient) *NoteBookController  {
	return &NoteBookController{
		notebookClient: nc,
	}
}

//w http.ResponseWriter, r *http.Request
func (this *NoteBookController)Get(w http.ResponseWriter, r *http.Request)  {
	w.Header().Set("Access-Control-Allow-Origin", "*")

	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()
	ctx := r.Context()

	log.Println("path", r.URL.Path)


	data, err := this.notebookClient.GetNotebookInfo(ctx, &proto.GetNoteBookRequest{
		UserId: "oMNol0Yk9XeI_0jHsYuFgFsQ2h6s",
	})
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		log.Println("error", r.URL.Path)
		return
	}


	jData, err := json.Marshal(data)
	if err != nil {
		panic(err)
	}
	w.Header().Set("Content-Type", "application/json")
	w.Write(jData)
}


func (this *NoteBookController)HandlerRequest(w http.ResponseWriter, r *http.Request){
	//解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()

	m := make(map[string] funcHandlerRequest)
	m["GET"] = this.Get
	//m["PUST"] = this.POST
	//m["PUT"] = this.PUT
	//m["DEL"] = this.DEL

	method :=  r.Method

	fun := m[method]
	fun(w, r)

}

//// get bookbook
//func (this *NoteBookController)getNotebookHandler(w http.ResponseWriter, r *http.Request){
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