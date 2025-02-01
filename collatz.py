"""
This module visualizes the Collatz Conjecture using Pygame.

Author: Jakob Lucas
"""

import pygame # type: ignore
import math
import random

pygame.init()

# Screen size and creation
SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

color1 = pygame.Color(255, 0, 0)
color2 = pygame.Color(0, 0, 255)

# Distance between squares on each axis
start_degree = 90
# Change in degree per step in a sequence
degree_increment = 10
# Standard length of a line
line_length = 25
# Degree that a line turns when a number is odd
line_degree_turn = 45

# Starting point for squares
square_spawn = [0, SCREEN_HEIGHT]

# Gets the next value of a number based on the Collatx conjecture 
def get_next(num: int) -> int:
    return num // 2 if num % 2 == 0 else 3 * num + 1

# Get the positions of each subsequent number in a sequence
def get_sequence_positions(n: int, s_degree: float) -> list[tuple[int, int]]:
    m = n
    step = 1
    
    sequence = [n]
    while m != 1:
        m = get_next(m)
        sequence.append(m)
    sequence.reverse()
    
    positions = [None] * len(sequence)
    
    x = math.cos(math.radians(s_degree)) * line_length
    y = math.sin(math.radians(s_degree)) * line_length
    
    # Until the number gets to 1, continue to create the squares 
    for num in sequence:
        
        angle = s_degree + step * degree_increment + (line_degree_turn * (num % 2))
        length = max(line_length // 5, line_length - step) * math.log2(num)
        
        x = math.cos(math.radians(angle)) * length + x
        y = math.sin(math.radians(angle)) * length + y
        
        positions[step - 1] = (x + SCREEN_WIDTH // 2, y + SCREEN_HEIGHT // 2)
        # Get the next value in the sequence
        step += 1
    
    return positions



# List of squares for every sequence
sequence_positions = []

counter = 2
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
        sequence_positions.append(get_sequence_positions(counter, start_degree))
        start_degree += random.randint(0, 45)
    
    # Draw each square from every sequence
    for sequence_index in range(len(sequence_positions)):
        for position_index in range(1, len(sequence_positions[sequence_index])):
            
            percent = position_index / len(sequence_positions[sequence_index]) 
            print(f"percent: {percent}")
            
            r = int(color1.r + percent * (color2.r - color1.r))
            g = int(color1.g + percent * (color2.g - color1.g))
            b = int(color1.b + percent * (color2.b - color1.b))
            
            print(f"r: {r}, g: {g}, b: {b}")
            
            pygame.draw.line(screen, pygame.Color(r, g, b), sequence_positions[sequence_index][position_index - 1], sequence_positions[sequence_index][position_index])
    
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
    