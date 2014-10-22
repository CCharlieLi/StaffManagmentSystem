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
		
		 // bg switcher
            var $btns = $(".bg-switch .bg");
            $btns.click(function (e) {
                e.preventDefault();
                $btns.removeClass("active");
                $(this).addClass("active");
                var bg = $(this).data("img");

                $("html").css("background-image", "url('/static/img/bgs/" + bg + "')");
            });
		
	});
}) (jQuery);