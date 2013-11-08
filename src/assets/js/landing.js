/*$(document).ready(function() {
    $(window).scroll( function(){
        var top_of_window = $(window).scrollTop();
        var section_number = Math.ceil(top_of_window/1000);
        var section = '#section'+section_number;
        var next_section = '#section'+(section_number+1);
        var new_y = -1 * (top_of_window%1000);
        $(section).css({ 'background-position-y': new_y});
        //$(next_section).css({ 'background-position-y': new_y+(section_number * 1000)});
    });
});*/

/*$(document).ready(function() {
    $("#landing section").each(function() {
        var section_name = this.id;
        console.log(section_name);
        var len = section_name.length;
        var page = section_name.substring(len-1,len);
        console.log(page);
        $(this).css({ 'top': (page-1)*1000});
    });
});*/

function smoothScrollTo(event, link) {
    event.preventDefault();
    $.smoothScroll({
        scrollTarget: link,
        speed: 2000,
        preventDefault: true
    });
}