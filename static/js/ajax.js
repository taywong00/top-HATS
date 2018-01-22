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
      output = document.getElementById("searched_stock");
      var inner = "Stock " + response["name"] + ": " + response["price"];
      output.innerHTML = inner
    } //end success callback
  });//end ajax call
}; //end transmit function

document.getElementById("stock_search").addEventListener('click', search_stock );
