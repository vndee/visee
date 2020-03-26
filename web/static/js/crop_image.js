const openModalBtn = document.querySelectorAll('[data-modal-target]')
const closeModalBtn = document.querySelectorAll('[data-close-button]')
const overlay = document.getElementById('overlay')

var x = 0
var y = 0
var width = 0
var height = 0
var img = document.querySelector("#target");

var selected_img = false;




openModalBtn.forEach(button => {
    button.addEventListener('click', () => {
        const modal = document.querySelector(button.dataset.modalTarget)
        openModal(modal)
    })
})

closeModalBtn.forEach(button => {
    button.addEventListener('click', () => {
        const modal = button.closest('.modal')
        closeModal(modal)
    })
})

function openModal(modal) {
    if (modal == null) return
    modal.classList.add('active')
    overlay.classList.add('active')

}

function closeModal(modal) {
    if (modal == null) return
    modal.classList.remove('active')
    overlay.classList.remove('active')
}


function previewImage(event) {
    var reader = new FileReader()
    var imageFile = document.getElementById("target")
	
    reader.onload = function() {
        if (reader.readyState == 2) {
            imageFile.src = reader.result;
        }
		if (selected_img == false) {
			selected_img = true
			select_coordinate()
			console.log('call crop')
		} else {
			src = $("#target").attr('src');
			$("#target").remove()
			$(".jcrop-holder" )[0].remove();
			$("#image-field").append("<img src="+src+" id='target' style='max-width: 400px; max-height: 400px;' />")
			select_coordinate()
			console.log('remove and call crop again')
		}
    }
    reader.readAsDataURL(event.target.files[0]);
}

function select_coordinate() {
	$('#target').Jcrop({ onSelect: showCoords, onChange: showCoords})
}

function showCoords(c) {	
	var dis_img = $("#target")
	if ( $("#target").length ) {
		var dis_img = $("#target")
		d_h = dis_img.css("height").replace("px","")
		d_w = dis_img.css("width").replace("px","")
		
		x = c.x/(d_w/img.naturalWidth)
		y = c.y/(d_h/img.naturalHeight)
		width = c.w/(d_w/img.naturalWidth)
		height = c.h/(d_h/img.naturalHeight)
	}
}

$('#crop_button').click(function() {
	var preview = document.getElementById('target');

	src_img = document.getElementById('target').src
	imageClipper(src_img, function() {
		this.crop(x, y, width, height)
		.toDataURL(function(dataUrl) {
			console.log('cropped!');
			preview.src = dataUrl;
		});
	});


	document.getElementsByClassName("jcrop-holder")[0].style.display = "none"
	document.getElementById("target").style.visibility = "";
	document.getElementById("target").style.display = "";
	$("#target").css("width","");
	$("#target").css("height","");

})