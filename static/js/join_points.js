// Render the number of squares and triangles
$(window).load(
    function(){
        document.getElementById("number_squares").innerHTML = `There are ${number_of_squares} squares`;
        document.getElementById("number_triangles").innerHTML = `There are ${number_of_triangles} triangles`;
    }
);

// Start to measure the time
var start_time = new Date().getTime();

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

    // Change to the original background color
    back_to_normal_background();

    // Save the number of clicks
    n_clicks += 1;

    // Check if the click is on a point of some figure
    if (is_solution_point(click_x, click_y)){
        id_clicks += 1; 
        nearest_point = nearest_solution_point(click_x, click_y);

        // If the click is on a point of a figure, draw a line from the previous point to the new point
        if (id_clicks % 2 == 0){
            if ((check_if_line_belongs_to_solution(initial_click, nearest_point, winning_lines)) && (!check_if_line_belongs_to_current_correct_lines(nearest_point, initial_click, current_winning_lines))){
                n_success += 1;
                draw_joining_line(initial_click.x, initial_click.y, nearest_point.x, nearest_point.y, 'green');
                clear_temp_line(); 
                current_winning_lines.push([initial_click, nearest_point]);
                
                // Show the result to the user
                highlight_result("correct_lines")
                show_data("correct_lines", n_success);

                // Check if some figure is finished
                var finished_figures = check_if_figure_is_finished();
                show_data("correct_figures", finished_figures.length);

                // Check if the game is finished
                if (finished_figures.length == winning_lines.length){
                    alert("Congratulations! You have finished the game in " + n_clicks + " clicks and you spent " + (new Date().getTime() - start_time)/1000 + " seconds.")
                };
                
            } else {
                draw_temp_line(initial_click.x, initial_click.y, nearest_point.x, nearest_point.y, 'red');
                n_fails += 1;

                // Show the result to the user
                highlight_result("incorrect_lines")
                show_data("incorrect_lines", n_fails);
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