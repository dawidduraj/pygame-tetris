import pygame

# Tetris class
class Tetris:
    rows = 0
    columns = 0
    field = []
    score = 0
    state = "start"
    
    def __init__(self, _rows, _columns):
        self.rows = _rows
        self.columns = _columns
        self.field = []
        self.score = 0
        self.state = "start"

        # create empty field
        for i in range(_rows):
            row = []
            for j in range(_columns):
                # empty field is defined with -1
                row.append(-1)
            self.field.append(row)

# variables/constants
WIDTH = 300
HEIGHT = 600
FPS = 20

game = Tetris()
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