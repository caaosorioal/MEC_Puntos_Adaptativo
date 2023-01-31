const startButton = document.getElementById("start-button");
startButton.addEventListener("click", function() {
  alert("Comienza el juego");
  window.location.replace(`/game/1`);
});