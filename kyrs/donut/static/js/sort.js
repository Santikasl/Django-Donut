const sortPost = document.getElementById("sort-post")
const mainContent = document.getElementById("mainId")
let sort = false;
$(document).on('click', '#sort-form',function(e){
    $.ajax({
        type:'POST',
        url: '/sort/',
        data:{
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        },
        success:function(res_post) {
            const dataPost = res_post.data
            if (Array.isArray(dataPost) && sort === false) {
                sortPost.style.display = 'grid'
                mainContent.style.display = 'none'
                dataPost.forEach(sortPosts => {
                    sortPost.innerHTML += `
                       <div class="photo">
                        <img class="zoom" src="${sortPosts.img}" alt="" width="300px" height="380px"
                             style=" border-radius: 30px;">
                        <div class="content fade button2" id="postbtn{{ posts.id}}}">
                            <p>Описание:</p>
                            <p>${sortPosts.descriptions}</p>

                        </div>
                    </div>
                  
                    `
                })
                sort = true;
            }
            else {
                sortPost.innerHTML = ""
                sortPost.style.display = 'none'
                mainContent.style.display = 'grid'
                sort = false;
            }
        },

        error : function(xhr,errmsg,err) {
        console.log("error"); // provide a bit more info about the error to the console
    }
    });
});

