$(document).ready(function() {
    $(window).on("resize load", resizeWindow);
});

function resizeWindow() {
    windowHeight = $(window).height();
    windowWidth = $(window).width();
    $(".member-access").height(windowHeight);
    $(".access-top").height(windowHeight/3);
    $(".access-middle").height(windowHeight/3);
    $(".access-bottom").height(windowHeight/3);
}

function showPasscodeEntry() {
    $("#code-entry").show();
    $("#access-selection").animate({left: "100%"}, 2000, function(){$("#access-selection").hide();});
}

function showQuestionPick() {
    $("#question-pick").show();
    $("#access-selection").animate({left: "-100%"}, 2000, function(){$("#access-selection").hide();$(".access-box-in").css("overflow", "visible");});
}