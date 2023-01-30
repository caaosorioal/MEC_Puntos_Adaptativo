from src.mec_points.figures import *

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
        lens = [figure[1] for figure in self.figures]
        rotations = []

        for figure in self.figures:
            if figure[0] == 'square':
                square_ = Square(self.x_dim_canvas, self.y_dim_canvas, figure[1], figure[2])
                figures.append(square_.create_figure())
                rotations.append(square_.rotation_angle)

            elif figure[0] == 'triangle':
                triangle_ = Triangle(self.x_dim_canvas, self.y_dim_canvas, figure[1], figure[2])
                figures.append(triangle_.create_figure())
                rotations.append(triangle_.rotation_angle)
                
            else:
                raise ValueError('The figure is not valid')

        solutions = self.create_solutions(figures)
        return (canvas, figures, solutions, lens, rotations)

    def create_solutions(self, figures : List[List[Tuple]]) -> List[List[Tuple]]:
        """
        This function creates the solution of every figure.
        A solution is just a counterclockwise path of all pairs of points from the figure
        """
        if len(figures) == 0:
            raise ValueError('The list of figures is empty')
         
        solutions = []
        for figure in figures:
            solutions_figure = []
            solutions_figure.append((figure[-1], figure[0]))

            for i in range(len(figure) - 1):
                solution_pair = (figure[i], figure[i+1])
                solutions_figure.append(solution_pair)

            solutions.append(solutions_figure)
            
        return solutions
