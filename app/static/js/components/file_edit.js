

class FileEdit extends BaseComponent{
    constructor() {
        super()

    }

    static new(...args) {
        return new this(...args)
    }

    renderMarkdown() {
        let self = this;
          _e('#id-input-src').addEventListener('input', function() {
            let src = event.target.value;
            // let textarea = _e('#id-input-src textarea');
            // let type =  textarea.dataset.type;

          //  log('srcwww', src)


            let md = new Remarkable();
            let html = md.render(src);
            _e('#id-editor-result').innerHTML = html;

             self.renderHightLine()
        });
    }

    saveHTML() {
        _e('textarea').addEventListener('blur', function (event) {
            let target = event.target;
            let ele = target.closest('.page-content-left');
            let title = ele.querySelector('.file-title').value;
            let id = ele.dataset.noteid;
            let catalogId = ele.dataset.catalogid || 0;
            let content = target.value;
            //log('targ', target)
            let data = {
                catalog_id: catalogId,
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


    }
}