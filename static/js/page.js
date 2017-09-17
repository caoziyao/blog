

// 自适应 textarea 高度
/*
* _e('textarea').addEventListener('keyup', function (event) {
    let target = event.target;
    target.height = target.scrollHeight
});
* */


const codeHtml = function (content) {
    let src = '``` \n' + content + ' \n ```'
    return src
};

const isCode = function (type) {
    let codeList = ['py', 'js'];
    return codeList.includes(type)
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



// 同步滚动
_e('textarea').addEventListener('scroll', function (event) {
     let target = event.target;
     document.body.scrollTop = target.scrollTop;
     log('target.scrollTop', event)
});





const __main = function () {
    init()
};

window.onload = function () {
    __main()
}
