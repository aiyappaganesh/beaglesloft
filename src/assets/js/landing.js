var currentMemberIndex = 0;
var member_keys = [];

$(document).ready(function() {
    $(window).on("load", resizeWindow);
    member_keys = $('#member_keys').val().split(',');
});

$(document).ready(function(){
    $('.progress').hover(function(){$(this).addClass('progress-striped active')},function(){$(this).removeClass('progress-striped active')});
    $('.progress-bar').hover(function(){$(this).css('background-color','rgba(255,215,0,0.5)')},function(){$(this).css('background-color','rgba(0,0,0,0.5)')});
});

$(document).ready(function(){
    $(window).scroll(function(){
        var section1_top = $('#section1').offset().top;
        var section2_top = $('#section2').offset().top;
        var section3_top = $('#section3').offset().top;
        var section4_top = $('#section4').offset().top;
        var section5_top = $('#section5').offset().top;
        var section6_top = $('#section6').offset().top;
        var section7_top = $('#section7').offset().top;
        var section8_top = $('#section8').offset().top;
        var section9_top = $('#section9').offset().top;
        var section10_top = $('#section10').offset().top;

        var window_top = $(window).scrollTop();
        var window_middle = $(window).scrollTop()+($(window).height() * 0.5);

        if(section1_top < window_middle && section1_top >= window_top) {
            highlightSection('#section1');
        } else if(section2_top < window_middle && section2_top >= window_top) {
            highlightSection('#section2');
        } else if(section3_top < window_middle && section3_top >= window_top) {
            highlightSection('#section2');
        } else if(section4_top < window_middle && section4_top >= window_top) {
            highlightSection('#section2');
        } else if(section5_top < window_middle && section5_top >= window_top) {
            highlightSection('#section2');
        } else if(section6_top < window_middle && section6_top >= window_top) {
            highlightSection('#section2');
        } else if(section7_top < window_middle && section7_top >= window_top) {
            highlightSection('#section7');
        } else if(section8_top < window_middle && section8_top >= window_top) {
            highlightSection('#section8');
        } else if(section9_top < window_middle && section9_top >= window_top) {
            highlightSection('#section9');
        } else if(section10_top < window_middle && section10_top >= window_top) {
            highlightSection('#section10');
        }
    });
});

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

function resizeWindow() {
    windowHeight = $(window).height();
    windowWidth = $(window).width();
    $(".quarter-height").height(windowHeight*0.25);
    $(".half-height").height(windowHeight*0.5);
    $(".three-quarter-height").height(windowHeight*0.75);
    $(".full-height").height(windowHeight);
    $(".one-fifth-height").height(windowHeight*0.2);
    $(".seven-tenth-height").height(windowHeight*0.7);
    $(".one-tenth-height").height(windowHeight*0.1);
    $(".one-sixth-height").height(windowHeight*0.167);
    $(".one-twelfth-height").height(windowHeight*0.083);

    //Element Sizes
    s1mh = 43 + ((1280-windowWidth) * 0.029167);
    s1mh = Math.max(43,s1mh);
    s1mh = Math.min(71,s1mh);
    $(".section1-message").css('height',s1mh+'%');
    s1ih = 57 - ((1280-windowWidth) * 0.029167);
    s1ih = Math.max(29, s1ih);
    s1ih = Math.min(57, s1ih);
    $(".section1-image").css('height',s1ih+'%');
    $(".section1-img").css('height','100%');


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
    $(".people-top").height(windowHeight*0.1875);
    $(".people-middle").height(windowHeight*0.515);
    $(".people-bottom").height(windowHeight*0.0475);
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
    $(".people-margin-top").height(windowHeight/6.936);
    $(".people-container").height(windowHeight/1.238);
    $(".people-container").width(windowWidth/1.544);
    $(".people-margin-bottom").height(windowHeight/20.807);

    //Set font-sizes
    $(".section1_heading").css('font-size',windowWidth/30.476);
    $(".section_text").css('font-size',windowWidth/80);
    $(".section2_text").css('font-size',windowWidth/40);
    $(".section3_heading").css('font-size',windowWidth/32);
    $(".section6_left_text").css('font-size',windowWidth/53.33);
    $(".section6_right_heading").css('font-size',windowWidth/53.33);
    $(".section6_right_text").css('font-size',windowWidth/85.33);
    $(".program-time").css('font-size',windowWidth/80);
    $(".program-heading").css('font-size',windowWidth/53.33);
    $(".program-desc").css('font-size',windowWidth/98.46);
    $(".people-designation").css('font-size',windowWidth/91.43);
    $(".people-name").css('font-size',windowWidth/42.67);
    $(".people-website").css('font-size',windowWidth/91.43);
    $(".people-twitter-handle").css('font-size',windowWidth/91.43);
    $(".people-desc").css('font-size',windowWidth/80);
    $(".people-score-name").css('font-size',windowWidth/64);
    $(".calendar-text").css('font-size',windowWidth/67.368);

    //Set line-height
    $(".section_text").css('line-height',(windowWidth/49.23)+'px');
    $(".section2_text").css('line-height',(windowWidth/25.6)+'px');

    //Set Margin
    $(".people-picture").css('margin',windowWidth/256);
    $(".progress").css('margin-bottom',windowWidth/426.67);
    $(".progress").css('margin-top',windowWidth/213.33);

    //Set dimensions
    $(".progress").css('height',windowWidth/64);
    $(".people-score-name").css('height',windowWidth/64);
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