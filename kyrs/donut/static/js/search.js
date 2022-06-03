console.log("hellow world")

const url = window.location.href
const searchForm = document.getElementById("search-form")
const searchInput = document.getElementById("search-input")
const resultBlock = document.getElementById("results-block")

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value

const sendSearchData = (dataName) =>{
    $.ajax({
        type: 'POST',
        url:'search/',
        data: {
            'csrfmiddlewaretoken': csrf,
            'dataName': dataName,
        },
        success: (res)=>{
            console.log(res.data)
            const data = res.data
            if (Array.isArray(data)){
                resultBlock.innerHTML = ""

                data.forEach(dataName=>{
                    resultBlock.innerHTML += `
                        <div class="searchItems">
                       <a href="">
                       <div class="img-profile">
                       <img src="${dataName.img}" alt="" width="80px">
                       </div>
                       <h2 class="nameSearch">${dataName.name}</h2>
                        </a>
                        </div>
                        </br>
                    `
                })
            } else {
                if(searchInput.value.length > 0){
                    console.log(searchInput.value.length)
                    resultBlock.innerHTML = `<b> ${data} </b>`
                } else {
                    resultBlock.classList.add('not-visible')
                }
            }

        },
        error:(err) => {
            console.log(err)
        }
    })
}


searchInput.addEventListener('keyup', e =>{
    console.log(e.target.value)

    if(resultBlock.classList.contains('not-visible')){
        resultBlock.classList.remove('not-visible')
    }

    sendSearchData(e.target.value)
})

