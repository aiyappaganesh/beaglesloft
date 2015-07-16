
$(document).ready(function(){
    $('#starting-animation-bg').delay(4000).queue(
        function(){
            $(this).remove();
            $('#landing-carousel').append();
        }
    );
});