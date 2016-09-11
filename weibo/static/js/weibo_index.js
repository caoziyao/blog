/**
 * Created by Administrator on 2016/9/10.
 */


// alert('Hello jq')

var log = function(){
    // 调试
    console.log(arguments)
}

// var comm_display =  $('.comment-hide')

var comm = $('.comment')
var comm_display = $('.comment-hide')

comm.click(function () {
    comm_display.hide()
})