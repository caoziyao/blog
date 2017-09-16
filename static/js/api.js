
const _ajax = function (request) {
    //let _xsrf = getCookie("_xsrf");
    //log('xsrf', _xsrf)
    let r = new XMLHttpRequest();
    r.open(request.method, request.url, true);


    if (request.contentType !== undefined) {
        log('contentType')
        r.setRequestHeader('Content-Type', request.contentType)
    }
    r.onreadystatechange = function (event) {
        if (r.readyState === 4) {
            request.callback(r.response)
        }
    };
    //r.setRequestHeader("X-XSRFToken", _xsrf);
    if (request.method === 'GET') {
        r.send()
    } else {
        log('send post', request.data)
        r.send(request.data)
    }
};

const _post = function (url, data, callback) {
    let request = {
        url: url,
        method: 'POST',
        data: data,
        callback: callback,
    };
    Api.ajax(request)
};

const _get = function (url, callback) {
    let request = {
        url: url,
        method: 'GET',
        callback: callback,
    };
    Api.ajax(request)
};

const Api = {
    ajax: _ajax,
    post: _post,
    get: _get,
};