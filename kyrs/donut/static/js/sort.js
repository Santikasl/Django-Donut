// const url = window.location.href
const sortBtn = document.getElementById("sortBtn")
const csrf = document.getElementsByName('csrfmiddlewaretoken')[2].value
//
// const sort = (dataName) => {
//         $.ajax({
//             type: 'POST',
//             url: 'sort/',
//             data: {
//                 'csrfmiddlewaretoken': csrf,
//                 'dataName': dataName,
//             },
//             success: (res) => {
//                 alert("gewwg")
//             },
//             error: (err) => {
//                 console.log(err)
//         }
//     })
// }
//
// sortBtn.onclick = function(e) {
//     alert('Спасибо');
//     sort(e.target.value)
// };

$( document ).ready(function() {
    $("#sortBtn").click(
		function(){
			sendAjaxForm('result_form', 'ajax_form', 'sort/');
			return false;
		}
	);
});

function sendAjaxForm(result_form, ajax_form, url) {
    $.ajax({
        url:'sort/',
        type:'POST',
        dataType: "html",
        data: {
                'csrfmiddlewaretoken': csrf,
                'dataName': dataName,
        },
        success: function(response) {
        	result = $.parseJSON(response);
        	$('#result_form').html('Имя: '+result.name+'<br>Телефон: '+result.phonenumber);
    	},
    	error: function(response) { // Данные не отправлены
            $('#result_form').html('Ошибка. Данные не отправлены.');
    	}
 	});
}

