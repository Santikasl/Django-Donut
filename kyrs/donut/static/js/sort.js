const sortPost = document.getElementById("sort-post")
const mainContent = document.getElementById("mainId")
let sort = false;
$(document).on('click', '#sort-form', function (e) {
    $.ajax({
        type: 'POST',
        url: '/sort/',
        data: {
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (res_post) {
            const dataPost = res_post.data
            if (Array.isArray(dataPost) && sort === false) {
                sortPost.style.display = 'grid'
                mainContent.style.display='none'
                dataPost.forEach(sortPosts => {
                    sortPost.innerHTML += `
                    <div class="photo">
                        <img class="zoom" src="${sortPosts.img}" alt="" width="300px" height="380px"
                             style="border-radius: 30px;">
                        <div class="button2 content fade">
                            <p>Описание:</p>
                            <div class="description-post" id="description-post-id">
                                <p class="p-desc">${sortPosts.descriptions}</p>
                            </div>
                            <button class="more-btn" id="open${sortPosts.pk}">Подробнее</button>
                        </div>
                    </div>
                    <div class="overlay2" id="myOverlayopen${sortPosts.pk}">
                        <div class="popup2">
                            <div class="photo-post">
                                <img src="${sortPosts.img}" alt="" width="100%" height="100%"
                                     style=" object-fit: cover;">
                            </div>
                            <h1 class="title-post">ОПИСАНИЕ</h1>
                            <div class="description" id="description${sortPosts.pk}">
                                <p>${sortPosts.descriptions}</p>
                            </div>
                            <form action="{% url 'like' %}" method="post" class="like-form form-like" id="${sortPosts.pk}">
                                ${context_var}
                                <input type="hidden" name="post_id" value="${sortPosts.pk}">
                                <button class="ui button positive like-btn${sortPosts.pk}" id="btnlike${sortPosts.pk}"
                                        type="submit"><p
                                        {% if posts|color:user %}
                                        style="color: red;"
                                        {% endif %}
                                        class="like-img"
                                        id="like-img${sortPosts.pk}">
                                    ❤ {{ posts.liked.all.count }}</p></button>
                            </form>
                        </div>
                    </div>
                      
                  
                    `
                })
                sort = true;
            } else {
                sortPost.innerHTML = ""
                sortPost.style.display = 'none'
                mainContent.style.display = 'grid'
                sort = false;
            }
        },

        error: function (xhr, errmsg, err) {
            console.log("error"); // provide a bit more info about the error to the console
        }
    });
});

