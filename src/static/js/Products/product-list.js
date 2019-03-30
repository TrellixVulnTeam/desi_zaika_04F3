$(document).ready(function(){
  $('.scrolling-wrapper').slick({
     dots: false,
     infinite: false,
     speed: 700,
     slidesToShow: 5,
     slidesToScroll: 2,
     prevArrow: '<div class="left-arrow"><i class="fas fa-arrow-alt-circle-left fa-2x"></i></div>',
     nextArrow: '<div class="right-arrow"><i class="fas fa-arrow-alt-circle-right fa-2x"></i></div>',
     responsive: [
       {
         breakpoint: 1024,
         settings: {
           slidesToShow: 4,
           slidesToScroll: 3,
           infinite: false,
           dots: false
         }
       },
       {
         breakpoint: 600,
         settings: {
           arrows:false,
           slidesToShow: 3,
           slidesToScroll: 2,
           infinite: false
         }
       },
       {
         breakpoint: 480,
         settings: {
           slidesToShow: 3,
           slidesToScroll: 2,
           infinite: false
         }
       }
     ]
  });
});
