class FileEdit extends BaseComponent {
    constructor() {
        super()

    }

    static new(...args) {
        return new this(...args)
    }

    renderMarkdown() {
        let self = this;
        _e('#id-editarea').addEventListener('input', function () {
            let src = event.target.value;
            let md = new Remarkable();
            let html = md.render(src);
            _e('.file-browser').innerHTML = html;
            self.renderHightLine()
        });
    }

}
