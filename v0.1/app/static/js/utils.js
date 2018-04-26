

const _e = sel => document.querySelector(sel);
const _es = sel => document.querySelectorAll(sel);
const log = console.log.bind(console);


const bindEvents =  (element, eventName, callback) => {
    let es = _es(element);
    for (let i = 0; i < es.length; i++) {
        let e = es[i];
        e.addEventListener(eventName, callback)
    }
};


const renderHightLine = function () {
     $('pre code').each(function(i, block) {
        hljs.highlightBlock(block);
     });
};

// js获取url参数值
const queryStringFromUrl = (name) => {
    let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    let r = window.location.search.substr(1).match(reg);
    if (r != null) {
        return unescape(r[2]);
    }
    return null;
}