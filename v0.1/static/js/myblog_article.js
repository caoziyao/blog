$(document).ready(function(){
    var log = function () {
        console.log(arguments)
    }

    
    var converter = new showdown.Converter();  
    // var text      = '#hello, markdown!',  
    var content = $('#contentID')
    // jQuery.trim(str) 描述:去掉字符串起始和结尾的空格
    var text = $.trim( content.text() )
    var html      = converter.makeHtml(text);  
    // alert(html);  
    
    content.html(html)

})