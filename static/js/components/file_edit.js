

class FileEdit {
    constructor() {
        // hljs heightjs

    }

    static new(...args) {
        return new this(...args)
    }

    saveHTML() {
        _e('textarea').addEventListener('blur', function (event) {
            let target = event.target;
            let ele = target.closest('.page-content-left');
            let title = ele.querySelector('.file-title').value;
            let id = ele.dataset.noteid;
            let content = target.value;
            //log('targ', target)
            let data = {
                note_id: id,
                content: content,
                title: title,
            };

            ajax.saveHTML(data, function (response) {
                let r = JSON.parse(response);
                if (r.status === 1) {
                    log('保存成功')
                }
            })

        });

        _e('#id-input-src').addEventListener('input', function() {
            let src = event.target.value;
            let textarea = _e('#id-input-src textarea');
            let type =  textarea.dataset.type;

            // if (isCode(type)) {
            //      src = codeHtml(src)
            // }

            let md = new Remarkable();
            let html = md.render(src);
            _e('#id-editor-result').innerHTML = html;

             renderHightLine()
        });
    }
}
