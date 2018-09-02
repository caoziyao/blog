package utilities

import (
	"net/http"
	"log"
	"net/url"
)

func GetQueryString(r *http.Request, name string) string {
	// 解析url传递的参数，对于POST则解析响应包的主体（request body）
	r.ParseForm()
	log.Println("path", r.URL.Path, r.URL.RawQuery)
	query, _ := url.ParseQuery(r.URL.RawQuery)

	value := query[name][0]
	return value
}
