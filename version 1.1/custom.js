$(document).ready(function() {
	var editor = ace.edit("editor");
    editor.setTheme("ace/theme/chrome");
    editor.session.setMode("ace/mode/c_cpp");
    document.getElementById('editor').style.fontSize='16px';
    editor.setValue('#include <stdio.h> \n\nint main(){\n\n\tprintf("yes");\n\treturn 0;\n}');
    
  if(!("WebSocket" in window)){
  $('#chat').fadeOut("fast");
  $('<p>Oh no, you need a browser that supports WebSockets. How about <a href="http://www.google.com/chrome">Google Chrome</a>?</p>').appendTo('#container');
  }else{
      //The user has WebSockets

      connect();

      function connect(){
          var socket;
          var host = "ws://localhost:8000";

          try{
              var socket = new WebSocket(host);

              //message('<p class="event">Socket Status: '+socket.readyState);

              socket.onopen = function(){
              	alert("Connected");
             	 //message('<p class="event">Socket Status: '+socket.readyState+' (open)');
              }

              socket.onmessage = function(msg){
              	//console.log(msg.data);
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
            $('.terminal').append(msg);
          }

          $('.run').on('click',function(event) {
          		if(socket.readyState==socket.CLOSED || socket.readyState==socket.CLOSING){
          			alert("You are not connected to the server. Please refresh your page");
          			return;
          		}
          		else{
          			event.preventDefault();
          			var text = editor.getValue();
          			$('.terminal').empty()
          			if(text==""){
                  		terminal('Please enter a message');
                  		return ;
              		}
              		else{
              			send(text);
              	  	}	
          	}
          		
          });	
          $('.reset').on('click',function(event) {
          		event.preventDefault();
               editor.setValue('#include <stdio.h> \n\nint main(){\n\n\tprintf("yes");\n\treturn 0;\n}');
          });
          $('.dsc').on('click',function(event) {
          		event.preventDefault();
          		socket.close();

          	});
          $('.resume').on('click',function(event) {
          		if(socket.readyState==socket.CLOSED || socket.readyState==socket.CLOSING){
          			alert("You are not connected to the server. Please refresh your page");
          			return;
          		}
          		else{
          		event.preventDefault();
          		var signal = "resume,!!";
          		$('.terminal').empty();
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
          		$('.terminal').empty();
          		send(signal);}
          });

      }//End connect

  }//End else

});
