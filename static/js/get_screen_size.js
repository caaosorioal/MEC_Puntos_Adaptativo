// Get the screen size

var height_size = $(document).height();
var width_size = $(document).width();

connection_to_server({'x_size': width_size , 'y_size': height_size}, 'POST', '0.0.0.0:8000/get-size-canvas/');