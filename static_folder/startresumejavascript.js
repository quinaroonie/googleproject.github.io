



function add_Skill_Entry(){
	var $container = $('#skillcontainer');
	var containerlength =$container.children().length;
	alert("length: " + containerlength);
	$container.append('<div id="skillentry'+ containerlength+'"> Name:  <input type="text" name="skillname"> <br> <br> Description of skill: <br> <textarea class="submissonfield" id="text" name="skill">Write your decription here.</textarea> <br> <br></div>');
}

function delete_Skill_Entry(){
	alert('works');
	var $container = $('#skillcontainer');
	var containerlength =$container.children().length - 1;

	//$container.remove(containerlength);

	alert("length: " + containerlength);

	var $latestskill = $container.children().get(containerlength);
	alert($latestskill)

//	var $latestskill = $('<div id="skillentry'+containerlength+'"> Name:  <input type="text" name="skillname"> <br> <br> Description of skill: <br> <textarea class="submissonfield" id="text" name="skill">Write your decription here.</textarea> <br> <br></div>');
	$latestskill.remove();
}



function setupEverything(){
	alert('Set up abc');

	var buttonskilladd = $('#addskill');
	buttonskilladd.on('click',add_Skill_Entry);

	var buttonskilldelete = $('#deleteskill');
	buttonskilldelete.on('click', delete_Skill_Entry);

	//alert('Set up');
}

$(document).ready(setupEverything);