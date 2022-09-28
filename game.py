import pygame

# variables/constants
WIDTH = 300
HEIGHT = 600
FPS = 20

gameover = False

# setup
pygame.init()
pygame.display.set_caption("Tetris 🕹️")
window = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()

# game loop
while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    
    clock.tick(FPS)

pygame.quit()