document.addEventListener("DOMContentLoaded", function() {

  var toggleHeaderDiv = document.getElementById("toggle_header");


  toggleHeaderDiv.addEventListener("click", function() {

    var header = document.querySelector("header");

    if (header.classList.contains("red")) {
      header.classList.remove("red");
      header.classList.add("green");
    } else if (header.classList.contains("green")) {
      header.classList.remove("green");
      header.classList.add("red");
    }
  });
});

