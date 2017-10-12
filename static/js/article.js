
const init2 = function () {
     let src = _e('#id-input-src textarea').value

    log('srccc', _e('#id-input-src'), src)
     let md = new Remarkable();
            let html = md.render(src);
            _e('#id-editor-result').innerHTML = html;

            $('pre code').each(function (i, block) {
        hljs.highlightBlock(block);
    });
}



const init = function () {


    let fb = FileBrowser.new('.file-browser');
    fb.renderMarkDown()
    //fb.renderMarkDown()
}


const __main = function () {
   init()
}

__main()
