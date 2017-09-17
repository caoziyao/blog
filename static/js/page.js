

// 自适应 textarea 高度
/*
* _e('textarea').addEventListener('keyup', function (event) {
    let target = event.target;
    target.height = target.scrollHeight
});
* */

const saveHtml = function (content) {

    const callback = function (response) {
        let r = JSON.parse(response);
        if (r.status == 1){
            log('保存成功')
        }
    };

    let url = '/page/api/edit_page';
    let path = _e('.head-filename').dataset.filepath;
    let data = {
        content: content,
        path: path,
    };

    Api.post(url, JSON.stringify(data), callback)

};


const codeHtml = function (content) {
    let src = '``` \n' + content + ' \n ```'
    return src
};

const isCode = function (type) {
    let codeList = ['py', 'js'];
    return codeList.includes(type)
};

const renderHightLine = function () {
     $('pre code').each(function(i, block) {
        hljs.highlightBlock(block);
     });
};


const init = function () {
    let textarea = _e('#id-input-src textarea');
    let src = textarea.value;
    let type =  textarea.dataset.type;
    if (isCode(type)) {
        src = codeHtml(src)
    }
    let md = new Remarkable();
    let html = md.render(src);
    _e('#id-editor-result').innerHTML = html;

    renderHightLine()
};

_e('#id-input-src').addEventListener('input', function() {
    let src = event.target.value;
    let textarea = _e('#id-input-src textarea');
    let type =  textarea.dataset.type;

    if (isCode(type)) {
         src = codeHtml(src)
    }

    let md = new Remarkable();
    let html = md.render(src);
    _e('#id-editor-result').innerHTML = html;

     renderHightLine()
});


// 同步滚动
_e('textarea').addEventListener('scroll', function (event) {
     let target = event.target;
     document.body.scrollTop = target.scrollTop;
     log('target.scrollTop', event)
});


_e('textarea').addEventListener('blur', function (event) {
    let target = event.target;
    let content = target.value;
    //log('targ', target)
    saveHtml(content)
});



const __main = function () {
    init()
};

window.onload = function () {
    __main()
}
