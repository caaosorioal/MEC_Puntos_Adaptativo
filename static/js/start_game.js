const startButton = document.getElementById("start-button");
startButton.addEventListener("click", function() {
  alert("Comienza el juego");
  window.location.replace("http://localhost:8000/game/1");
});