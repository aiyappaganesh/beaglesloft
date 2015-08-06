$(document).ready(function(){
    var url = document.URL;
    if(url.indexOf('blog')!=-1) {
        $("#navbar-fluid").css({ opacity: 1 });
    }
    $('.centered-full-width-element').width($(window).width());
    $('.tab_icons .tab').click(
        function(){
            var carousel_id = $(this).children('input[name="carousel_id"]').first().val();
            $('.active_tab').removeClass('first_icon');
            $('.active_tab h3').css('color', '');
            var icon_url = $('.active_tab #icon_url').val()
            $('.active_tab a #icon').attr('src', icon_url);
            $('.active_tab').removeClass('active_tab');
            $(carousel_id + '_tab').addClass('active_tab');
            var highlight_icon_url = $(carousel_id +'_tab #highlight_icon_url').val();
            $(carousel_id + '_tab a img').attr('src', highlight_icon_url)
            $(carousel_id + '_tab h3').css('color', '#000000');
            $('.service-carousel').fadeOut(0);
            $(carousel_id).fadeIn(0);
        }
    );
    $(function () {
        $('[data-toggle="popover"]').popover()
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
    var link_st_ind = link.lastIndexOf('/');
    var link_hash_ind = link.indexOf('#');
    var accessed_page = link.substring(link_st_ind, link_hash_ind);
    if(link_hash_ind == -1) {
        accessed_page = link.substring(link_st_ind);
    }
    $(".nav-link").each(function(){
        var st_ind = this.href.lastIndexOf('/');
        var hash_ind = this.href.indexOf('#');
        var curr_link_page = this.href.substring(st_ind, hash_ind);
        if(hash_ind == -1) {
            curr_link_page = this.href.substring(st_ind);
        }
        if(curr_link_page == accessed_page) {
            this.style.textDecoration="none";
            $(this).children().css({"color":"#fa7900"});
            $(this).css({"color":"#ffffff"});
        } else {
            this.style.textDecoration="none";
            $(this).children().css({"color":"#ffffff"});
            $(this).css({"color":"#adacac"});
        }
    });
}