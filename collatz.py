import pygame

pygame.init()

SCREEN_WIDTH = 2560
SCREEN_HEIGHT = 1440

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

square_size = 10

def get_next(num: int) -> int:
    return num // 2 if num % 2 == 0 else 3 * num + 1

def create_num_squares(num: int) -> list[pygame.Rect]:
    m = num
    step = 0
    
    squares = []
    
    squares.append(pygame.Rect((step, m * square_size, square_size, square_size)))
    while m != 1:
        m = get_next(m)
        step += square_size
        squares.append(pygame.Rect((step, m * square_size, square_size, square_size)))
    
    return squares

group_squares = []

counter = 0
n = 0

run = True
pressed = False

while run:
    
    screen.fill((255, 255, 255))
    
    key = pygame.key.get_pressed()
    if key[pygame.K_ESCAPE]:
       run = False
        
    if key[pygame.K_j] and pressed != True:
        counter += 1
        pressed = True
        
    if not key[pygame.K_j]:
        pressed = False
    
    if n != counter:
        n = counter
        group_squares.append(create_num_squares(counter))
            
    for group in group_squares:
        for r in group:
            pygame.draw.rect(screen, (0, 0, 0), r)
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()
    