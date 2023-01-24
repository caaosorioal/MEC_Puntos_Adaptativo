// This function will check if some figure is finished
// To do so, it will loop through the list of all the figures in the solution and then
// it will check if all the lines of the figure are in the list of the current winning lines

function check_if_figure_is_finished(){
    let finished_figures_ = [];
    
    for (i = 0; i < winning_lines.length; i++) {
        let finished_lines_of_figure = [];
        
        for (j = 0; j < winning_lines[i].length; j++) {
            if (check_if_line_belongs_to_current_correct_lines(winning_lines[i][j][0], winning_lines[i][j][1], current_winning_lines)){
                finished_lines_of_figure.push(winning_lines[i][j]);
            }
        };

        if (finished_lines_of_figure.length == winning_lines[i].length){
            finished_figures_.push(finished_lines_of_figure);
        }
    };
    return finished_figures_
};