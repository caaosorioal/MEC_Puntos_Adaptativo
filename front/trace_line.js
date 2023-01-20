var figures = [
    [{x:400, y:100}, {x:300, y:100}, {x:300, y:200}, {x:400, y:200}],
    [{x:200, y:100}, {x:100, y:100}, {x:100, y:200}, {x:200, y:200}]
];

var n_clicks = 0;
var initial_click = null;

var click_x = 0;
var click_y = 0;
var winning_lines = [];

$("#canvasLines").click(function(e){
    click_x = e.pageX - this.offsetLeft;
    click_y = e.pageY - this.offsetTop;

    if (is_solution_point(click_x, click_y)){
        n_clicks += 1; 
        nearest_point = nearest_solution_point(click_x, click_y);
        console.log("You clicked on a point that is part of a figure");
        
        if (n_clicks % 2 == 0){
            winning_lines.push({x1: initial_click.x, y1: initial_click.y, x2: nearest_point.x, y2: nearest_point.y});
            draw_winning_line(initial_click.x, initial_click.y, nearest_point.x, nearest_point.y, "green");
            console.log(winning_lines);
            initial_click = null;
            click_x = 0;
            click_y = 0;
            clear_line();
        } else {
            initial_click = {x: nearest_point.x, y: nearest_point.y};
        }
    } else {
        clear_line();
    }
});

$("#canvasLines").mousemove(function(e){
    cursor_x = e.pageX - this.offsetLeft;
    cursor_y = e.pageY - this.offsetTop;

    if (is_solution_point(click_x, click_y)){
        nearest_point = nearest_solution_point(click_x, click_y);
        draw_line(nearest_point.x, nearest_point.y, cursor_x, cursor_y, "red");
        draw_point(nearest_point.x, nearest_point.y, "red");
    }
}).mouseover();

console.log(winning_lines);



