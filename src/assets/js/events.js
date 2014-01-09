$(document).ready(function(){
    $('.learn-more-button').mouseover(function(){
        $(this).animate({'background-color':'#FF0017 !important','color':'#ffffff'},250);
    });
    $('.learn-more-button').mouseout(function(){
        $(this).animate({'background-color':'transparent','color':'#FF0017'},250);
    });
});

function showPage(page) {
    $('.page-select').each(function(){
        $(this).css('color','#c62530');
    });
    $('.tab-page').each(function(){
        $(this).fadeOut(500);
    });
    $('#' + page + '-select').css('color','#9c9c9c');
    $('#' + page + '-page').fadeIn(1500);
}