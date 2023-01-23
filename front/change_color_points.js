var figures = [
    [{x:400, y:100}, {x:300, y:100}, {x:300, y:200}, {x:400, y:200}],
];

function euclidean_distance(x1, y1, x2, y2) {
    return Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));
}

$("#canvasLines").mousemove(function(e){
    mouse_x = e.pageX - this.offsetLeft;
    mouse_y = e.pageY - this.offsetTop;

    for (var i = 0; i < figures.length; i++) {
        for (var j = 0; j < figures[i].length; j++) {
            if (euclidean_distance(mouse_x, mouse_y, figures[i][j].x, figures[i][j].y) < 5) {
                draw_point(figures[i][j].x, figures[i][j].y, "black", 7)
            } else {
                // The first point is to erase the previous point.
                draw_point(figures[i][j].x, figures[i][j].y, "white", 8)
                draw_point(figures[i][j].x, figures[i][j].y, "black")
            }
        }
    }
}).mouseover();