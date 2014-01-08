var currentMemberIndex = 0;
var member_keys = [];
var currentPartner = 1;
var partnerCycleInterval = null;
var partnerTimeout = null;

$(document).ready(function() {
    member_keys = $('#member_keys').val().split(',');
    showMemberInfo(member_keys[0]);
});

$(document).ready(function(){
    $('.progress').hover(function(){$(this).addClass('progress-striped active')},function(){$(this).removeClass('progress-striped active')});
    $('.progress-bar').hover(function(){$(this).css('background-color','rgba(255,215,0,0.5)')},function(){$(this).css('background-color','rgba(199,36,48,1)')});
});

$(document).ready(function(){
    $("body").keydown(function(e) {
        if(e.keyCode == 37) { // left
            showPreviousMemberInfo();
        } else if(e.keyCode == 39) { // right
            showNextMemberInfo();
        }
    });
});

$(document).ready(function(){
    selectCurrentPartner();
});

$(document).ready(function(){
    setPartnerCycleTimer();
});

$(document).ready(function(){
    $(".partner-square").click(function(){
        window.clearInterval(partnerCycleInterval);
        selectPartner(this);
        window.clearTimeout(partnerTimeout);
        partnerTimeout = window.setTimeout(function(){
            setPartnerCycleTimer();
        }, 5000);
    });
});

function setPartnerCycleTimer() {
    window.clearInterval(partnerCycleInterval);
    partnerCycleInterval = window.setInterval(function(){
        selectCurrentPartner();
    },2500);
}

function selectCurrentPartner() {
    selectPartner($('#partner-'+currentPartner));
    currentPartner = currentPartner + 1;
    if(currentPartner == 5) {
        currentPartner = 1;
    }
}

function selectPartner(e) {
    $(".partner-square").each(function(){
        $(this).css('border','none');
    });
    $(e).css('border','5px solid #c62530');
    var value_str = $($(e).find('input')[0]).val();
    values = value_str.split(';');
    $(".partner-img").each(function(){
        $(this).css('display','none');
    });
    $('#partner-img-'+values[0]).css('display','block');
    $('#partner-website').text(values[1]);
    $('#partner-website').parent().attr('href','http://'+values[1]);
    $('#partner-desc').text(values[2]);
}

function showMemberInfo(key) {
    //$('#people-grid').fadeOut(10);
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
        if(data.image) {
            $('#picture').attr('src','/api/members/'+data.email+'/image');
        } else if(data.facebook_id) {
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
    //$('#people-detail').fadeIn(1000);
    currentMemberIndex = member_keys.indexOf(key);
    if(currentMemberIndex == -1) {currentMemberIndex = 0;}
    $('.people-picture').each(function(){
        $(this).css('border', 'none');
    });
    $('#people-'+(currentMemberIndex+1)).css('border', '5px solid #c62530');
    $('#people-'+(currentMemberIndex+1)).focus();
    $('#member-carousel').carousel(Math.floor(currentMemberIndex/7));
}

function showMemberGrid() {
    $('#people-detail').fadeOut(0);
    $('#people-grid').fadeIn(1000);
}

function showNextMemberInfo() {
    nextMemberIndex = currentMemberIndex+1;
    if(nextMemberIndex >= member_keys.length) {
        nextMemberIndex = 0;
    }
    showMemberInfo(member_keys[nextMemberIndex]);
}

function showPreviousMemberInfo() {
    nextMemberIndex = currentMemberIndex-1;
    if(nextMemberIndex < 0) {
        nextMemberIndex = member_keys.length-1;
    }
    showMemberInfo(member_keys[nextMemberIndex]);
}