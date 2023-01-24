// Create a line from point A to point B

function clear_temp_line(){
    var main_canvas = document.getElementById("canvasLines");
    var ctx = main_canvas.getContext("2d");

    ctx.clearRect(0,0, main_canvas.width, main_canvas.height);
};

function draw_temp_line(x1, y1, x2, y2, color){
    var main_canvas = document.getElementById("canvasLines");
    var ctx = main_canvas.getContext("2d");

    ctx.clearRect(0,0, main_canvas.width, main_canvas.height);
    ctx.strokeStyle = color;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
};

function draw_joining_line(x1, y1, x2, y2, color){
    ctx.strokeStyle = color;
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
};
