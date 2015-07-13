
$(document).ready(function(){
    $(window).scroll(function(){
        var section1_top = $('#section1').offset().top;

        var window_top = $(window).scrollTop();
        var window_middle = $(window).scrollTop()+($(window).height() * 0.5);

        if(section1_top < window_middle && section1_top >= window_top) {
            highlightSection('#section1');
        }
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
                                            switchLinkIcon($(this), 'highlight_icon', 'black-font')
                                        },
                                        function(){
                                            if ($(this).hasClass("active")) {
                                                return
                                            };
                                            switchLinkIcon($(this), 'icon', 'red-font')
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
                                                                                switchLinkIcon($(this), 'icon', 'red-font');
                                                                            }
                                                                           );
                                            $(this).addClass('active');
                                            switchLinkIcon($(this), 'highlight_icon', 'black-font');
                                        }
                                    );
});

function switchLinkIcon(ele, icon, text_color){
    var highlight_icon = ele.children('input[name="' + icon + '"]').first().val();
    ele.children('a').css("background-image", "url(" + highlight_icon + ")");
    ele.children('h3').removeClass();
    ele.children('h3').addClass(text_color);
    ele.children('h3').addClass('uppercase');
    ele.children('h3').addClass('service-name');
}

/*$('#section1-carousel').on('slide.bs.carousel', function () {
    $('#slide-copy').fadeTo(200,0);
});*/

/*$('#section1-carousel').on('slid.bs.carousel', function () {
    $('#slide-copy').text($($('.carousel-inner .active').find('input')[0]).val());
    $('#slide-copy').fadeTo(200,1);
});*/

$('#section1-carousel').on('slide.bs.carousel', function(e){
    $(this).find('.section1_heading').fadeOut(500);
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
        $('#landing-logo').hide(function(){$('#landing-main').fadeIn(function(){
            $('#section1-carousel').carousel('cycle');
        })});
        return;
    }
    $('#landing-logo').fadeIn(1000, function(){
        $('#logo-img').fadeIn(1000, function(){
            $('#logo-msg').fadeIn(4000, function(){
                $('#logo').fadeOut(1000, function(){
                    $('#landing-logo').fadeOut(2000);
                    $('#landing-main').fadeIn(1500, function(){
                        //('.navbar-inner').css('background-color','transparent');
                        //$('.nav>li>a').css('color','#000000');
                        //$("#navbar-fluid").css({ 'opacity': '1' });
                        $('#section1-carousel').carousel('cycle');
                    });
                });
            });
        });
    });
});