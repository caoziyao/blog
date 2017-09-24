


// 失去焦点保存事件
var bindBlurEvent = function () {

    let fe = FileEdit.new();
    fe.saveHTML();
    fe.renderMarkdown();
}

// 绑定下拉事件
var bindDropDownEvent = function (element) {
    let ele = element;
    _e(ele).addEventListener('click', function (event) {
        let target = event.target;
        let div = target.closest('.wiki-dropdwon-div');
        // log('div', div);
        div.querySelector('.dropdwon-box').classList.toggle('hidden')

    })
};


var autoSetHight = function () {
    $('textarea').on('focus', 'textarea', function() {
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
    $('textarea').on('input', 'textarea', function() {
        let i = this
        i.rows = Math.round(i.scrollHeight / i.dataset.dif)
    })

    _e('textarea').addEventListener('scroll', function (event) {
     let target = event.target;
     _e('.page-content-right').scrollTop = target.scrollTop;
     log('target.scrollTop', event)
});
}



var __main = function () {

     let fb = FileBrowser.new('.file-browser');
     fb.renderMarkDown();
     bindBlurEvent()

     autoSetHight()

}

window.onload = function () {
    __main()
}