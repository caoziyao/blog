


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


_e('.dropdwon-box').addEventListener('mouseleave', function (event) {
    let target = event.target
    target.classList.add('hidden')
    // this.style.display = 'none'

})



// 新建笔记
_e('#id-new-note').addEventListener('click', function () {
    let html = template('id-tmp-page-new', {data: ''});
    _e('.page-content').innerHTML = html

    let fb = FileBrowser.new('.file-browser');
    fb.renderMarkDown();
    bindBlurEvent()
});


var loadCatalog = function (target, ul) {

        let catalogId = ul.dataset.catalogid;
        let data = {
            catalog_id: catalogId,
        };
        ajax.loadCatalog(data, function (response) {
             let r = JSON.parse(response);
            log('r', r);
            if (r.status === 1) {
                let data = r.data;
                let html = template('id-tmp-page-content', {data: data});
                _e('.page-content').innerHTML = html

                let fb = FileBrowser.new('.file-browser');
                fb.renderMarkDown();

            }
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

var loadNote = function (target, ul) {
     let noteId = target.dataset.noteid;
     let catalogId = ul.dataset.catalogid;

        let data = {
            note_id: noteId,
            catalog_id: catalogId,
        };
        // log('data', data)

        ajax.loadNote(data, function (response) {
             let r = JSON.parse(response);
            log('r', r);
            if (r.status === 1) {
                let data = r.data;
                let html = template('id-tmp-page-edit', {data: data});
                _e('.page-content').innerHTML = html;

                let fb = FileBrowser.new('.file-browser');
                fb.renderMarkDown();
                bindBlurEvent()

                autoSetHight()
            }
        })
}

// 绑定事件
bindEvents('.dropdwon-box-link', function (event) {

    let target = event.target;
    let ul = target.closest('.dropdwon-box-ul');
    let classList = target.classList;
    if (classList.contains('catalog')) {
        loadCatalog(target, ul)

    } else if (classList.contains('note')) {
        loadNote(target, ul)

    }

});



var __main = function () {

    bindDropDownEvent('#id-catalog-btn')
    bindDropDownEvent('#id-new-btn')

}

window.onload = function () {
    __main()
}