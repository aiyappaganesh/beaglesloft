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