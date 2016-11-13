window.onload = function(){
	var variables = new Set();

	const varInput = document.getElementById("var-input")
	const send = document.getElementById("send")

	function updateVarList(variables) {
		const varList = document.getElementById("var-list")
		let ol = document.createElement('ol')

		varList.innerHTML = ''
		ol.innerHTML = Array.from(variables).map(variable => `<li>${variable} <i class="fa fa-close"></i></li>`).join('')
		varList.appendChild(ol)
	}

	varInput.addEventListener('keydown', function(e) {
		if (e.key == 'Enter') {
			variables.add(e.target.value)
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
	        xCord: xValue
	        success: function(response){
	            console.log('success')
	            console.log(response)
	        }
		})*/
	})

	$('#var-list').on('click', 'li', function(e){
		variables.delete(e.target.innerText.trim());
		updateVarList(variables);
	});

	$('.submitButton').on('click', function(e){
		$.ajax({
			url: "/upload",
			type: "POST",
			alphaValue: document.getElementById('alphaValue').innerText,
			titleValue: document.getElementById('titleValue').value,
			xValue: document.getElementById('xValue').value,
			yValue: document.getElementById('yValue').value,
			success: function(response){
				console.log('success')
				console.log(response);
			}
		})
	})
	
}

//Sliders
var el, newPoint, newPlace, offset;
 
// Select all range inputs, watch for change
$("input[type='range']").change(function() {

 // Cache this for efficiency
 el = $(this);
 
 // Measure width of range input
 width = el.width();
 
 // Figure out placement percentage between left and right of input
 newPoint = (el.val() - el.attr("min")) / (el.attr("max") - el.attr("min"));
  
  offset = -1;

 // Prevent bubble from going beyond left or right (unsupported browsers)
 if (newPoint < 0) { newPlace = 0; }
 else if (newPoint > 1) { newPlace = width; }
 else { newPlace = width * newPoint + offset; offset -= newPoint; }
 
 // Move bubble
 el
   .next("output")
   .css({
     left: newPlace,
     marginLeft: offset + "%"
   })
     .text(el.val());
 })
 // Fake a change to position bubble at page load
 .trigger('change');



