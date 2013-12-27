
$(document).ready(function(){
    $(window).scroll(function(){
        var section1_top = $('#section1').offset().top;
        //var section2_top = $('#section2').offset().top;
        //var section3_top = $('#section3').offset().top;
        //var section4_top = $('#section4').offset().top;
        //var section5_top = $('#section5').offset().top;
        //var section6_top = $('#section6').offset().top;
        //var section7_top = $('#section7').offset().top;
        //var section8_top = $('#section8').offset().top;
        //var section9_top = $('#section9').offset().top;
        //var section10_top = $('#section10').offset().top;

        var window_top = $(window).scrollTop();
        var window_middle = $(window).scrollTop()+($(window).height() * 0.5);

        if(section1_top < window_middle && section1_top >= window_top) {
            highlightSection('#section1');
        } /*else if(section2_top < window_middle && section2_top >= window_top) {
            highlightSection('#section2');
        } else if(section3_top < window_middle && section3_top >= window_top) {
            highlightSection('#section2');
        } else if(section4_top < window_middle && section4_top >= window_top) {
            highlightSection('#section2');
        } else if(section5_top < window_middle && section5_top >= window_top) {
            highlightSection('#section2');
        } else if(section6_top < window_middle && section6_top >= window_top) {
            highlightSection('#section2');
        } else if(section7_top < window_middle && section7_top >= window_top) {
            highlightSection('#section7');
        } else if(section8_top < window_middle && section8_top >= window_top) {
            highlightSection('#section8');
        } else if(section9_top < window_middle && section9_top >= window_top) {
            highlightSection('#section9');
        } else if(section10_top < window_middle && section10_top >= window_top) {
            highlightSection('#section10');
        }*/
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
    //$('#navbar-fluid').hide();
    $('#logo').fadeIn(1000, function(){
            $('#landing-logo').fadeOut(2000, function(){
                //$('#navbar-fluid').fadeIn(2000);
                $('#landing-main').fadeIn(2000, function() {
                    scrollTo(document.URL);
                })
            })
        });
});