function smoothScrollTo(event, link) {
    event.preventDefault();
    $.smoothScroll({
        scrollTarget: link,
        speed: 2000,
        preventDefault: true
    });
}

var currentMemberIndex = 0;
var member_keys = [];

$(document).ready(function(){
    member_keys = $('#member_keys').val().split(',');
});

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
                if(newSectionNumber != 3 && newSectionNumber != 6) {
                    highlightSection(newSection);
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
                if(newSectionNumber == 6) {
                    highlightSection('#section'+2);
                } else if(newSectionNumber != 5 && newSectionNumber != 4 &&  newSectionNumber != 3) {
                    highlightSection(newSection);
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

function highlightSection(section) {
    $(".nav-link").each(function(){
        st_ind = this.href.indexOf('#');
        if(this.href.substring(st_ind) == section) {
            this.style.textDecoration="overline";
        } else {
            this.style.textDecoration="none";
        }
    });
}

$(document).ready(function() {
    $(window).on("load", resizeWindow);
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
    $(".one-sixth-height").height(windowHeight*0.167);
    $(".one-twelfth-height").height(windowHeight*0.083);
    $(".section6a-top").height(windowHeight*0.3);
    $(".section6a-bottom").height(windowHeight*0.285);
    $(".section6b-top").height(windowHeight*0.203);
    $(".section6b-middle").height(windowHeight*0.714);
    $(".section6b-bottom").height(windowHeight*0.083);
    $(".section6b-middle-top").height(windowHeight*0.083);
    $(".section6b-middle-middle").height(windowHeight*0.548);
    $(".section6b-middle-bottom").height(windowHeight*0.083);
    $(".program-top").height(windowHeight*0.1875);
    $(".program-middle").height(windowHeight*0.375);
    $(".program-bottom").height(windowHeight*0.1875);
    $(".people-top").height(windowHeight*0.1575);
    $(".people-middle").height(windowHeight*0.515);
    $(".people-bottom").height(windowHeight*0.0775);
    $(".people-detail-1").height(windowHeight*0.14375);
    $(".people-detail-1-top").height(windowHeight*0.030975);
    $(".people-detail-1-bottom").height(windowHeight*0.071875);
    $(".people-detail-2").height(windowHeight*0.1);
    $(".people-detail-3").height(windowHeight*0.4125);
    $(".people-desc").height(windowHeight*0.4125*0.6);
    $(".people-desc-gap").height(windowHeight*0.4125*0.1);
    $(".people-scores").height(windowHeight*0.4125*0.3);
    $(".people-detail-4").height(windowHeight*0.09375);
    $(".contact-top").height(windowHeight*0.1875);
    $(".contact-middle").height(windowHeight*0.375);
    $(".contact-bottom").height(windowHeight*0.1875);
    $(".all-the-way-up").css('top',-1*windowHeight);
    $(".all-the-way-down").css('top',windowHeight);
    $(".half-way-across").css('left',windowWidth/2);
}

function showMemberInfo(key) {
    $('#people-grid').fadeOut(10);
    $.post('/api/members/get_member',{email:key}).done(function(data){
        var desig_text = '';
        if(data.designation) {
            desig_text = data.designation;
        }
        if(desig_text != '') {
            desig_text = desig_text + ', ';
        }
        if(data.organization) {
            desig_text = desig_text + data.organization;
        }
        if(desig_text != '') {
            $('#designation').text(desig_text);
        }
        if(data.name) {
            $('#name').text(data.name);
        } else {
            $('#name').text('');
        }
        if(data.website) {
            $('#website').text(data.website);
        } else {
            $('#website').text('');
        }
        if(data.twitter_handle) {
            $('#twitter_handle').text(data.twitter_handle);
        } else {
            $('#twitter_handle').text('');
        }
        if(data.facebook_id) {
            $('#picture').attr('src','https://graph.facebook.com/'+data.facebook_id+'/picture?width=300&height=300');
        } else {
            $('#picture').attr('src','/assets/img/landing/default-user.gif');
        }
        if(data.bio) {
            $('#bio').text(data.bio);
        } else {
            $('#bio').text('');
        }
        if(data.influence_score) {
            $('#influence').css('width',data.influence_score+'%');
        } else {
            $('#influence').css('width',0+'%');
        }
        if(data.activity_score) {
            $('#activity').css('width',data.activity_score+'%');
        } else {
            $('#activity').css('width',0+'%');
        }
        if(data.proficiency_score) {
            $('#proficiency').css('width',data.proficiency_score+'%');
        } else {
            $('#proficiency').css('width',0+'%');
        }
    });
    $('#people-detail').fadeIn(1000);
    currentMemberIndex = member_keys.indexOf(key);
    if(currentMemberIndex == -1) {currentMemberIndex = 0;}
}

function showMemberGrid() {
    $('#people-detail').fadeOut(0);
    $('#people-grid').fadeIn(1000);
}

function showNextMemberInfo() {
    if((currentMemberIndex+1) < member_keys.length) {
        showMemberInfo(member_keys[currentMemberIndex+1]);
    }
}

function showPreviousMemberInfo() {
    if((currentMemberIndex-1) >= 0) {
        showMemberInfo(member_keys[currentMemberIndex-1]);
    }
}