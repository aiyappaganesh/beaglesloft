$(document).ready(function(){
    var url = document.URL;
    if(url.indexOf('blog')!=-1) {
        $("#navbar-fluid").css({ opacity: 1 });
    }
    /*var current_page = getCurrentPage();
    if(current_page == '/') {
        $("#navbar-fluid").css({ 'position':'absolute', '-webkit-transform': 'translateY(0%)', 'transform': 'translateY(0%)' });
        $('#navbar-logo').attr('src','/assets/img/landing/beagles-logo-black.png');
    }*/
});

$(document).ready(function() {
    $(window).scroll( function(){
        var top_of_window = $(window).scrollTop();
        var show_navbar = ($(window).height() * 0.1);
        var current_page = getCurrentPage();

        if(top_of_window > show_navbar) {
            $("#navbar-fluid").css({ opacity: 1 });
            $('#navbar-fluid').css({'-webkit-transform':'translateY(0%)', 'transform':'translateY(0%)'});
        } else if(document.URL.indexOf('blog')==-1){
            var curr_opacity = (top_of_window)/(show_navbar);
            $("#navbar-fluid").css({ opacity: curr_opacity });
            $('#navbar-fluid').css({'-webkit-transform':'translateY(-100%)', 'transform':'translateY(-100%)'});
        }

        /*if(current_page == '/') {
            $("#navbar-fluid").css({ opacity: 1 });
            var welcome_top = $('#welcome').offset().top;
            if(top_of_window >= (welcome_top-70)) {
                $('#navbar-fluid').css('position','fixed');
                $('#navbar-logo').attr('src','/assets/img/landing/beagles-logo-nav.png');
                $('.navbar-inner').css('background-color','transparent');
                $('.nav>li>a').css('color','#adacac');
                $('.nav-bg').css({'-webkit-transform':'translateY(0%)', 'transform':'translateY(0%)'});
            } else {
                $('#navbar-fluid').css('position','absolute');
                $('#navbar-logo').attr('src','/assets/img/landing/beagles-logo-black.png');
                $('.navbar-inner').css('background-color','transparent');
                $('.nav>li>a').css('color','#000000');
                $('.nav-bg').css({'-webkit-transform':'translateY(-100%)', 'transform':'translateY(-100%)'});
            }
        } else {
            if(top_of_window > show_navbar) {
                $("#navbar-fluid").css({ 'opacity':'1', '-webkit-transform':'translateY(0%)', 'transform':'translateY(0%)' });
            } else if(document.URL.indexOf('blog')==-1){
                var curr_opacity = (top_of_window)/(show_navbar);
                $("#navbar-fluid").css({ 'opacity': curr_opacity, '-webkit-transform': 'translateY(-100%)', 'transform': 'translateY(-100%)' });
            }
        }*/
    });
});

$(document).ready(function() {
    $(".nav-link").click( function(event){
        var current_page = '';
        var current_last_index = document.URL.lastIndexOf('#');
        if(current_last_index == -1) {
            current_page = document.URL.substring(document.URL.lastIndexOf('/'));
        } else {
            current_page = document.URL.substring(document.URL.lastIndexOf('/'),current_last_index);
        }

        var new_page = '';
        var new_last_index = this.href.lastIndexOf('#');
        if(new_last_index == -1) {
            new_page = this.href.substring(this.href.lastIndexOf('/'));
        } else {
            new_page = this.href.substring(this.href.lastIndexOf('/'),new_last_index);
        }

        if (current_page == new_page) {
            event.preventDefault();
            scrollTo(this.href);
        }
    });
});

$(document).ready(function() {
    var url = document.URL;
    highlightLink(url);
});

function getCurrentPage() {
    var url = document.URL;
    var current_page = '';
    var current_last_index = url.lastIndexOf('#');
    if(current_last_index == -1) {
        current_page = url.substring(url.lastIndexOf('/'));
    } else {
        current_page = url.substring(url.lastIndexOf('/'),current_last_index);
    }
    return current_page;
}

function highlightLink(link) {
    var accessed_page = link.substring(link.lastIndexOf('/'));
    link_st_ind = link.indexOf('#section');
    $(".nav-link").each(function(){
        st_ind = this.href.indexOf('#');
        if((st_ind != -1) && (this.href.substring(st_ind) == link.substring(link_st_ind))) {
            this.style.textDecoration="overline";
        } else if(accessed_page == this.href.substring(this.href.lastIndexOf('/'))) {
            this.style.textDecoration="overline";
        } else {
            this.style.textDecoration="none";
        }
    });
}

function scrollTo(link) {
    var link_st_ind = link.lastIndexOf('/');
    smoothScrollTo(link.substring(link_st_ind+1));
}

function smoothScrollTo(link) {
    $.smoothScroll({
        scrollTarget: link,
        speed: 2000,
        preventDefault: true
    });
}

$(document).ready(function() {
    //$(window).on("load", resizeWindow);
});

