// This function checks if the game is finished

function check_if_game_is_finished(){
    var finished_figures = check_if_figure_is_finished();
    
    if (finished_figures.length == winning_lines.length){
        // Final time of the game
        return true
    } else {
        return false
    }
};