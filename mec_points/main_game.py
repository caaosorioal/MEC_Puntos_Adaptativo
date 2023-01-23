import pygame
import pygame.freetype
from mec_points.game import Game
import time
from mec_points.create_game import create_random_setup
from mec_points.utils import *

# Initialize pygame
pygame.init()

# Create the screen
x_dim_canvas = 800
y_dim_canvas = 600

screen = pygame.display.set_mode((x_dim_canvas, y_dim_canvas))
pygame.display.set_caption("MEC - Aprendizaje Adaptativo")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

# Intantiate the game
number_of_figures = 1
game_setup = create_random_setup(x_dim_canvas, y_dim_canvas, number_of_figures)
#game_setup = [('square', 100.0, True)]
_, figures = Game(x_dim_canvas, y_dim_canvas, game_setup).create_game()
all_points = []

# Initialize auxiliary variables
click_position_start = None
click_position_finish = None 
finished_line = False
failed_attempts = 0
correct_attempts = 0

solutions_lines = []
for figure in figures:
    solutions_lines.extend(list((figure[i], figure[i+1]) for i in range(len(figure)-1)))
    solutions_lines.append((figure[-1], figure[0]))

lines = []

while not done:
    # This limits the while loop to a max of 60 times per second.
    clock.tick(60)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            done = True  

    # Clear the screen and set the screen background
    screen.fill("white")

    # Plot the initial points of the figures
    for figure in figures:
        for point in figure:
            pygame.draw.circle(screen, "black", list(point), 5)
            all_points.append(point)

    # Get position of the mouse 
    mouse_position = pygame.mouse.get_pos()

    # Check if the mouse is near to a point, in that case highlight it
    nearest_point = nearest_point_to_mouse(mouse_position, all_points, 5)
    if nearest_point is not None:
        pygame.draw.circle(screen, "orange", nearest_point, 5)

    # This click is for start the line
    if event.type == pygame.MOUSEBUTTONDOWN:
        state = pygame.mouse.get_pressed()

        # If the user click the left button and the mouse is near to a point
        if state[0] and nearest_point is not None:
            click_position_start = nearest_point
        # If the user click the right button and the mouse is near to a point
        elif state[2] and nearest_point is not None:
            click_position_finish = nearest_point

            # Stop 0.5 seconds to see the line
            time.sleep(0.2)
            final_line = pygame.draw.line(screen, "gray", click_position_start, click_position_finish, 3)
            lines.append((click_position_start, click_position_finish))
            click_position_start = None

    # Draw a line from the initial position to the current position
    if click_position_start is not None:
        pygame.draw.circle(screen, "blue", click_position_start, 5)
        pygame.draw.line(screen, "gray", click_position_start, mouse_position, 3)

    # Continuously check if the user has finished a correct line
    current_solutions = check_for_solutions(lines, solutions_lines)
    correct_attempts = len(current_solutions)
    failed_attempts = len(lines) - correct_attempts

    # If the user has finished a correct line, show it
    if current_solutions is not None:
        for solution in current_solutions:
            pygame.draw.line(screen, "green", solution[0], solution[1], 3)

    
    # Draw the text
    font = pygame.freetype.SysFont("Arial", 15)
    font.render_to(screen, (10, 10), f"Correct attempts: {correct_attempts}", (0, 0, 0))
    font.render_to(screen, (10, 30), f"Failed attempts: {failed_attempts}", (0, 0, 0))

    # If the user has finished all the lines, show a message
    if correct_attempts == len(solutions_lines):
        font.render_to(screen, (10, 50), f"Congratulations! You have finished the game", (0, 0, 0))

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()