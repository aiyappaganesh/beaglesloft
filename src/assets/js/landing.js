
$(document).ready(function(){
	$('#starting-animation-bg .centered-fullscreen .logo-container').fadeIn(2000, function() {
		$('#starting-animation-bg .centered-fullscreen').fadeOut(2000, function() {
			$('#starting-animation-bg').remove();
		});	
	});

	$('.tab_icon').on('touchend click', function(){	
        var carousel_id = $(this).children('input[name="carousel_id"]').first().val();
        $('.active_tab').removeClass('first_icon');
        $('.active_tab h3').css('color', '');
        var icon_url = $('.active_tab #icon_url').val()
        $('.active_tab a #icon').attr('src', icon_url);
        $('.active_tab').removeClass('active_tab');
        $(carousel_id + '_tab').addClass('active_tab');
        var highlight_icon_url = $(carousel_id +'_tab #highlight_icon_url').val();
        $(carousel_id + '_tab a img').attr('src', highlight_icon_url)
        $(carousel_id + '_tab h3').css('color', '#000000');                    
        $('.service-carousel').fadeOut(0);
        $(carousel_id).fadeIn(0);
    });
});    