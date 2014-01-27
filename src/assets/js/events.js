$(document).ready(function(){
    $('.learn-more-button').mouseover(function(){
        $(this).css({'background-color':'#FF0017 !important','color':'#ffffff'});
    });
    $('.learn-more-button').mouseout(function(){
        $(this).css({'background-color':'transparent','color':'#FF0017'});
    });
});

function showPage(page) {
    ga('send', 'event', 'Events Page', 'click', page + ' Clicked');
    $('.page-select').each(function(){
        $(this).css('color','#c62530');
    });
    $('.tab-page').each(function(){
        $(this).fadeOut(500);
    });
    $('#' + page + '-select').css('color','#9c9c9c');
    $('#' + page + '-page').fadeIn(1500);
}