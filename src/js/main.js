window.onload = function(){
	console.log('hello')
	var variables = []

	const varInput = document.getElementById("var-input")

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

	$('#var-list').addEventListener('click', 'li', function(e) {
		
	})

}



