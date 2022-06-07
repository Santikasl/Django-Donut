
$(document).on('click', '.edit2',function(e){
    let id = e.target.id;
    const description2 = document.getElementById("description"+ id)
    const textarea = document.getElementById("edit-desc"+id)
    console.log(textarea)
    textarea.style.display='none'

    console.log(id)
    $.ajax({
        type:'POST',
        url: '/edit/',
        data:{
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success:function(res_post2) {
            console.log("gwwrgewg")
            description2.style.display = 'none'
            textarea.style.display='flex'
            // const dataPost = res_post.data
            // if (Array.isArray(dataPost) && sort === false) {
            //     sortPost.style.display = 'grid'
            //     mainContent.style.display = 'none'
            //     dataPost.forEach(sortPosts => {
            //         sortPost.innerHTML += `
            //            <div class="photo">
            //             <img class="zoom" src="${sortPosts.img}" alt="" width="300px" height="380px"
            //                  style=" border-radius: 30px;">
            //             <div class="content fade button2" id="postbtn{{ posts.id}}}">
            //                 <p>Описание:</p>
            //                 <p>${sortPosts.descriptions}</p>
            //
            //             </div>
            //         </div>
            //
            //         `
            //     })
            //     sort = true;
            // }
            // else {
            //     sortPost.innerHTML = ""
            //     sortPost.style.display = 'none'
            //     mainContent.style.display = 'grid'
            //     sort = false;
            // }
        },

        error : function(xhr,errmsg,err) {
        console.log("error"); // provide a bit more info about the error to the console
    }
    });
});

