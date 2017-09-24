

class BaseComponent{
    constructor() {
        this.hljs = hljs
    }

    static new(...args) {
        return new this(...args)
    }

    // 高亮语法
    renderHightLine() {
        let hljs = this.hljs;
         $('pre code').each(function(i, block) {
            hljs.highlightBlock(block);
         });
    };
}