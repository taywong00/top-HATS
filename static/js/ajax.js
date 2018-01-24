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

      var stockName = document.getElementById("searched_stock_name");
      var nameVal = "Stock: " + response["name"];
      stockName.style.display = "inline"
      stockName.value = nameVal;

      var stockPrice = document.getElementById("searched_stock_price");
      var priceVal = "Price: " + response["price"];
      stockPrice.style.display = "inline"
      stockPrice.value = priceVal;

      var high = document.getElementById("high");
      var highval = "High: " + response["high"];
      high.style.display = "inline";
      high.value = highval;

      var low = document.getElementById("low");
      var lowval = "Low: " + response["low"];
      low.style.display = "inline";
      low.value = lowval;


      var button = document.getElementById("buy");
      button.style.display = "inline";

      var field = document.getElementById("num_stock");
      field.style.display = "inline";
  }, //end success callback
  error: function (response){
    var errorMess = document.getElementById("searched_stock_name");
    var clear = document.getElementById("searched_stock_price");
    var button = document.getElementById("buy");
    var field = document.getElementById("num_stock");
    errorMess.value = "Invalid Ticker!";
    clear.value = "";
    clear.style.display = "none"
    button.style.display = "none";
    field.style.display = "inline";
  }
  });//end ajax call
}; //end transmit function

document.getElementById("stock_search").addEventListener('click', search_stock );
