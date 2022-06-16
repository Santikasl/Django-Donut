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
                mainContent.innerHTML = ""
                dataPost.forEach(sortPosts => {
                    sortPost.innerHTML += `
    <script src="like.js" defer></script>
                    <div class="photo">
                        <img class="zoom" src="${sortPosts.img}" alt="" width="300px" height="380px"
                             style="border-radius: 30px;">
                        <div class="button2 content fade">
                            <p>Описание:</p>
                            <div class="description-post" id="description-post-id">
                                <p class="p-desc">${sortPosts.descriptions.split('\n').join('<br>')}</p>
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
                            <form action="${like_urs}" method="post" class="like-form form-like" id="l${sortPosts.pk}">
                               <input type='hidden' name='csrfmiddlewaretoken' value='${context_var}' />

                                <input type="hidden" name="post_id" value="${sortPosts.pk}">
                                <button class="ui button positive like-btn${sortPosts.pk}" id="btnlike${sortPosts.pk}" type="submit" style="color: red;">
                                <p class="like-img" id="like-img${sortPosts.pk}"> ❤ ${sortPosts.like}</p>
                                </button>
                            </form>
                        </div>
                    </div>
                      
                  
                    `
                })
                sort = true;
            } else {
                const all_posts = res_post.a
                sortPost.innerHTML = ""
                sortPost.style.display = 'none'
                all_posts.forEach(allPosts => {
                    mainContent.innerHTML += `
                        <div class="photo">
                            <img class="zoom" src="${allPosts.img}" alt="" width="300px" height="380px"
                                 style="border-radius: 30px;">
                                <div class="button2 content fade">
                                    <p>Описание:</p>
                                    <div class="description-post" id="description-post-id">
                                        <p class="p-desc">${allPosts.descriptions.split('\n').join('<br>')}</p>
                                    </div>
                                    <button class="more-btn" id="open${allPosts.pk}">Подробнее</button>
                                </div>
                        </div>
                    <div class="overlay2" id="myOverlayopen${allPosts.pk}">
                        <div class="popup2">
                            <div class="photo-post">
                                <img src="${allPosts.img}" alt="" width="100%" height="100%"
                                     style=" object-fit: cover;">
                            </div>
                            <h1 class="title-post">ОПИСАНИЕ</h1>
                            <div class="description" id="description${allPosts.pk}">
                                <p>${allPosts.descriptions}</p>
                            </div>
                            <form action="{% url 'like' %}" method="post" class="like-form form-like"
                                  id="e${allPosts.pk}">
                                   <input type='hidden' name='csrfmiddlewaretoken' value='${context_var}' />
                                <input type="hidden" name="post_id" value="${allPosts.pk}">
                                    <button class="ui button positive like-btn${allPosts.pk}"
                                            id="btnlike${allPosts.pk}"
                                            type="submit"><p
                                        {% if posts|color:user %}
                                        style="color: red;"
                                        {% endif %}
                                        class="like-img"
                                        id="like-img${allPosts.pk}">
                                        ❤ ${allPosts.like}</p></button>
                            </form>
                        </div>
                    </div>

                    `
                })
                sort = false;
            }
        },

        error: function (xhr, errmsg, err) {
            console.log("error"); // provide a bit more info about the error to the console
        }
    });
});

