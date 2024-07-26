document.addEventListener("DOMContentLoaded", function() {

  var redHeaderDiv = document.getElementById("red_header");


  redHeaderDiv.addEventListener("click", function() {

    var header = document.querySelector("header");

    header.classList.add("red");
  });
});

