<?php

/*	A RESTFUL API for interaction with servers, formatting and calling necessary
	proceses for compilation of submitted program by the user.

/*
Do not make any changes in this file.
*/
if(isset($_POST['code'])){
	/*
	Generating a random filename for the .chpl file
	This way, caching of unchanged files can be done
	in future updates and improve efficiency.
	*/
	$filename= "base_file_".rand().".chpl";
	$file = fopen($filename,"w");
	$content = $_POST['code'];
	fwrite($file, $content);
	fclose($file);
	/*
	Calling the main python file for compilation
	and execution of the submitted code.
	*/
	$command = 'python3 controller.py '.$filename;
	$output = shell_exec($command);
	/*
	Checking flags in the output given by .py file
	for determining whether execution was 
	successful or some error was encountererd.
	*/
	$_output = ereg_replace("//error", "", $output); 
	if ($output==$_output){
		/*
		Some basic formatting so that the output 
		looks identical to what you get on a terminal
		*/
		$output = substr_replace($output, "", 0,2); 
		$output = substr_replace($output, "", -2,1);
		/*
		Replacing '\n' with '<br>' elements for HTML
		compatibility.
		*/
		$output = str_replace("\\n", "<br>", $output);
		$result = array('status'=>'success','op'=>$output);
		/*
		Sending output to the client handler
		*/
		echo json_encode($result);
		/*
		Calling the clean up routine to delete generated .chpl
		files and their executables. A little 
		house cleaning.
		*/
		$clean_up = shell_exec('bash remove.sh');
		die();	
	}
	else{
		$output = ereg_replace("//error", "", $output); 
		$result = array('status'=>'error','op'=>$output);
		/*
		Replacing '\n' with '<br>' elements for HTML
		compatibility.
		*/
		$output = str_replace("\\n", "<br>", $output);
		/*
		Sending output to the client handler
		*/
		echo json_encode($result);
		/*
		Calling the clean up routine to delete generated .chpl
		files and their executables. A little 
		house cleaning.
		*/
		$clean_up = shell_exec('bash remove.sh');
		die();	
			
	}
	
}
else{
	/*
	A bad request scenario is handled here. We won't be doing
	anything, but just killing the program so that malicious 
	attacks are avoided. Further security enhsncements are 
	under development.
	*/
	die();
}
?>
