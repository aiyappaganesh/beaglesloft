$(document).ready(function(){
    var url = document.URL;
    var current_page = '';
    var current_last_index = document.URL.lastIndexOf('#');
    if(current_last_index == -1) {
        current_page = document.URL.substring(document.URL.lastIndexOf('/'));
    } else {
        current_page = document.URL.substring(document.URL.lastIndexOf('/'),current_last_index);
    }
    if(current_page == '/') return;
    $('#navbar-fluid').css('background-color','rgba(48,46,46,1)');
    $('#navbar-fluid a').css('color','#adacac');
    $('#navbar-logo').attr('src','/assets/img/landing/beagles-logo.png');
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