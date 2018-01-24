var search_stock = function( e ) {
  var name = $('input[name="stock"]').val();
  console.log("Name = " + name);

  $.ajax({
  url: '/get_stock_price',
  type: 'POST',
  data: {'stock' : name},
  success: function(response) {
      console.log("wait...")
      response = JSON.parse(response);
      console.log(response["price"]);
      stockName = document.getElementById("searched_stock_name");
      var nameVal = "Stock: " + response["name"];
      stockName.display = "inline"
      stockName.value = nameVal;
      stockPrice = document.getElementById("searched_stock_price");
      var priceVal = "Price: " + response["price"];
      stockPrice.display = "inline"
      stockPrice.value = priceVal;
      var button = document.getElementById("buy");
      button.style.display = "inline";
      var field = document.getElementById("num_stock");
      field.style.display = "inline";
  }, //end success callback
  error: function (response){
    var errorMess = document.getElementById("searched_stock_name");
    var clear = document.getElementById("searched_stock_price");
    var button = document.getElementById("buy");
    var field = document.getElementByID("num_stock");
    errorMess.value = "Invalid Ticker!";
    errorMess.display = "none"
    clear.value = "";
    clear.display = "none"
    button.style.display = "none";
    field.style.display = "inline";
  }
  });//end ajax call
}; //end transmit function

document.getElementById("stock_search").addEventListener('click', search_stock );
