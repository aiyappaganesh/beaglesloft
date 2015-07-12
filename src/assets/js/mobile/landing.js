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

    $('.service-container li').hover(
        function(){
            switchLinkIcon($(this), 'highlight_icon')
        },
        function(){
            if ($(this).hasClass("active")) {
                return;
            };
            switchLinkIcon($(this), 'icon');
        }
    );

    $('.service-container li').click(
        function(){
            var carousel_id = $(this).children('input[name="carousel_id"]').first().val();
            $('.service-carousel').fadeOut(0);
            $(carousel_id).fadeIn(0);
            $('.service-container li').each(
                function(){
                    $(this).removeClass('active');
                    switchLinkIcon($(this), 'icon');
                }
               );
            $(this).addClass('active');
            switchLinkIcon($(this), 'highlight_icon');
        }
    );
});

function switchLinkIcon(ele, icon){
    var highlight_icon = ele.children('input[name="' + icon + '"]').first().val();
    ele.children('a').css("background-image", "url(" + highlight_icon + ")");
}

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