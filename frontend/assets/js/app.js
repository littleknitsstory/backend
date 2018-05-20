import $ from "jquery";



// $(function(){
//     $(window).scroll(function() {
//         if($(this).scrollTop() >= 290) {
//             $('.menu-container').addClass('menu-fixed');
//             }
//         else{
//             $('.menu-container').removeClass('menu-fixed');
//             }
//     });
// });

$(document).ready(function() {
  $(window).bind('scroll', function() {
    // The value of where the "scoll" is.
    if($(window).scrollTop() > 235){
      $('.menu').addClass('menu-fixed');
      $('.container').css('padding-top', '90px');
    }else{
      $('.menu').removeClass('menu-fixed');
      // Adding padding so it doesn't jump up
      // when the menu gets fixed.
      $('.container').css('padding-top', '0px');
    }
  })
});