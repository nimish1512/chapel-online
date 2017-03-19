$(function() {
	 document.getElementById("comment").value = '// Simple hello world \nwriteln("Hello, world!");    // print \'Hello, world!\' to the console';
	$("#comment").numberedtextarea({
		allowTabChar:true,
	});
	$("#result").numberedtextarea();

	$('.hit').on('click', function(event){
		$("body").mLoading({
  			text:"Compiling...",
  			mask:true,
		});
		event.preventDefault();
		$("body").mLoading('show');
		$.ajax({
			url:"index.php",
			data:"code="+$('#comment').val(),
			dataType:"json",
			type:"POST",
			success:function(reply){
				$("body").mLoading('hide');
				document.getElementById('result').value = reply;
			},
			error:function(reply){
				$("body").mLoading('hide');
				console.log("error");
			}
		});

	});
});