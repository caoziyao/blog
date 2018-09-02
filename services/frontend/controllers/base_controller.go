package controllers

import (
	"net/http"
	"encoding/json"
)

type BaseControll struct {
}

// rpc message 转换为 json
func (this *BaseControll) messageToJson(data interface{}) ([]byte) {
	jData, err := json.Marshal(data)
	if err != nil {
		panic(err)
	}
	return jData
}

// 发送 json 数据到 服务器
func (this *BaseControll) sendJson(w http.ResponseWriter, jData []byte) {
	w.Header().Set("Content-Type", "application/json")
	w.Write(jData)
}

// 发送 success json 数据到服务器
func (this *BaseControll) sendSuccess(w http.ResponseWriter, data interface{}) {
	w.Header().Set("Content-Type", "application/json")

	m := make(map[string]interface{})
	m["data"] = data
	m["status"] = "0"
	m["message"] = ""

	jData := this.messageToJson(m)
	this.sendJson(w, jData)
}

// 发送 失败 json 数据到 服务器
func (this *BaseControll) sendFail(w http.ResponseWriter, message string) {
	w.Header().Set("Content-Type", "application/json")

	m := make(map[string]string)
	m["data"] = ""
	m["status"] = "200212"
	m["message"] = message

	jData := this.messageToJson(m)
	this.sendJson(w, jData)
}

// 不知道 method
func (this *BaseControll) unknowMethod(w http.ResponseWriter, r *http.Request) {
	m := make(map[string]string)
	m["data"] = "unkonw request method"

	jData := this.messageToJson(m)
	this.sendJson(w, jData)
}
