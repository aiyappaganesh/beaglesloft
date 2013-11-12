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

var currentSectionNumber = 1;
var totalDelta = 0;
$(window).mousewheel(function(event, delta){
    event.preventDefault();
    totalDelta = totalDelta + delta;
    if(Math.abs(totalDelta) < 400) {
        return;
    } else {
        totalDelta = 0;
    }
    oldSection = '#section'+currentSectionNumber;
    newSection = null;
    if (currentSectionNumber < 10 && delta < 0){
        newSection = '#section'+(currentSectionNumber+1);
        if(currentSectionNumber == 3 || currentSectionNumber == 4 || currentSectionNumber == 5) {
            $(oldSection+'a').animate({top: "-700px"}, 2000).hide();
            $(oldSection+'b').animate({top: "700px"}, 2000).hide();
        }
        $(oldSection).slideToggle();
        if(currentSectionNumber+1 == 3 || currentSectionNumber+1 == 4 || currentSectionNumber+1 == 5) {
            $(newSection+'a').show().animate({top: "0px"}, 2000);
            $(newSection+'b').show().animate({top: "0px"}, 2000);
        }
        $(newSection).slideToggle();
        currentSectionNumber = currentSectionNumber + 1;
    } else if (currentSectionNumber > 1 && delta > 0) {
        newSection = '#section'+(currentSectionNumber-1);
        if(currentSectionNumber == 3 || currentSectionNumber == 4 || currentSectionNumber == 5) {
            $(oldSection+'a').animate({top: "-700px"}, 2000).hide();
            $(oldSection+'b').animate({top: "700px"}, 2000).hide();
        }
        $(oldSection).slideToggle();
        if(currentSectionNumber-1 == 3 || currentSectionNumber-1 == 4 || currentSectionNumber-1 == 5) {
            $(newSection+'a').show().animate({top: "0px"}, 2000);
            $(newSection+'b').show().animate({top: "0px"}, 2000);
        }
        $(newSection).slideToggle();
        currentSectionNumber = currentSectionNumber - 1;
    }
});

$(document).ready(function() {
    $(".nav-link").click( function(){
        st_ind = this.href.indexOf('#');
        sec_num = this.href.substring(st_ind+8);
        if(sec_num == currentSectionNumber) return;
        $('#section'+currentSectionNumber).slideToggle();
        $(this.href.substring(st_ind)).slideToggle();
        currentSectionNumber = sec_num;
    });
});