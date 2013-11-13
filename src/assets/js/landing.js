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
var acceptScroll = true;
$(window).mousewheel(function(event, delta){
    event.preventDefault();
    if(acceptScroll) {
        totalDelta = totalDelta + delta;
        if(Math.abs(totalDelta) < 500) {
            return;
        } else {
            acceptScroll = false;
        }
        oldSection = '#section'+currentSectionNumber;
        newSection = null;
        if (currentSectionNumber < 10 && delta < 0){
            newSection = '#section'+(currentSectionNumber+1);
            if(currentSectionNumber+1 == 3 || currentSectionNumber+1 == 4 || currentSectionNumber+1 == 5) {
                $(newSection+'a').show().animate({top: "0px"}, 2000, function() {});
                $(newSection+'b').show().animate({top: "0px"}, 2000);
            }
            if(currentSectionNumber+1 != 4 && currentSectionNumber+1 != 5) {
                $(newSection).slideToggle();
            }
            hideOldOnScrollDown(currentSectionNumber);
            currentSectionNumber = currentSectionNumber + 1;
        } else if (currentSectionNumber > 1 && delta > 0) {
            newSection = '#section'+(currentSectionNumber-1);
            if(currentSectionNumber-1 == 3 || currentSectionNumber-1 == 4 || currentSectionNumber-1 == 5) {
                $(newSection+'a').show().animate({top: "0px"}, 2000);
                $(newSection+'b').show().animate({top: "0px"}, 2000);
            }
            if(currentSectionNumber-1 != 3 && currentSectionNumber-1 != 4) {
                if(currentSectionNumber == 6) {
                    $('#section'+3).slideToggle();
                } else {
                    $(newSection).slideToggle();
                }
            }
            hideOldOnScrollUp(currentSectionNumber);
            currentSectionNumber = currentSectionNumber - 1;
        }
        totalDelta = 0;
        acceptScroll = true;
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

function hideOldOnScrollDown(currentSectionNumber) {
    windowHeight = $(window).height();
    if(currentSectionNumber == 3 || currentSectionNumber == 5) {
        $(oldSection+'a').animate({top: -1*windowHeight}, 2000);
        $(oldSection+'b').animate({top: windowHeight}, 2000);
    } else if(currentSectionNumber == 4) {
        $(oldSection+'a').animate({top: windowHeight}, 2000);
        $(oldSection+'b').animate({top: -1*windowHeight}, 2000);
    }
    if(currentSectionNumber+1 != 4 && currentSectionNumber+1 != 5) {
        if(currentSectionNumber+1 == 6) {
            $('#section'+3).slideToggle();
        } else {
            $(oldSection).slideToggle();
        }
    }
}

function hideOldOnScrollUp(currentSectionNumber) {
    windowHeight = $(window).height();
    if(currentSectionNumber == 3 || currentSectionNumber == 5) {
        $(oldSection+'a').animate({top: -1*windowHeight}, 2000);
        $(oldSection+'b').animate({top: windowHeight}, 2000);
    } else if(currentSectionNumber == 4) {
        $(oldSection+'a').animate({top: windowHeight}, 2000);
        $(oldSection+'b').animate({top: -1*windowHeight}, 2000);
    }
    if(currentSectionNumber-1 != 3 && currentSectionNumber-1 != 4) {
        $(oldSection).slideToggle();
    }
}

$(document).ready(function() {
    $(window).on("resize load", resizeWindow);
});

function resizeWindow() {
    windowHeight = $(window).height();
    windowWidth = $(window).width();
    $(".quarter-height").height(windowHeight*0.25);
    $(".half-height").height(windowHeight*0.5);
    $(".three-quarter-height").height(windowHeight*0.75);
    $(".full-height").height(windowHeight);
    $(".section6a-top").height(windowHeight*0.214);
    $(".section6a-bottom").height(windowHeight*0.285);
    $(".section6b-top").height(windowHeight*0.143);
    $(".section6b-bottom").height(windowHeight*0.357);
    $(".all-the-way-up").css('top',-1*windowHeight);
    $(".all-the-way-down").css('top',windowHeight);
    $(".half-way-across").css('left',windowWidth/2);
}