<?php

	require "ip_address.php";

	$clump_t = $_POST['clump_t'];
	$size_u = $_POST['size_u'];
	$shape_u = $_POST['shape_u'];
	$marginal_a = $_POST['marginal_a'];
	$epithelial_s = $_POST['epithelial_s'];
	$bare_n = $_POST['bare_n'];
	$bland_c = $_POST['bland_c'];
	$normal_n = $_POST['normal_n'];
	$mitoses = $_POST['mitoses'];

	$headers = array('Content-Type: application/json');
	$fields = array('clump_t'=>$clump_t, 'size_u'=>$size_u, 'shape_u'=>$shape_u,
					'marginal_a'=>$marginal_a, 'epithelial_s'=>$epithelial_s,
					'bare_n'=>$bare_n, 'bland_c'=>$bland_c, 'normal_n'=>$normal_n,
					'mitoses'=>$mitoses
				   );
	$payload = json_encode($fields);
	$url = 'http://' .$ip_address.':5000/bc/api';
	$curl_session = curl_init();
	
	curl_setopt($curl_session, CURLOPT_URL, $url);
	curl_setopt($curl_session, CURLOPT_POST, true);
	curl_setopt($curl_session, CURLOPT_HTTPHEADER, $headers);
	curl_setopt($curl_session, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($curl_session, CURLOPT_SSL_VERIFYPEER, false);
	curl_setopt($curl_session, CURLOPT_IPRESOLVE, CURL_IPRESOLVE_V4);
	curl_setopt($curl_session, CURLOPT_POSTFIELDS, $payload);
				
	$result = curl_exec($curl_session);

	curl_close($curl_session);
				
	echo $result;

?>