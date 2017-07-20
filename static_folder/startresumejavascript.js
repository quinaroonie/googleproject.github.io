



function add_Skill_Entry(){
	var $container = $('#skillcontainer');
	var containerlength =$container.children().length;
	//alert("length: " + containerlength);

	$container.append('<div id="skillentry'+ containerlength+'"> Name:  <input type="text" name="skillname'+containerlength+'"> <br> <br> Description of skill: <br> <textarea class="submissonfield" id="text" name="skill'+containerlength+'">Write your decription here.</textarea> <br> <br></div>');
}

function delete_Skill_Entry(){
	//alert('works');
	var $container = $('#skillcontainer');
	var containerlength =$container.children().length - 1;


	//alert("length: " + containerlength);

	var $latestskill = $container.children().get(containerlength);
	alert($latestskill)
	$latestskill.remove();
}

function add_Experience(){
	var $container =$('#jobcontainer');
	var containerlength = $container.children().length;
	//alert('add_Experence')
	$container.append('<div id="jobentry'+containerlength+'"> <br> Job Position : <input type="text" name="jobposition"> <br> <br> Description of previous postions: <br> <textarea class="submissonfield" id="text" name="des">Write your decription here.</textarea> </div>');
}

function delete_Experience(){
	var $container =$('#jobcontainer');
	var containerlength = $container.children().length - 1;

	var $latestjob = $container.children().get(containerlength);
	//alert($latestjob)
	$latestjob.remove();
}	

function add_Degree(){
	var $container = $('#degreecontainer');
	var containerlength = $container.children().length;
	$container.append('<div id="degreeentry'+containerlength+'"> <br> Name of Degree: <input type="text" name="degree"> <br> <br> School of which you earn degree: <input type="text" name="school"> </div>');

}

function delete_Degree(){
	var $container =$('#degreecontainer');
	var containerlength = $container.children().length - 1;

	var $latestdegree = $container.children().get(containerlength);
	//alert($latestdegree)
	$latestdegree.remove();
}


function setupEverything(){
	//alert('Set up abc');

	var buttonskilladd = $('#addskill');
	buttonskilladd.on('click',add_Skill_Entry);
	var buttonskilldelete = $('#deleteskill');
	buttonskilldelete.on('click', delete_Skill_Entry);

	var buttonExadd = $('#addexperience');
	buttonExadd.on('click', add_Experience);
	var buttonExdelete = $('#deleteexperience');
	buttonExdelete.on('click', delete_Experience);

	var buttondegreeadd = $('#adddegree') ;
	buttondegreeadd.on('click', add_Degree);
	var buttondeletedegree = $('#deletedegree');
	buttondeletedegree.on('click',delete_Degree);


	//alert('Set up');
}

$(document).ready(setupEverything);