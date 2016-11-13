document.onload = function(){
	console.log('hello')
	var variables = []

	const varInput = document.getElementById("var-input")

	updateVarList(variables) {
		const varList = document.getElementById("var-list")
		let ol = document.createElement('ol')
		ol.innerHTML = variables.map(variable => `<li>${variable}</li>`)
		varList.innerHTML = ol
	}

	varInput.addEventListener('keydown', function(e) {
		if (e.key == 'Enter') {
			variables.push(e.target.value)
			e.target.value = ''
			updateVarList()
		}
	})

}



