
function predict(){
	
	$.ajax({
		type: "POST",
		url: "../cgi-bin/php/predict_bc.php",
		async: false,
		datatype: 'json',
		data: {
			clump_t: clump_t_id.value,
			size_u: size_u_id.value,
			shape_u: shape_u_id.value,
			marginal_a: marginal_a_id.value,
			epithelial_s: epithelial_s_id.value,
			bare_n: bare_n_id.value,
			bland_c: bland_c_id.value,
			normal_n: normal_n_id.value,
			mitoses: mitoses_id.value
		},
		success: function(response){
			try {
				benign_id.innerHTML = "Error";
				malignant_id.innerHTML = "Error";
				console.log(response);
				var obj = JSON.parse(response);
				console.log(obj.benign);
				console.log(obj.malignant);
				benign_id.innerHTML = (parseFloat(obj.benign)*100).toFixed(1) + "%";
				malignant_id.innerHTML = (parseFloat(obj.malignant)*100).toFixed(1) + "%";
			}
			catch(err){
				console.log(response);
				benign_id.innerHTML = "Error";
				malignant_id.innerHTML = "Error";
			}

		},
		error: function(response){
			console.log(response);
			benign_id.innerHTML = "Error";
			malignant_id.innerHTML = "Error";
		}
	})
	
}

function page_load(){
	//get text input ids
	clump_t_id = document.getElementById("clump_t");
	size_u_id = document.getElementById("size_u");
	shape_u_id = document.getElementById("shape_u");
	marginal_a_id = document.getElementById("marginal_a");
	epithelial_s_id = document.getElementById("epithelial_s");
	bare_n_id = document.getElementById("bare_n");
	bland_c_id = document.getElementById("bland_c");
	normal_n_id = document.getElementById("normal_n");
	mitoses_id = document.getElementById("mitoses");
	
	//get prediction span ids
	benign_id = document.getElementById("benign");
	malignant_id = document.getElementById("malignant");
}

function benign(){

	clump_t_id.value = 2;
	size_u_id.value = 1;
	shape_u_id.value = 1;
	marginal_a_id.value = 1;
	epithelial_s_id.value = 2;
	bare_n_id.value = 2;
	bland_c_id.value = 1;
	normal_n_id.value = 1;
	mitoses_id.value = 1;
}

function malignant(){

	clump_t_id.value = 5;
	size_u_id.value = 10;
	shape_u_id.value = 10;
	marginal_a_id.value = 3;
	epithelial_s_id.value = 7;
	bare_n_id.value = 8;
	bland_c_id.value = 3;
	normal_n_id.value = 10;
	mitoses_id.value = 2;
}