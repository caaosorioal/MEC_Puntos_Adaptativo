var figures = [
    [{x:400, y:100}, {x:300, y:100}, {x:300, y:200}, {x:400, y:200}],
    [{x:200, y:100}, {x:100, y:100}, {x:100, y:200}, {x:200, y:200}]
];

var ctx = document.getElementById("canvasPoints").getContext("2d");

// Function to draw the points inside the figure array.
function draw_point(x, y, color){
    ctx.fillStyle = color; 
    ctx.beginPath(); //Start path
    ctx.arc(x, y, 5, 0, Math.PI * 2, true); // Draw a point using the arc function of the canvas with a point structure.
    ctx.fill(); // Close the path and fill.
}

function draw_points(figure){
    for (var i = 0; i < figure.length; i++) {
        draw_point(figure[i].x , figure[i].y);
    } 
}

// Draw all the figures.
for (var i = 0; i < figures.length; i++) {
    draw_points(figures[i]);
}
