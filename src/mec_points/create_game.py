import random 
from typing import List, Tuple

def create_random_setup(x_dim_canvas : float, y_dim_canvas : float, number_figures : int = 3, 
    different_lens : bool = False, different_rotation : bool = False) -> List[Tuple[str, float, bool]]:
    """
    This function creates a random setup for the game
    """
    # Create the figures
    figures = []
    figure_side = random.uniform(0, min(x_dim_canvas, y_dim_canvas))
    rotation = False

    for _ in range(number_figures):
        figure = random.choice(['square', 'triangle'])
        if different_lens: 
            figure_side = random.uniform(0, min(x_dim_canvas, y_dim_canvas))

        if different_rotation: 
            rotation = random.choice([True, False])

        figures.append((figure, figure_side, rotation))

    return figures