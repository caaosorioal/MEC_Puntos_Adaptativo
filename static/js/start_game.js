const startButton = document.getElementById("start-button");
startButton.addEventListener("click", function() {
  alert("Comienza el juego");
  window.location.replace(`0.0.0.0:${server_port}/game/1`);
});