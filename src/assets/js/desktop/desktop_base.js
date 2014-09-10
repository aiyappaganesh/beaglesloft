$(document).ready(function(){
    $('.content-page').scroll( function(){
        var top_of_window = $('.content-page').scrollTop();
        var show_navbar = ($('.content-page').height() * 0.1);
        var current_page = getCurrentPage();

        if(top_of_window > show_navbar) {
            $("#navbar-fluid").css({ opacity: 1 });
            $('#navbar-fluid').css({'-webkit-transform':'translateY(0%)', 'transform':'translateY(0%)'});
        } else if(document.URL.indexOf('blog')==-1){
            var curr_opacity = (top_of_window)/(show_navbar);
            $("#navbar-fluid").css({ opacity: curr_opacity });$('#navbar-fluid').css({'-webkit-transform':'translateY(-100%)', 'transform':'translateY(-100%)'});
        }
    });
});