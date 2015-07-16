
$(document).ready(function(){
	$('#starting-animation-bg .centered-fullscreen').fadeOut(4000, function(){ $('#starting-animation-bg').remove(); });
	/*
    $('#starting-animation-bg').delay(20000).queue(
        function(){
            $(this).remove();
        }
    );
	*/
});