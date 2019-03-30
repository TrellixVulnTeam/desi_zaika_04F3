$(document).ready(function (){
  var addProductForm = $(".add-product");
  addProductForm.submit(function(e){
    e.preventDefault();
    var thisForm = $(this);
    var action = thisForm.attr("action");
    var method= thisForm.attr("method");
    var data = thisForm.serialize();

    $.ajax({
      url:action,
      method:method,
      data:data,
      success: function(data){
        var buttonArea = thisForm.find(".buttonArea");
        if(data.added){
          buttonArea.html('<button type="submit" class="add-to-cart-button">Remove</button>');
        }else{
          buttonArea.html('<button  type="submit" class="add-to-cart-button">Add To Cart</button>');
        }

        var productsInTheCart = $('.products-in-the-cart');
        productsInTheCart.text(data.cartProductCount);
        // if(window.location.href.indexOf('cart') != -1){
        //   updateCart();
        // }
      },
      error : function(error){
        console.log("error");
        console.log(error);
      }
    });

  });
  // updateCart(){
  //   console.log("cart updated!");
  // }
});
