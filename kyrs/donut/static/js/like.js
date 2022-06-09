// const postId = document.getElementById('post_id')
// id = postId.value;
//
// $(document).on('click', '#id-like',function(e){
//     $.ajax({
//         type:'POST',
//         url: '/like/',
//         data:{
//             csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
//             'id': id,
//             'description': description,
//         },
//         success:function(res_post2) {
//
//
//         },
//
//         error : function(xhr,errmsg,err) {
//         console.log("error"); // provide a bit more info about the error to the console
//     }
//     });
// });
//

$('.like-form').submit(function (e){
    e.preventDefault()
    const post_id = $(this).attr('id')
    const url = $(this).attr('action')
    let res;
    const like = $(`.like-btn${post_id}`).text()
    const intLike = like
    const trimCount = parseInt(intLike)
    console.log(trimCount)
    const btnlike = document.getElementById('btnlike'+post_id)
    console.log(like)
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            'post_id': post_id,
        },
        success: function (response) {

            if (response.value == 'Like'){

                res = trimCount - 1
                btnlike.innerHTML=`
                 ${res}
                `

            }else {

                res = trimCount + 1
              btnlike.innerHTML=`
                 ${res}
                `

            }
            console.log("secsues",response)

        },
        error : function(xhr,errmsg,err) {
             console.log("error");
    }
    })

})
