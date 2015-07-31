
$(document).ready(function(){
	$('#starting-animation-bg .centered-fullscreen .logo-container').fadeIn(2000, function() {
		$('#starting-animation-bg .centered-fullscreen').fadeOut(2000, function() {
			$('#starting-animation-bg').remove();
		});	
	});

	$('.tab_icon').click(function(){	
		console.log();
        var carousel_id = $(this).children('input[name="carousel_id"]').first().val();
        $('.service-carousel').fadeOut(0);
        $(carousel_id).fadeIn(0);
    });
});    