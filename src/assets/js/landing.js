
$(document).ready(function(){

    /*$(window).scroll(function(){
        var section1_top = $('#section1-carousel').offset().top;

        var window_top = $(window).scrollTop();
        var window_middle = $(window).scrollTop()+($(window).height() * 0.5);

        if(section1_top < window_middle && section1_top >= window_top) {
            highlightSection('#section1-carousel');
        }
    });*/

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
	$('#starting-animation-bg .centered-fullscreen .logo-container').fadeIn(2000, function() {
		$('#starting-animation-bg .centered-fullscreen').fadeOut(2000, function() {
			$('#starting-animation-bg').remove();
			$('#section1-carousel').carousel('cycle');
			$('.content-page').css('overflow-y','scroll');
		});
	});
});

/*$('#section1-carousel').on('slide.bs.carousel', function () {
    $('#slide-copy').fadeTo(200,0);
});*/

/*$('#section1-carousel').on('slid.bs.carousel', function () {
    $('#slide-copy').text($($('.carousel-inner .active').find('input')[0]).val());
    $('#slide-copy').fadeTo(200,1);
});*/

$('#section1-carousel').on('slide.bs.carousel', function(e){
    $(this).find('.section1-heading').fadeOut(500);
    $('#'+e.relatedTarget.id+'-copy').fadeIn(500);
});

function highlightSection(section) {
    $(".nav-link").each(function(){
        st_ind = this.href.indexOf('#');
        if(this.href.substring(st_ind) == section) {
            this.style.textDecoration="overline";
        } else {
            this.style.textDecoration="none";
        }
    });
}

function showServiceHighlightIcon(e) {
    $(e).find('.no-hover').fadeOut(0);
    $(e).find('.on-hover').fadeIn(0);
}

function hideServiceHighlightIcon(e) {
    $(e).find('.on-hover').fadeOut(0);
    $(e).find('.no-hover').fadeIn(0);
}

$(window).load(function(){
    var url = document.URL;
    var accessed_page_section = url.substring(url.lastIndexOf('/'));
    if(accessed_page_section != '/') {
        $('#starting-animation-bg').remove();
		$('#section1-carousel').carousel('cycle');
		$('.content-page').css('overflow-y','scroll');
        return;
    }
});