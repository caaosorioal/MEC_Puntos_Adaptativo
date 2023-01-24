function is_solution_point(p_x, p_y){
    for (var i = 0; i < figures.length; i++) {
        for (var j = 0; j < figures[i].length; j++) {
            if (euclidean_distance(p_x, p_y, figures[i][j].x, figures[i][j].y) < 5) {
                return true
            };
        };
    };   
    return false
};

function nearest_solution_point(p_x, p_y){
    var nearest_point = null;
    var radius = 5;

    for (var i = 0; i < figures.length; i++) {
        for (var j = 0; j < figures[i].length; j++) {
            var distance = euclidean_distance(p_x, p_y, figures[i][j].x, figures[i][j].y);
            if (distance < radius) {
                nearest_distance = distance;
                nearest_point = figures[i][j];
            };
        };
    };   
    return nearest_point
}