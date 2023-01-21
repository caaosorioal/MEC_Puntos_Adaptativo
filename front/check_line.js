// This function checks if the line between point_1 and point_2 is in the list winning_lines
function check_if_solution(point_1, point_2){
    for (var i = 0; i < winning_lines.length; i++) {
        if (point_1.x == winning_lines[i][0].x && point_1.y == winning_lines[i][0].y 
            && point_2.x == winning_lines[i][1].x && point_2.y == winning_lines[i][1].y){
            return true
        } else if (point_1.x == winning_lines[i][1].x && point_1.y == winning_lines[i][1].y
            && point_2.x == winning_lines[i][0].x && point_2.y == winning_lines[i][0].y){
            return true
        }
    };
    return false
}