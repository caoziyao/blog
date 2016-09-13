/**
 * Created by Administrator on 2016/9/13.
 */
var api = {}

api.ajax = function (url, method, form, success, error) {
     var request = {
        url: url,
        type: method,
        data: form,
        success: success,
        error: error
    }

    $.ajax(request)
}


api.post = function (url, form, success, error) {
    api.ajax(url, 'post', form, success, error)
}


api.myblogCommAdd = function (form, success, error) {
    var url = '/api/comment/add'
    api.post(url, form, success, error)
}
