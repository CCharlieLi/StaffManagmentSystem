/* Form Messages */
	
		$(".form-message").live("click", function() {
			$(this).animate({opacity:0}, function() {
				$(this).slideUp("medium", function() {
					$(this).css("opacity", '');
				});
			});
		});