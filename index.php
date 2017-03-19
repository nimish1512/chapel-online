<?php
if(isset($_POST['code'])){
	$filename= "base_file_".rand().".chpl";
	$file = fopen($filename,"w");
	$content = $_POST['code'];
	fwrite($file, $content);
	fclose($file);
	$command = 'python3 controller.py '.$filename;
	$output = shell_exec($command);
	echo json_encode($output);
	die();

}
else{
	die();
}
?>
