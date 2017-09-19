
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
            if (r.status === 1) {
                let data = r.data;
                let html = data.content;
                _e('.file-browser').innerHTML = html;

                let fb = FileBrowser.new('.file-browser');
                fb.renderMarkDown();
            }
        })
}

// 绑定事件
bindEvents('.dropdwon-box-link', function (event) {

    let target = event.target;
    let ul = target.closest('.dropdwon-box-ul');
    let classList = target.classList;
    if (classList.contains('catalog')) {
       // loadCatalog(target, ul)

    } else if (classList.contains('note')) {
        loadNote(target, ul)

    }

});



var __main = function () {

    bindDropDownEvent('#id-catalog-btn')

}

window.onload = function () {
    __main()
}
