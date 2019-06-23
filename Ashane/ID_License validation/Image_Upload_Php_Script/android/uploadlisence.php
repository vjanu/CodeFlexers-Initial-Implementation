<?php
	class emp{}
	
	$image = $_POST['image'];
	$name = $_POST['name'];
	
	if (empty($name)) { 
		$response = new emp();
		$response->success = 0;
		$response->message = "Please dont empty Name."; 
		die(json_encode($response));
	} else {
		$random = random_word(20);
		
		//$path = "images/".$random.".png";
		//$path = "images/".$name.".png";
		//$path = "Document_Validation_Final/Read_Old_NIC/tes-img/".$name.".png";
		$path = "file:///C:/Users/Ashane/Desktop/Read_Lisence/tes-img/".$name.".png";
		
		// sesuiakan ip address laptop/pc atau URL server
		//$actualpath = "http://192.168.10.177/android/upload_image/$path";
		//$actualpath = "localhost:8080/android/upload_image/$path";
		//$actualpath = "localhost:8080/android/$path";

			chmod ($path, 0777);
			file_put_contents($path,base64_decode($image));
			
			$response = new emp();
			$response->success = 1;
			$response->message = "Successfully Uploaded";
			die(json_encode($response));

	}	
	
	function random_word($id = 20){
		$pool = '1234567890abcdefghijkmnpqrstuvwxyz';
		
		$word = '';
		for ($i = 0; $i < $id; $i++){
			$word .= substr($pool, mt_rand(0, strlen($pool) -1), 1);
		}
		return $word; 
	}
	
?>	
