$(document).ready(function(){
    $('.learn-more-button').mouseover(function(){
        $(this).animate({'background-color':'#FF0017 !important','color':'#ffffff'},500);
    });
    $('.learn-more-button').mouseout(function(){
        $(this).animate({'background-color':'transparent','color':'#FF0017'},500);
    });
});