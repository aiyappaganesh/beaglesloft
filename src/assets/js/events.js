$(document).ready(function() {
    $(window).on("load resize", resizeWindow);
});

function resizeWindow() {
    windowHeight = $(window).height();
    windowWidth = $(window).width();
    $(".quarter-height").height(windowHeight*0.25);
    $(".half-height").height(windowHeight*0.5);
    $(".three-quarter-height").height(windowHeight*0.75);
    $(".full-height").height(windowHeight);
}