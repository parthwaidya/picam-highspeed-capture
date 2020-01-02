<?php
 if($_SERVER['REQUEST_METHOD']=='POST'){
	 $file_name = $_FILES['file']['name'];
	 $file_size = $_FILES['file']['size'];
	 $file_type = $_FILES['file']['type'];
	 $temp_name = $_FILES['file']['tmp_name'];
	 $location = "../uploads/";
	 $url = "http://localhost/uploads/".$file_name;
	 move_uploaded_file($temp_name,$location.$file_name); 
 }else{
 	echo "Error";
 }
 ?>
