package controllers

import (
	"net/http"
	"log"
	"kuaibiji/services/proto"

	util "kuaibiji/services/frontend/utilities"
)

type NoteBookController struct {
	BaseControll
	notebookClient proto.NotebookClient
	userClient     proto.UserClient
}

func NewNoteBookController(nc proto.NotebookClient, uc proto.UserClient) *NoteBookController {
	return &NoteBookController{
		notebookClient: nc,
		userClient:     uc,
	}
}

//w http.ResponseWriter, r *http.Request
func (this *NoteBookController) Get(w http.ResponseWriter, r *http.Request) {
	//w.Header().Set("Access-Control-Allow-Origin", "*")

	ctx := r.Context()
	userId := util.GetQueryString(r, "user_id")

	//userId := "oMNol0Yk9XeI_0jHsYuFgFsQ2h6s"
	// 获得 user
	user, err := this.userClient.GetUserInfo(ctx, &proto.GetUserRequest{
		UserId: userId,
	})
	log.Println("user", user.Data, err)

	if user.Data.UserId != "" {
		// 如果存在用户
		log.Println("ssssss", user.Data)
		data, err := this.notebookClient.GetNotebookInfo(ctx, &proto.GetNoteBookRequest{
			UserId: userId,
		})
		//data, err := Fetch(this.notebookClient.GetNotebookInfo, ctx, w, &proto.GetNoteBookRequest{
		//		UserId: userId,
		//	})

		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			log.Println("error", r.URL.Path)
			return
		} else {
			this.sendSuccess(w, data.Data)
		}

	} else {
		this.sendFail(w, "not user")
	}
}

func (this *NoteBookController) HandlerRequest(w http.ResponseWriter, r *http.Request) {
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
