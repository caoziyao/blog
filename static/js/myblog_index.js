/**
 * Created by Administrator on 2016/9/13.
 */


$(document).ready(function () {


    var log = function () {
        console.log(arguments)
    }

    var hide = $('.hide')

    // 评论超链接
    $('.entry-footer-comment').click(function () {
        log('评论超链接')
        $(this).parent().next().slideToggle()
        return false
    })


    // 评论提交按钮
    $('.blog-comment-add').on('click', function () {
        log('blog-comment-add')
        var button = $(this)
        var parent = button.parent()
        var comment = parent.find('.comment-content').val()
        var comment_list = $('.comment-list')

        // comment_list.css("background", "#ff1100")

        var form = {
            'comment': comment
        }

        var success = function () {
            log('success!!', arguments)
            var response = arguments[0]
            var str = JSON.parse(response)
            var username = str.username
            log('js username', username)

            var comment = str.comment
            var created_time = comment.created_time
            var cell = `
                <div >
                    <div>${comment}</div>
                </div>
            `;
            comment_list.append(cell)
        }

        var error = function () {
            log('error!!', arguments)
        }

        api.myblogCommAdd(form, success, error)
    })

})

       // var request = {
       //      url: '/api/comment/add',
       //      type: 'post',
       //      data: comment_dict,
       //      success: function () {
       //          log('success!!', arguments)
       //          var response = arguments[0]
       //          var str = JSON.parse(response)
       //          var username = str.username
       //          log('js username', username)
       //
       //          var comment = str.comment
       //          var created_time = comment.created_time
       //          var cell = `
       //              <div >
       //                  <div>${comment}</div>
       //              </div>
       //          `;
       //
       //
       //          comment_list.append(cell)
       //      },
       //      error: function () {
       //          log('error!!', arguments)
       //      }
       //  }
       //
       //  $.ajax(request)
