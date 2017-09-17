

class FileBrowser {
    constructor(element) {
        // hljs heightjs
        this.hljs = hljs;
        this.md = new Remarkable();
        this.element = element;

    }

    static new(...args) {
        return new this(...args)
    }

    renderHightLine() {
        let hljs = this.hljs;
         $('pre code').each(function(i, block) {
            hljs.highlightBlock(block);
         });
    };


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

