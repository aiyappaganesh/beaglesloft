
$(document).ready(function(){
	$('#starting-animation-bg .centered-fullscreen .logo-container').fadeIn(2000, function() {
		$('#starting-animation-bg .centered-fullscreen').fadeOut(2000, function() {
			$('#starting-animation-bg').remove();
		});	
	});
});