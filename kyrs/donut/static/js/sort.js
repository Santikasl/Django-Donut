const sortPost = document.getElementById("sort-post")
console.log(sortPost)
const mainContent = document.getElementById("mainId")
const mainContent2 = document.getElementById("mainId2")
console.log(mainContent)
let sort = false;
$(document).on('click', '#sort-form', function (e) {
    if (sort === false) {
         mainContent2.style.display = 'none'
        sortPost.style.display = 'grid'
        mainContent.innerHTML = ""
        sort = true;
    } else {
        sortPost.style.display = 'none'
        sortPost.style.display = 'none'
         mainContent.innerHTML = ""
        mainContent2.style.display = 'grid'
        sort = false;
    }
})
