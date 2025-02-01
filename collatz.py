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
    if num == 1: return 0
    return num // 2 if num % 2 == 0 else 3 * num + 1

# Creates the pygame rect squares for each number in a sequence
def get_sequence_positions(num: int) -> list[(int, int)]:
    m = num
    step = 0
    
    positions = []
    
    # Until the number gets to 1, continue to create the sqaures 
    while m >= 1:
        
        x = step 
        y = square_spawn[1] - (m * square_size * axis_multiplier[1])
        
        positions.append((x, y))
        
        # Get the next value in the sequence
        m = get_next(m)
        step += square_size * axis_multiplier[0]
    
    return positions



# List of squares for every sequence
sequence_positions = []

counter = 0
n = 0

run = True
pressed = False

# Game loop
while run:
    
    # Create the screen and get the key presses
    screen.fill((24, 14, 26))
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
        sequence_positions.append(get_sequence_positions(counter))
    
    # Draw each square from every sequence
    for g in range(len(sequence_positions)):
        for s in range(1, len(sequence_positions[g])):
            pygame.draw.line(screen, pygame.Color(213, 224, 216, 0), sequence_positions[g][s - 1], sequence_positions[g][s])
    
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
    