function resizeWindow() {
    windowHeight = $(window).height();
    windowWidth = $(window).width();
    $(".quarter-height").height(windowHeight*0.25);
    $(".half-height").height(windowHeight*0.5);
    $(".three-quarter-height").height(windowHeight*0.75);
    $(".full-height").height(windowHeight);
    $(".one-fifth-height").height(windowHeight*0.2);
    $(".seven-tenth-height").height(windowHeight*0.7);
    $(".one-tenth-height").height(windowHeight*0.1);
    $(".one-sixth-height").height(windowHeight*0.167);
    $(".one-twelfth-height").height(windowHeight*0.083);
    $(".values-height").height(windowHeight*1.0);

    //Element Sizes
    s1mh = 43 + ((1280-windowWidth) * 0.029167);
    s1mh = Math.max(43,s1mh);
    s1mh = Math.min(71,s1mh);
    $(".section1-message").css('height',s1mh+'%');
    s1ih = 57 - ((1280-windowWidth) * 0.029167);
    s1ih = Math.max(29, s1ih);
    s1ih = Math.min(57, s1ih);
    $(".section1-image").css('height',s1ih+'%');
    $(".section1-img").css('height','100%');


    $(".section6a-top").height(windowHeight*0.3);
    $(".section6a-bottom").height(windowHeight*0.285);
    $(".section6b-top").height(windowHeight*0.203);
    $(".section6b-middle").height(windowHeight*0.714);
    $(".section6b-bottom").height(windowHeight*0.083);
    $(".section6b-middle-top").height(windowHeight*0.083);
    $(".section6b-middle-middle").height(windowHeight*0.548);
    $(".section6b-middle-bottom").height(windowHeight*0.010);
    $(".program-top").height(windowHeight*0.1875);
    $(".program-middle").height(windowHeight*0.375);
    $(".program-bottom").height(windowHeight*0.1875);
    $(".people-top").height(windowHeight*0.1875);
    $(".people-middle").height(windowHeight*0.515);
    $(".people-bottom").height(windowHeight*0.0475);
    $(".people-detail-1").height(windowHeight*0.14375);
    $(".people-detail-1-top").height(windowHeight*0.030975);
    $(".people-detail-1-bottom").height(windowHeight*0.071875);
    $(".people-detail-2").height(windowHeight*0.1);
    $(".people-detail-3").height(windowHeight*0.4125);
    $(".people-desc").height(windowHeight*0.4125*0.6);
    $(".people-desc-gap").height(windowHeight*0.4125*0.1);
    $(".people-scores").height(windowHeight*0.4125*0.3);
    $(".people-detail-4").height(windowHeight*0.09375);
    $(".contact-top").height(windowHeight*0.1875);
    $(".contact-middle").height(windowHeight*0.375);
    $(".contact-bottom").height(windowHeight*0.1875);
    $(".people-margin-top").height(windowHeight/6.936);
    $(".people-container").height(windowHeight/1.238);
    $(".people-container").width(windowWidth/1.544);
    $(".people-margin-bottom").height(windowHeight/20.807);

    //Set font-sizes
    $(".section1_heading").css('font-size',windowWidth/30.476);
    $(".section1_text").css('font-size',windowWidth/58.18);
    $(".section_text").css('font-size',windowWidth/80);
    $(".section2_text").css('font-size',windowWidth/40);
    $(".section3_heading").css('font-size',windowWidth/38.78);
    $(".section6_left_text").css('font-size',windowWidth/45.71);
    $(".section6_right_heading").css('font-size',windowWidth/35.56);
    $(".section6_right_text").css('font-size',windowWidth/80);
    $(".program-time").css('font-size',windowWidth/80);
    $(".program-heading").css('font-size',windowWidth/53.33);
    $(".program-desc").css('font-size',windowWidth/98.46);
    $(".people-designation").css('font-size',windowWidth/91.43);
    $(".people-name").css('font-size',windowWidth/42.67);
    $(".people-website").css('font-size',windowWidth/91.43);
    $(".people-twitter-handle").css('font-size',windowWidth/91.43);
    $(".people-desc").css('font-size',windowWidth/70);
    $(".people-score-name").css('font-size',windowWidth/64);
    $(".calendar-text").css('font-size',windowWidth/67.368);

    //Set line-height
    $(".section1_text").css('line-height',(windowWidth/49.23)+'px');
    $(".section_text").css('line-height',(windowWidth/42.67)+'px');
    $(".section2_text").css('line-height',(windowWidth/32)+'px');
    $(".people-desc").css('line-height',(windowWidth/42.66)+'px');

    //Set Margin
    //$(".people-picture").css('margin',windowWidth/256);
    $(".progress").css('margin-bottom',windowWidth/426.67);
    $(".progress").css('margin-top',windowWidth/213.33);

    //Set dimensions
    $(".progress").css('height',windowWidth/64);
    $(".people-score-name").css('height',windowWidth/64);
}