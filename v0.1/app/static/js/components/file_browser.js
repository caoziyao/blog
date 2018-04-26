class FileBrowser extends BaseComponent {
    constructor(element, data) {
        super()
        // hljs heightjs
        this.element = element
        this.data = data

    }

    static new(...args) {
        return new this(...args)
    }

    renderMarkDown() {
        let e = _e(this.element)
        let data = this.data
        // let src = _e('textarea').value.trim()
        let md = new Remarkable();
        let html = md.render(data);
        e.innerHTML = html;
        this.renderHightLine()

    }
}

