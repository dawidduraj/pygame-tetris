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
        
        # testing
        self.field[1][3] = 1

# variables/constants
WIDTH = 600
HEIGHT = 660
CELLSIZE = 30
FPS = 20
COLORS = {
    "BACKGROUND": (0,0,0),
    "GRID": (128,128,128),
    0: (0, 240, 240),      # cyan -> ####

    1: (0, 0, 240),        # blue   -> #
                                       ####

    2: (240, 0, 160),      # orange ->   #
                                       ###

    3: (240, 240, 0),      # yellow ->  ##
                                        ##

    4: (0, 240, 0),        # green ->   ##
                                       ##

    5: (160, 0, 240),      # purple ->   #
                                       ###

    6: (240, 0, 0),        # red -> ##
                                     ##
}

game = Tetris(10,20)
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

    window.fill(COLORS["BACKGROUND"])

    # draw grid
    for i in range(0, game.rows):
        for j in range(0, game.columns):
            if game.field[i][j] == -1:
                pygame.draw.rect(window, COLORS["GRID"],[ i*CELLSIZE + CELLSIZE, j*CELLSIZE + CELLSIZE, CELLSIZE, CELLSIZE],1)
            else:
                pygame.draw.rect(window, COLORS[game.field[i][j]],[ i*CELLSIZE + CELLSIZE, j*CELLSIZE + CELLSIZE, CELLSIZE, CELLSIZE])
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()