$(document).ready(function() {
	var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/c_cpp");
    document.getElementById('editor').style.fontSize='16px';
    editor.setValue('\n#include <stdio.h> \n\nint main(){\n\n\tprintf("yes");\n\treturn 0;\n}');
  if(!("WebSocket" in window)){
  $('#chat').fadeOut("fast");
  $('<p>Oh no, you need a browser that supports WebSockets. How about <a href="http://www.google.com/chrome">Google Chrome</a>?</p>').appendTo('#container');
  }else{
      //The user has WebSockets

      connect();

      function connect(){
          var socket;
          var host = "ws://139.59.11.10:8000";

          try{
              var socket = new WebSocket(host);

              //message('<p class="event">Socket Status: '+socket.readyState);

              socket.onopen = function(){
              	alert("Connected");
                $('.status').empty();
                $('.status').append('Status: Idle')
             	 //message('<p class="event">Socket Status: '+socket.readyState+' (open)');
              }

              socket.onmessage = function(msg){
              	$("body").mLoading('hide');
              	terminal(msg.data);
             	 //message('<p class="message">Received: '+msg.data);
              }

              socket.onclose = function(){
              	//message('<p class="event">Socket Status: '+socket.readyState+' (Closed)');
              }			

          } catch(exception){
             console.log(exception);
          }

          function send(text){
              try{
              	//console.log(text);
                  socket.send(text);
                  //terminal(text)

              } catch(exception){
                 terminal('exception');
              }
              //$('#chat').val("");
          }

          function terminal(msg){
          	msg = msg.replace('\n','<br>');
            $('.display').append(msg);
          }

          $('.run').on('click',function(event) {
          		if(socket.readyState==socket.CLOSED || socket.readyState==socket.CLOSING){
          			alert("You are not connected to the server. Please refresh your page");
          			return;
          		}
          		else{
          			event.preventDefault();
          			var text = editor.getValue();
          			$('.display').empty()
          			if(text==""){
                  		terminal('Please enter a message');
                  		return ;
              		}
              		else{
                    $('.status').empty();
                    $('.status').append("Status: Running");
                    $("body").mLoading();
                    send(text);
              	  	}	
          	}
          		
          });	
          $('.reset').on('click',function(event) {
          		event.preventDefault();
               editor.setValue('\n#include <stdio.h> \n\nint main(){\n\n\tprintf("yes");\n\treturn 0;\n}');
          });
          $('.resume').on('click',function(event) {
          		if(socket.readyState==socket.CLOSED || socket.readyState==socket.CLOSING){
          			alert("You are not connected to the server. Please refresh your page");
          			return;
          		}
          		else{
          		event.preventDefault();
          		var signal = "resume,!!";
              $('.status').empty();
              $('.status').append("Status: Running");
          		send(signal);}
          });
          $('.pause').on('click',function(event) {
          		if(socket.readyState==socket.CLOSED || socket.readyState==socket.CLOSING){
          			alert("You are not connected to the server. Please refresh your page");
          			return;
          		}
          		else{
          		event.preventDefault();
          		var signal = "pause,!!";
              $('.status').empty();
              $('.status').append("Status: Paused");
          		send(signal);}
          });

      }//End connect

  }//End else

});
