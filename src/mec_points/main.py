from src.mec_points.game import Game

# Test case for canvas
(x_dim_canvas, y_dim_canvas) = (15, 10)

figures = [
    ('square', 7, True), 
    ('triangle', 7, True), 
    ('triangle', 7, True), 
    ('square', 7, True)
]

canvas, figures = Game(x_dim_canvas, y_dim_canvas, figures).create_game()
canvas.plot_points(figures)

