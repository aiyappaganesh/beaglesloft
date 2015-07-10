$(document).ready(function() {
   $("#section3-carousel").on("swiperight", function() {
      $("#section3-carousel").carousel('prev');
    });
   $("#section3-carousel").on("swipeleft", function() {
      $("#section3-carousel").carousel('next');
   });

   $('#signup-form').submit(function(e) {
        e.preventDefault();
        $('#signup-message').fadeOut();
        var email = $('#signup-email').val();
        if(email) {
            $.post('/api/members/add_email',{'email':email});
            $('#signup-message').fadeIn();
        } else {
            $('#signup-email').focus();
        }
        $('#signup-email').val('');
    });
});

function showServiceCarousel(id) {
    $('.service-carousel').fadeOut(0);
    $(id).fadeIn(0);
}

function showServiceHighlightIcon(e) {
    $(e).find('.no-hover').fadeOut(0);
    $(e).find('.on-hover').fadeIn(0);
}

function hideServiceHighlightIcon(e) {
    $(e).find('.on-hover').fadeOut(0);
    $(e).find('.no-hover').fadeIn(0);
}