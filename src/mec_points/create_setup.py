import random 
from typing import List, Tuple
from src.apis.get_config import *
from src.mec_points.game import Game
from typing import Dict
import numpy as np

# This function creates the random setup for the game
def send_data_random_game(n_figures : int = 3, different_lens : bool = True, different_rotation : bool = True) -> Dict:
    canvas_x_size, canvas_y_size = canvas_size()

    game_setup, difficulty = create_random_setup(
                                                canvas_x_size, 
                                                canvas_y_size, 
                                                number_figures=n_figures, 
                                                different_lens=different_lens,
                                                different_rotation=different_rotation
    )
    _, figures, solutions, lens, rotations = Game(canvas_x_size, canvas_y_size, game_setup).create_game()

    return {
        "x_size" : canvas_x_size,
        "y_size" : canvas_y_size, 
        "generated_figures" : figures,
        "generated_solutions" : solutions,
        "difficulty": difficulty,
        "n_figures" : n_figures,
        "mean_lens_figures" : np.mean(lens),
        "rotation_mean_angles" : np.mean(rotations),
        "std_lens_figures" : np.std(lens),
    }

# This function allow to create a random setup for the game
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
    min_dim = min(x_dim_canvas, y_dim_canvas)
    figure_side = random.uniform(0.2 * min_dim, 0.8 * min_dim)
    rotation = False

    for _ in range(number_figures):
        figure = random.choice(['square', 'triangle'])
        if different_lens: 
            figure_side = random.uniform(0.2 * min_dim, 0.8 * min_dim)

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
        

