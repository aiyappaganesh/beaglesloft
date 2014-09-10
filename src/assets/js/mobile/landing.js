$(document).ready(function() {
   $("#section3-carousel").on("swiperight", function() {
      $("#section3-carousel").carousel('prev');
    });
   $("#section3-carousel").on("swipeleft", function() {
      $("#section3-carousel").carousel('next');
   });
});