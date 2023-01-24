import random 
from typing import List, Tuple

def create_random_setup(x_dim_canvas : float, 
                        y_dim_canvas : float, 
                        number_figures : int = 3, 
                        different_lens : bool = False, 
                        different_rotation : bool = False) -> List[Tuple[str, float, bool]]:
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

    difficulty = get_difficulty(figures)
    return figures, difficulty


def get_difficulty(game_setup : List[Tuple[str, float, bool]]) -> str:
    """
    This function returns the difficulty of the game
    """
    difficulty_index = len(game_setup)

    for figure_setup in game_setup:
        if figure_setup[0] == 'triangle':
            difficulty_index += 3
        else:
            difficulty_index += 4

        if figure_setup[2]:
            difficulty_index += 1
        
        if figure_setup[1] > 0.5:
            difficulty_index += 1

    if difficulty_index <= 9:
        return 'easy'
    elif difficulty_index <= 15:
        return 'medium'
    else:
        return 'hard'
        

