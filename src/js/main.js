window.onload = function(){
	var variables = []

	const varInput = document.getElementById("var-input")
	const send = document.getElementById("send")

	function updateVarList(variables) {
		const varList = document.getElementById("var-list")
		let ol = document.createElement('ol')

		varList.innerHTML = ''
		ol.innerHTML = variables.map(variable => `<li>${variable} <i class="fa fa-close"></i></li>`).join('')
		varList.appendChild(ol)
	}

	varInput.addEventListener('keydown', function(e) {
		if (e.key == 'Enter') {
			variables.push(e.target.value)
			e.target.value = ''
			updateVarList(variables)
		}
	})

	send.addEventListener('click', function(e) {
		const fileInput = document.getElementById("csv")
		var file = fileInput.files[0]
		var form = new FormData()
		form.append('file', file)
		console.log(form)

		/*$.ajax({
			url : "/upload",
	        type: "POST",
	        cache: false,
	        contentType: false,
	        processData: false,
	        data : form,
	        success: function(response){
	            console.log('success')
	            console.log(response)
	        }
		})*/
	})



	$('#var-list').on('click', 'li', function(e) {

	})

}



