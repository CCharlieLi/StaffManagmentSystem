(function($) {
	$(document).ready(function() {	
		$.validator.addMethod("stringCheck", function(value, element) {       
			return this.optional(element) || /^[\u0391-\uFFE5\w]+$/.test(value);       
		}, "只能包括中文字、英文字母、数字和下划线"); 

		$("#login-form-wrap form").validate({
			// 字符验证       
			rules: {
				username: {
					required: true,
					stringCheck:true,   
					byteRangeLength:[3,15] 
				}, 

				password: {required: true}
			}, 

			messages: {
			    username: {       
           			required: "Account is required !", 
 				},
 				password: {       
           			required: "Password is required !", 
 				}
			    
			},

			//focusInvalid: false,
			//onkeyup: false,

			errorPlacement: function(error, element) {  
				//$("#errormessage").remove();
				//var tmp = "<div class=\"alert alert-error form-message\" id=\"errormessage\" style=\"cursor: pointer;\"><i class=\"icon-exclamation-sign\"></i>"+error.text()+"</div>";
				//$("#login-form-wrap").prepend(tmp);
				element.attr("value","");
				element.attr("placeholder",error.text());
				//error.appendTo($("#login-form-wrap"));

			}, 

			invalidHandler: function(form, validator) {
				if($.fn.effect) {
					$("#login-form").effect("shake", {distance: 6, times: 2}, 35);
				}
			}
		});
		
		$("html").css("background-image", "url('/static/manage/img/bgs/6.jpg')");
        var time = 0;
        $.extend({             
        	referesh: function () {            
				$("html").css("background-image", "url('/static/manage/img/bgs/"+ time%6 +".jpg')");
                time ++;
        }});
         
        timerID = setInterval("$.referesh()", 1000*60*5 );
        
		
	});
}) (jQuery);
