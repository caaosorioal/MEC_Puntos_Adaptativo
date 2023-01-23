from mec_points.figures import *

class Game:
    def __init__(self, x_dim_canvas, y_dim_canvas, figures_setup : Tuple[str, float, bool]):
        self.x_dim_canvas = x_dim_canvas
        self.y_dim_canvas = y_dim_canvas
        self.figures = figures_setup

    def create_game(self) -> List[List[Tuple]]:
        """
        This function creates a game with the given parameters
        """
        # Create the canvas
        canvas = Canvas(self.x_dim_canvas, self.y_dim_canvas)

        # Create the figures
        figures = []
        for figure in self.figures:
            if figure[0] == 'square':
                figures.append(Square(self.x_dim_canvas, self.y_dim_canvas, figure[1], figure[2]).create_figure())
            elif figure[0] == 'triangle':
                figures.append(Triangle(self.x_dim_canvas, self.y_dim_canvas, figure[1], figure[2]).create_figure())
            else:
                raise ValueError('The figure is not valid')

        return (canvas, figures)