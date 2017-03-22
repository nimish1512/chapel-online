/*
This is the main controller of the view. 
Functionalities such as default settings, showing output,
showing errors, posting data to the API are carried out
by this file.

*/

$(function() {
	/*
	Setting up the default 'Hello, World!' code in the code editing area.
	*/
	document.getElementById("comment").value = '// Simple hello world \nwriteln("Hello, world!");    // print \'Hello, world!\' to the console';
	/*
	Setting up dynamic line numbers system.
	This allows to display line numbers as lines are inserted in the code
	editing area. Customization of line numbers can be done by passing in
	arguements as shown below or by changing CSS classes from main.css
	file.
	*/  
	$("#comment").numberedtextarea({
		allowTabChar:true,
	});
	//Take action on click of Compile & Run button
	$('.hit').on('click', function(event){
	/*
	Sets up message for user while posting data
	*/
		$("body").mLoading({
  			text:"Compiling your code...",
  			mask:true,
		});
		event.preventDefault();
	/*
	Disables user actions when a request is being sent to the API.
	This helps in maintaining code consistency and lesser API calls.
	*/
		$("body").mLoading('show');
	/*
	Standard AJAX call to the API.
	Server sends data in JSON format.
	Method used for interaction is POST.
	*/	
		$.ajax({
			url:"index.php",
			data:"code="+$('#comment').val(),
			type:"POST",
			dataType:"json",
			success:function(reply){
	/*
	Unmask the page after receiving dat from the serer.
	*/			
				$("body").mLoading('hide');
	/*
	Some formatting of data based on its class (Success or Error).
	If Success, show success message and result.
	*/
				if(reply.status=='success'){
					$('#result').html("<span class='success'>Success: </span>"+reply.op);
				}
	/*
	If Error, show error  message and result.
	*/
				else{
					$('#result').html("<span class='error'>Compilation Error: </span>"+reply.op);	
				}
				
			},
	/*
	AJAX call failure scenario is handled here. This might happen 
	due to lack of internet connectivity, API is down, etc...
	*/		
			error:function(reply){
				$("body").mLoading('hide');
				alert("Something went wrong and we couldn't take your request. Please try again after a while.");
			}
		});

	});
});
