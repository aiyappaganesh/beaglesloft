$(document).ready(function(){
    var url = document.URL;
    if(url.indexOf('blog')!=-1) {
        $("#navbar-fluid").css({ opacity: 1 });
    }
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
            this.style.textDecoration="none";
            $(this).children().css({"color":"#fa7900"});
        } else if(accessed_page == this.href.substring(this.href.lastIndexOf('/'))) {
            this.style.textDecoration="none";
            $(this).children().css({"color":"#fa7900"});
        } else {
            this.style.textDecoration="none";
            $(this).children().css({"color":"#ffffff"});
        }
    });
}