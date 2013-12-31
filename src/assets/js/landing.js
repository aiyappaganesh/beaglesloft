
$(document).ready(function(){
    $(window).scroll(function(){
        var section1_top = $('#section1').offset().top;

        var window_top = $(window).scrollTop();
        var window_middle = $(window).scrollTop()+($(window).height() * 0.5);

        if(section1_top < window_middle && section1_top >= window_top) {
            highlightSection('#section1');
        }
    });
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

$(document).ready(function(){
    var url = document.URL;
    var accessed_page_section = url.substring(url.lastIndexOf('/'));
    if(accessed_page_section != '/') {
        $('#landing-logo').hide(100, function(){$('#landing-main').show(0, function(){scrollTo(url)})});
        return;
    }
    $('#logo').fadeIn(1000, function(){
            $('#landing-logo').fadeOut(2000, function(){
                $('#landing-main').fadeIn(2000, function() {
                    scrollTo(document.URL);
                })
            })
        });
});