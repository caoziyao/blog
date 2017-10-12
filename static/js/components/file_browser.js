

class FileBrowser extends BaseComponent{
    constructor(element) {
        super()
        // hljs heightjs

        this.element = element;

    }

    static new(...args) {
        return new this(...args)
    }


    renderMarkDown() {
           let e = _e(this.element);

            let src = _e('textarea').value.trim() ;
            let md = new Remarkable();

            let html = md.render(src);
           // log('src', src)

            e.innerHTML = html;

        this.renderHightLine()

    }
}

