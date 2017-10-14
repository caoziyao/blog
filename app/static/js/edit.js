// 失去焦点保存事件
var bindBlurEvent = function () {

    let fe = FileEdit.new();
    fe.saveHTML();
    fe.renderMarkdown();
}



var autoSetHight = function () {
    $('textarea').on('focus', 'textarea', function () {
        let i = this
        let dif = i.scrollHeight
        i.value += '\n'
        dif = i.scrollHeight - dif
        let arr = i.value.split('')
        arr.splice(-1, 1)
        i.value = arr.join('')
        i.rows = Math.round(i.scrollHeight / dif)
        i.dataset.dif = dif
    })
    $('textarea').on('input', 'textarea', function () {
        let i = this
        i.rows = Math.round(i.scrollHeight / i.dataset.dif)
    })

    _e('textarea').addEventListener('scroll', function (event) {
        let target = event.target;
        _e('.page-content-right').scrollTop = target.scrollTop;
        //log('target.scrollTop', event)
    });
}


const init = function () {
     let src = _e('#id-input-src textarea').value

  //  log('srccc', _e('#id-input-src'), src)
     let md = new Remarkable();
            let html = md.render(src);
            _e('#id-editor-result').innerHTML = html;

            $('pre code').each(function (i, block) {
        hljs.highlightBlock(block);
    });
}


const __main = function () {


    let fb = FileBrowser.new('.file-browser');
    fb.renderMarkDown();

    bindBlurEvent()
    init()
    // autoSetHight()



}

window.onload = function () {
    __main()
}