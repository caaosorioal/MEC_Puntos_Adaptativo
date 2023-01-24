var ctx = document.getElementById("canvasPoints").getContext("2d");

// Function to draw the points inside the figure array.
function draw_point(x, y, color, radius = 5){
    ctx.fillStyle = color; 
    ctx.beginPath(); 
    ctx.arc(x, y, radius, 0, Math.PI * 2, true); 
    ctx.fill(); 
};

function draw_points(figure){
    for (var i = 0; i < figure.length; i++) {
        draw_point(figure[i].x , figure[i].y);
    } 
};

// Draw all the figures.
for (var i = 0; i < figures.length; i++) {
    draw_points(figures[i]);
};
