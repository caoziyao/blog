

class FileBrowser extends BaseComponent{
    constructor(element) {
        super()
        // hljs heightjs
        this.md = new Remarkable();
        this.element = element;

    }

    static new(...args) {
        return new this(...args)
    }


    renderMarkDown() {
        let eles = _es(this.element);

        for (let i = 0; i < eles.length; i++){
            let e = eles[i];
            let html = e.innerHTML.trim();
            html = this.md.render(html);
            e.innerHTML = html;

        }
        this.renderHightLine()

    }
}

