$("#myCanvas").click(function(e){
    getMousePosition(e); 
});

function getMousePosition(e){
    var rect = myCanvachangeColorPoints.getBoundingClientRect();
    var x = e.clientX - rect.left; // x == the location of the click in the document - the location (relative to the left) of the canvas in the document
    var y = e.clientY - rect.top; // y == the location of the click in the document - the location (relative to the top) of the canvas in the document
    
    // This method will handle the coordinates and will draw them in the canvas.
    drawCoordinates(x,y);
}

function drawCoordinates(x,y){
    var pointSize = 5; // Change according to the size of the point.
    var ctx = document.getElementById("myCanvas").getContext("2d");

    ctx.fillStyle = "#ff2626"; // Red color

    ctx.beginPath(); //Start path
    ctx.arc(x, y, pointSize, 0, Math.PI * 2, true); // Draw a point using the arc function of the canvas with a point structure.
    ctx.fill(); // Close the path and fill.
}   
