// Initialize the list of the current winning lines
var current_winning_lines = [];

function check_if_line_belongs_to_solution(point_1, point_2, list){
    for (var i = 0; i < list.length; i++) {
        for (var j = 0; j < list[i].length; j++) {
            if (point_1.x == list[i][j][0].x && point_1.y ==  list[i][j][0].y 
                && point_2.x == list[i][j][1].x && point_2.y ==  list[i][j][1].y){
                return true
            } else if (point_1.x == list[i][j][1].x && point_1.y ==  list[i][j][1].y
                && point_2.x ==  list[i][j][0].x && point_2.y ==  list[i][j][0].y){
                return true
            }
        }
    };
    return false
};


function check_if_line_belongs_to_current_correct_lines(point_1, point_2, list){
    for (var i = 0; i < list.length; i++) {
        if (point_1.x == list[i][0].x && point_1.y == list[i][0].y 
            && point_2.x == list[i][1].x && point_2.y == list[i][1].y){
            return true
        } else if (point_1.x == list[i][1].x && point_1.y == list[i][1].y
            && point_2.x == list[i][0].x && point_2.y == list[i][0].y){
            return true
        }
    };
    return false
};