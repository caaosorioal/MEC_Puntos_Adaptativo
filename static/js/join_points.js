// Initial setup to follow up the events
var id_clicks = 0;
var initial_click = null;
var error_line = false;
var n_clicks = 0;

// Initialiaze the success/fails counter
var n_success = 0;
var n_fails = 0;

// Variables to store the coordinates of the cursor
var click_x = 0;
var click_y = 0;

$("#canvasLines").click(function(e){
    click_x = e.pageX - this.offsetLeft;
    click_y = e.pageY - this.offsetTop;
    // Save the number of clicks
    n_clicks += 1;

    // Check if the click is on a point of some figure
    if (is_solution_point(click_x, click_y)){
        id_clicks += 1; 
        nearest_point = nearest_solution_point(click_x, click_y);
        console.log("You clicked on a point that is part of a figure");
        
        // If the click is on a point of a figure, draw a line from the previous point to the new point
        if (id_clicks % 2 == 0){
            if ((check_if_point_belongs_to_list(initial_click, nearest_point, winning_lines)) && (!check_if_point_belongs_to_list(nearest_point, initial_click, current_winning_lines))){
                n_success += 1;
                draw_joining_line(initial_click.x, initial_click.y, nearest_point.x, nearest_point.y, 'green');
                clear_temp_line(); 
                current_winning_lines.push([initial_click, nearest_point]);
            } else {
                draw_temp_line(initial_click.x, initial_click.y, nearest_point.x, nearest_point.y, 'red');
                n_fails += 1;
            }
            initial_click = null;
            click_x = 0;
            click_y = 0;
        } else {
            initial_click = {x: nearest_point.x, y: nearest_point.y};
        }
    } else {
        id_clicks = 0;
        initial_click = null;
        clear_temp_line();
    }
    console.log("n_clicks: " + n_clicks);
    console.log("n_success: " + n_success);
    console.log("n_fails: " + n_fails);
});

$("#canvasLines").mousemove(function(e){
    cursor_x = e.pageX - this.offsetLeft;
    cursor_y = e.pageY - this.offsetTop;

    // Check if the cursor is on a point of some figure. If so, draw a red point and a red line from the last point clicked to the cursor
    if (is_solution_point(click_x, click_y)){
        nearest_point = nearest_solution_point(click_x, click_y);
        draw_temp_line(nearest_point.x, nearest_point.y, cursor_x, cursor_y, "orange");
        draw_point(nearest_point.x, nearest_point.y, "#ffb703", 8);
    }
}).mouseover();