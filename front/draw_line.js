// Create a line from point A to point B

function draw_line(x1, y1, x2, y2, color){
    var main_canvas = document.getElementById("canvasLines");
    var ctx = main_canvas.getContext("2d");

    ctx.clearRect(0,0, main_canvas.width, main_canvas.height);
    ctx.strokeStyle = color;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
}