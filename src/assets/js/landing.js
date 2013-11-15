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
var startTime = null;
$(window).mousewheel(function(event, delta){
    event.preventDefault();
    if(startTime) {
        if(($.now() - startTime) < 1500) {
            return;
        }
    }
    if(acceptScroll) {
        totalDelta = totalDelta + delta;
        if(Math.abs(totalDelta) < 50) {
            return;
        } else {
            acceptScroll = false;
        }

        newSection = null;
        if (currentSectionNumber < 10 && delta < 0){
            newSectionNumber = currentSectionNumber+1;
            newSection = '#section'+newSectionNumber;
            if(newSectionNumber == 3 || newSectionNumber == 4 || newSectionNumber == 5) {
                $(newSection+'a').show().animate({top: "0px"}, 2000);
                $(newSection+'b').show().animate({top: "0px"}, 2000);
            }
            if(newSectionNumber != 4 && newSectionNumber != 5) {
                if(newSectionNumber > 5) {
                    $(newSection).fadeToggle();
                } else {
                    $(newSection).slideToggle();
                }
            }
            hideOldOnScrollDown(currentSectionNumber);
            currentSectionNumber = newSectionNumber;
        } else if (currentSectionNumber > 1 && delta > 0) {
            newSectionNumber = currentSectionNumber-1;
            newSection = '#section'+newSectionNumber;
            if(newSectionNumber == 3 || newSectionNumber == 4 || newSectionNumber == 5) {
                $(newSection+'a').show().animate({top: "0px"}, 2000);
                $(newSection+'b').show().animate({top: "0px"}, 2000);
            }
            if(newSectionNumber != 3 && newSectionNumber != 4) {
                if(currentSectionNumber == 6) {
                    $('#section'+3).fadeToggle();
                } else {
                    if(newSectionNumber > 5) {
                        $(newSection).fadeToggle();
                    } else {
                        $(newSection).slideToggle();
                    }
                }
            }
            hideOldOnScrollUp(currentSectionNumber);
            currentSectionNumber = newSectionNumber;
        }
        totalDelta = 0;
        acceptScroll = true;
        startTime = $.now();
    }
});

$(document).ready(function() {
    $(".nav-link").click( function(){
        $(".nav-link").each(function(){this.style.textDecoration="none"});
        this.style.textDecoration="overline";
        st_ind = this.href.indexOf('#');
        sec_num = parseInt(this.href.substring(st_ind+8));
        if(sec_num == currentSectionNumber) return;
        $('#section'+currentSectionNumber).slideToggle();
        $(this.href.substring(st_ind)).slideToggle();
        currentSectionNumber = sec_num;
    });
});

function hideOldOnScrollDown(currentSectionNumber) {
    oldSection = '#section'+currentSectionNumber;
    windowHeight = $(window).height();
    if(currentSectionNumber == 3 || currentSectionNumber == 5) {
        $(oldSection+'a').animate({top: -1*windowHeight}, 2000, function(){$(oldSection+'a').hide();});
        $(oldSection+'b').animate({top: windowHeight}, 2000, function(){$(oldSection+'b').hide();});
    } else if(currentSectionNumber == 4) {
        $(oldSection+'a').animate({top: windowHeight}, 2000, function(){$(oldSection+'a').hide();});
        $(oldSection+'b').animate({top: -1*windowHeight}, 2000, function(){$(oldSection+'b').hide();});
    }
    if(currentSectionNumber+1 != 4 && currentSectionNumber+1 != 5) {
        if(currentSectionNumber+1 == 6) {
            $('#section'+3).fadeToggle();
        } else {
            if(currentSectionNumber > 5) {
                $(oldSection).fadeToggle();
            } else {
                $(oldSection).slideToggle();
            }
        }
    }
}

function hideOldOnScrollUp(currentSectionNumber) {
    oldSection = '#section'+currentSectionNumber;
    windowHeight = $(window).height();
    if(currentSectionNumber == 3 || currentSectionNumber == 5) {
        $(oldSection+'a').animate({top: -1*windowHeight}, 2000, function(){$(oldSection+'a').hide();});
        $(oldSection+'b').animate({top: windowHeight}, 2000, function(){$(oldSection+'b').hide();});
    } else if(currentSectionNumber == 4) {
        $(oldSection+'a').animate({top: windowHeight}, 2000, function(){$(oldSection+'a').hide();});
        $(oldSection+'b').animate({top: -1*windowHeight}, 2000, function(){$(oldSection+'b').hide();});
    }
    if(currentSectionNumber-1 != 3 && currentSectionNumber-1 != 4) {
        if(currentSectionNumber > 5) {
            $(oldSection).fadeToggle();
        } else {
            $(oldSection).slideToggle();
        }
    }
}

$(document).ready(function() {
    $(window).on("resize load", resizeWindow);
});

function resizeWindow() {
    windowHeight = $(window).height();
    windowWidth = $(window).width();
    $("#landing").height(windowHeight);
    $(".quarter-height").height(windowHeight*0.25);
    $(".half-height").height(windowHeight*0.5);
    $(".three-quarter-height").height(windowHeight*0.75);
    $(".full-height").height(windowHeight);
    $(".one-fifth-height").height(windowHeight*0.2);
    $(".seven-tenth-height").height(windowHeight*0.7);
    $(".one-tenth-height").height(windowHeight*0.1);
    $(".section6a-top").height(windowHeight*0.3);
    $(".section6a-bottom").height(windowHeight*0.285);
    $(".section6b-top").height(windowHeight*0.203);
    $(".section6b-middle").height(windowHeight*0.714);
    $(".section6b-bottom").height(windowHeight*0.083);
    $(".section6b-middle-top").height(windowHeight*0.083);
    $(".section6b-middle-middle").height(windowHeight*0.548);
    $(".section6b-middle-bottom").height(windowHeight*0.083);
    $(".program-top").height(windowHeight*0.175);
    $(".program-middle").height(windowHeight*0.35);
    $(".program-bottom").height(windowHeight*0.175);
    $(".contact-top").height(windowHeight*0.175);
    $(".contact-middle").height(windowHeight*0.35);
    $(".contact-bottom").height(windowHeight*0.175);
    $(".all-the-way-up").css('top',-1*windowHeight);
    $(".all-the-way-down").css('top',windowHeight);
    $(".half-way-across").css('left',windowWidth/2);
}