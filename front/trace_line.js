var figures = [
    [{x:400, y:100}, {x:300, y:100}, {x:300, y:200}, {x:400, y:200}],
    [{x:200, y:100}, {x:100, y:100}, {x:100, y:200}, {x:200, y:200}]
];

var n_clicks = 0;
var click_x = 0;
var click_y = 0;

$("#canvasLines").click(function(e){
    click_x = e.pageX - this.offsetLeft;
    click_y = e.pageY - this.offsetTop;
    n_clicks += 1; 
    for (var i = 0; i < figures.length; i++) {
        for (var j = 0; j < figures[i].length; j++) {
            if ((euclidean_distance(click_x, click_y, figures[i][j].x, figures[i][j].y) >= 5) ) {
                var main_canvas = document.getElementById("canvasLines");
                var ctx = main_canvas.getContext("2d");
                ctx.clearRect(0,0, main_canvas.width, main_canvas.height);
            } else {}
        }
    }

});

$("#canvasLines").mousemove(function(e){
    cursor_x = e.pageX - this.offsetLeft;
    cursor_y = e.pageY - this.offsetTop;

    for (var i = 0; i < figures.length; i++) {
        for (var j = 0; j < figures[i].length; j++) {
            if ((euclidean_distance(click_x, click_y, figures[i][j].x, figures[i][j].y) < 5) && (n_clicks % 2 == 0) ) {
                draw_line(figures[i][j].x, figures[i][j].y, cursor_x, cursor_y, "red");
                draw_point(figures[i][j].x, figures[i][j].y, "red");
            } else {}
        }
    }

    
}).mouseover();




