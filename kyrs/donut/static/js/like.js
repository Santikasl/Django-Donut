$('.like-form').submit(function (e) {
    e.preventDefault()
    const post_id = $(this).attr('id')
    const url = $(this).attr('action')
    let res;
    const like = $(`.like-btn${post_id}`).text()
    const intLike = like
    const trimCount = parseInt(intLike)
    console.log(trimCount)
    const btnlike = document.getElementById('btnlike' + post_id)
    const like_img = document.getElementById('like-img' + post_id)
    console.log(like)
    $.ajax({
        type: 'POST',
        url: url,
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            'post_id': post_id,
        },
        success: function (response) {
            value = response.likes
            btnlike.innerHTML = `
            <p class="like-img" id="like-img${post_id}">❤ ${value}</p> 
            `
            if (response.like_value == 'Like') {
                btnlike.style.color = 'black'


            } else {
                btnlike.style.color = 'red'


            }


        },
        error: function (xhr, errmsg, err) {
            console.log("error");
        }
    })

})


