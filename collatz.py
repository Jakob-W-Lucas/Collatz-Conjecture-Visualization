"""

Collatz Visualization

Author: Jakob Lucas

"""

import pygame

pygame.init()

# Screen size and creation
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Size of each square to display
square_size = 10
# Distance between squares on each axis
axis_multiplier = [2, 2]

# Starting point for squares
square_spawn = [0, SCREEN_HEIGHT]

# Gets the next value of a number based on the Collatx conjecture 
def get_next(num: int) -> int:
    return num // 2 if num % 2 == 0 else 3 * num + 1

# Creates the pygame rect squares for each number in a sequence
def create_num_squares(num: int) -> list[pygame.Rect]:
    m = num
    step = 0
    
    squares = []
    
    # Initial square in a sequence 
    squares.append(pygame.Rect((step, square_spawn[1] - (m * square_size * axis_multiplier[1]), square_size, square_size)))
    
    # Until the number gets to 1, continue to create the sqaures 
    while m != 1:
    
        # Get the next value in the sequence
        m = get_next(m)
        step += square_size * axis_multiplier[0]
        
        x = step 
        y = square_spawn[1] - (m * square_size * axis_multiplier[1])
        
        # Create the new square
        squares.append(pygame.Rect((x, y, square_size, square_size)))
    
    return squares



# List of squares for every sequence
sequence_squares = []

counter = 0
n = 0

run = True
pressed = False

# Game loop
while run:
    
    # Create the screen and get the key presses
    screen.fill((255, 255, 255))
    key = pygame.key.get_pressed()
    
    # Returns true once when the key is initially pressed
    if key[pygame.K_j] and pressed != True:
        counter += 1
        pressed = True
    
    # Only allow to increment when key is let go
    if not key[pygame.K_j]:
        pressed = False
    
    # Get the new list of squares for the next sequence
    if n != counter:
        n = counter
        sequence_squares.append(create_num_squares(counter))
    
    # Draw each square from every sequence
    for group in sequence_squares:
        for r in group:
            pygame.draw.rect(screen, (0, 0, 0), r)
    
    # Exit
    if key[pygame.K_ESCAPE]:
       run = False
       
    # Quit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # Update the game display
    pygame.display.update()

pygame.quit()
    