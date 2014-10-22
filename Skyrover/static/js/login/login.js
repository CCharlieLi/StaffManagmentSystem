(function($) {
	$(document).ready(function() {	
		$("#login-form-wrap form").validate({
			rules: {
				username: {required: true}, 
				password: {required: true}
			}, 
			errorPlacement: function(error, element) {  
			}, 
			invalidHandler: function(form, validator) {
				if($.fn.effect) {
					$("#login-form").effect("shake", {distance: 6, times: 2}, 35);
				}
			}
		});
		
		$("html").css("background-image", "url('/static/img/bgs/6.jpg')");
        var time = 0;
        $.extend({             
        	referesh: function () {            
				$("html").css("background-image", "url('/static/img/bgs/"+ time%6 +".jpg')");
                time ++;
        }});
         
        timerID = setInterval("$.referesh()", 4000 );
        
		
	});
}) (jQuery);
