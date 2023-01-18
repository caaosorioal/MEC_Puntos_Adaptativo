import pygame
from math import pi
from game import Game
from create_game import create_random_setup

# Initialize pygame
pygame.init()

# Create the screen
x_dim_canvas = 800
y_dim_canvas = 600

screen = pygame.display.set_mode((x_dim_canvas, y_dim_canvas))
pygame.display.set_caption("Example code for the draw module")

# Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

number_of_figures = 5
game_setup = create_random_setup(x_dim_canvas, y_dim_canvas, number_of_figures)
_, figures = Game(x_dim_canvas, y_dim_canvas, game_setup).create_game()

click_position_start = None
click_position_finish = None

while not done:
    # This limits the while loop to a max of 60 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(60)

    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    # Clear the screen and set the screen background
    screen.fill("white")

    # Plot the points of figures
    for figure in figures:
        for point in figure:
            pygame.draw.circle(screen, "black", list(point), 5)
    
    if event.type == pygame.MOUSEBUTTONDOWN:
        click_position_start = event.pos

    if event.type == pygame.MOUSEBUTTONUP:
        click_position_finish = event.pos
            
    # Get position of the mouse 
    mouse_position = pygame.mouse.get_pos()

    # Draw a line from the initial position to the current position
    if click_position_start is not None:
        pygame.draw.circle(screen, "red", click_position_start, 5)
        pygame.draw.line(screen, "gray", click_position_start, mouse_position, 3)

    if click_position_finish is not None:
        pygame.draw.circle(screen, "red", click_position_finish, 5)
        pygame.draw.line(screen, "gray", click_position_start, click_position_finish, 3)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly
pygame.quit()