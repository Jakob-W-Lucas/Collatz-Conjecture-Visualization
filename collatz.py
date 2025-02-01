"""
This module visualizes the Collatz Conjecture using Pygame.

Author: Jakob Lucas
"""

import pygame
import math

pygame.init()

# Screen size and creation
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Distance between squares on each axis
start_degree = 90
degree_increment = 10
line_length = 30

# Starting point for squares
square_spawn = [0, SCREEN_HEIGHT]

# Gets the next value of a number based on the Collatx conjecture 
def get_next(num: int) -> int:
    return num // 2 if num % 2 == 0 else 3 * num + 1
    
def get_sequence_positions(n: int) -> list[tuple[int, int]]:
    m = n
    step = 1
    
    sequence = [n]
    while m != 1:
        m = get_next(m)
        sequence.append(m)
    sequence.reverse()
    
    positions = [None] * len(sequence)
    
    x = math.cos(math.radians(start_degree)) * line_length
    y = math.sin(math.radians(start_degree)) * line_length
    
    # Until the number gets to 1, continue to create the squares 
    for num in sequence:
        
        angle = start_degree + step * degree_increment + (90 * (num % 2))
        length = max(line_length // 5, line_length - step)
        
        x = math.cos(math.radians(angle)) * length + x
        y = math.sin(math.radians(angle)) * length + y
        
        positions[step - 1] = (x + SCREEN_WIDTH // 2, y + SCREEN_HEIGHT // 2)
        
        # Get the next value in the sequence
        step += 1
    
    return positions



# List of squares for every sequence
sequence_positions = []

counter = 888
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
            pygame.draw.rect(screen, pygame.Color(255, 0, 0), pygame.Rect(sequence_positions[g][s - 1][0], sequence_positions[g][s - 1][1], 3, 3), width=0)
    
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
    