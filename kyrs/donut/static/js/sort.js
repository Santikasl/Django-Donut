const sortPost = document.getElementById("sort-post")
console.log(sortPost)
const mainContent = document.getElementById("mainId")
const mainContent2 = document.getElementById("mainId2")
console.log(mainContent)
let sort = false;
$(document).on('click', '#sort-form', function (e) {
    if (sort === false) {
        mainContent.style.display = 'none'
        sortPost.style.display = 'grid'
        sort = true;
    } else {
        mainContent.style.display = 'grid'
        sortPost.style.display =  'none'
        sort = false;
    }
})
