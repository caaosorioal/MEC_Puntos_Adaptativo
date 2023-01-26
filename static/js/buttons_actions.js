$("#new_game").on("click", evt => {
    // Prevent the default action of the button
    evt.preventDefault();

    // Reload the page
    if (confirm("Are you sure you want to start a new game?")){
        location.reload();
    };
});

// Function to get a random integer between min and max
function randomInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

$("#get_hint").on("click", evt => {
    // Prevent the default action of the button
    evt.preventDefault();

    // Get a random line
    var random_line = winning_lines[randomInteger(0, winning_lines.length - 1)];
    // Get the points of the line
    var hint_points = random_line[randomInteger(0, random_line.length - 1)];

    // Draw the line
    if (!check_if_line_belongs_to_current_correct_lines(hint_points[0], hint_points[1], current_winning_lines)){
        draw_joining_line(hint_points[0].x, hint_points[0].y, hint_points[1].x, hint_points[1].y, 'green');
        current_winning_lines.push([hint_points[0], hint_points[1]]);
        n_success += 1;
        show_data("correct_lines", n_success);
    }
});