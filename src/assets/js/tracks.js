function showTrackPrograms(id){
    $('.track-program-listing').css('display', 'none');
    $(id).css('display', 'block');
}

var chevToggle = true;

function toggleChevron(e) {
    if($(e).hasClass('rotate-180')) {
        $(e).removeClass('rotate-180');
    } else {
        $(e).addClass('rotate-180');
    }
    chevToggle = true;
}

$('.collapse').on('show.bs.collapse', function() {
    if(chevToggle) {
        var glyph = $(this).parent().find('.glyphicon-chevron-down');
        chevToggle = false;
        toggleChevron(glyph);
    }
});

$('.collapse').on('hide.bs.collapse', function() {
    if(chevToggle) {
        var glyph = $(this).parent().find('.glyphicon-chevron-down');
        chevToggle = false;
        toggleChevron(glyph);
    }
});