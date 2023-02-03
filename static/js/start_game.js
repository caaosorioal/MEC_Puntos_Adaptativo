const startButton = document.getElementById("start-button");
startButton.addEventListener("click", function() {
  alert("The game will start now!");
  window.location.replace(`/game/1`);
});