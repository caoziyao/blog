
// 失去焦点保存事件
var bindBlurEvent = function () {

    let fe = FileEdit.new();
    fe.saveHTML();

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


