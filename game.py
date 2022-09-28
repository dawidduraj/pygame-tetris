from email.header import Header
import pygame
import random

# tetromino class
class Tetromino:
    x = 0
    y = 0
    type = [0][0]

    # Every type of tetromino in every rotation
    types = [
        # I
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        # J 
        [[0, 4, 5, 6],   [1, 2, 5, 9], [1, 5, 9, 8], [4, 5, 6, 10]],
        # L
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],
        # O
        [[1, 2, 5, 6]],
        # S 
        [[6, 7, 9, 10], [1, 5, 6, 10]],
        # T
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        # Z 
        [[4, 5, 9, 10], [2, 6, 5, 9]]
    ]

    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
        self.type = random.randrange(0,len(self.types))
        self.color = COLORS[self.type]
        self.rotation = 0

    def display(self):
        return self.types[self.type][self.rotation]

# Tetris class
class Tetris:
    rows = 0
    columns = 0
    field = []
    score = 0
    state = "start"
    tetromino = None
    
    def __init__(self,_columns,_rows):
        self.columns = _columns
        self.rows = _rows
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
        self.spawnTetromino()
        
    def spawnTetromino(self):
            self.tetromino = Tetromino(3,0)
    
    def fall(self):
        self.tetromino.y += 1
        if self.intersects():
            self.tetromino.y -= 1
            self.freeze()

    def freeze(self):
        global gameover
        for i in range(4):
            for j in range(4):
                scan = i * 4 + j
                if scan in self.tetromino.display():
                    self.field[i + self.tetromino.y][j + self.tetromino.x] = self.tetromino.type
        self.breakLines()
        self.spawnTetromino()
        if self.intersects():
            self.state = "gameover"
            gameover = True
    
    def moveX(self,dir):
        _x = self.tetromino.x
        edge = False

        for i in range(4):
            for j in range(4):
                scan = i * 4 + j
                if scan in self.tetromino.display():
                    if j + self.tetromino.x + dir > self.columns - 1 or \
                       j + self.tetromino.x + dir < 0:
                        edge = True
        if not edge:
            self.tetromino.x += dir
        
        if self.intersects():
            self.tetromino.x = _x
        

    def rotate(self):
        _rotation = self.tetromino.rotation
        # Modulo caps the rotation between 0 and the index of the last element in the array
        self.tetromino.rotation = (self.tetromino.rotation + 1) % len(self.tetromino.types[self.tetromino.type])
        if self.intersects():
            self.tetromino.rotation = _rotation

    def intersects(self):
        for i in range(4):
            for j in range(4):
                scan = i * 4 + j
                if scan in self.tetromino.display():
                    try:
                        if i + self.tetromino.y > self.rows - 1 or \
                           i + self.tetromino.y < 0 or \
                           j + self.tetromino.x > self.columns or \
                           j + self.tetromino.x < 0 or \
                           self.field[i + self.tetromino.y][j + self.tetromino.x] >= 0:
                            return True
                    except IndexError:
                        return True
        return False

    def breakLines(self):
        lines = 0

        for i in range(1, self.rows):
            empty = 0
            for j in range(self.columns):
                if self.field[i][j] == -1:
                    empty += 1

            if empty == 0:
                lines += 1
                for i2 in range(i, 1, -1):
                    for j in range(self.columns):
                        self.field[i2][j] = self.field[i2 - 1][j]
        self.score += lines ** 2

#        lines = 0
 #       for i in range(1,self.rows):
  #          empty = 0
   #         for j in range(self.columns):
    #            if self.field[i][j] == -1:
     #               empty += 1
      #      
       #     if empty == 0:
        #        lines +=1
         #       for k in range(i, 1 -1):
          #          for j in range(self.columns):
           #             self.field[k][j] = self.field[k-1][j]
        #self.score += lines ** 2 """



# variables/constants
WIDTH = 600
HEIGHT = 660
CELLSIZE = 30
FPS = 3
COLORS = {
    "BACKGROUND": (0,0,0),
    "GRID": (128,128,128),
    "TEXT": (0,0,180),
    0: (0, 240, 240),      # cyan -> ####

    1: (0, 0, 240),        # blue   -> #
                                       ####

    2: (255, 127, 0),      # orange ->   #
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
headerFont = pygame.font.SysFont('Arial', 32, True,False)
header = headerFont.render("Tetris!", True,COLORS["TEXT"])
scoreFont = pygame.font.SysFont('Arial', 28, False,False)

def drawGrid():

    # draw empty grid
    for i in range(0, game.rows):
        for j in range(0, game.columns):
            if game.field[i][j] == -1:
                pygame.draw.rect(window, COLORS["GRID"],[ j*CELLSIZE + CELLSIZE, i*CELLSIZE + CELLSIZE, CELLSIZE, CELLSIZE],1)
            else:
                pygame.draw.rect(window, COLORS[game.field[i][j]],[ j*CELLSIZE + CELLSIZE, i*CELLSIZE + CELLSIZE, CELLSIZE, CELLSIZE])
    
    # draw tetromino
    if game.tetromino:
        for i in range(4):
            for j in range(4):
                scan = i * 4 + j
                if scan in game.tetromino.display():
                    pygame.draw.rect(window,game.tetromino.color,[ (j + game.tetromino.x)*CELLSIZE + CELLSIZE, (i + game.tetromino.y)*CELLSIZE + CELLSIZE, CELLSIZE, CELLSIZE])

# game loop
while not gameover:
    window.fill(COLORS["BACKGROUND"]) 
    if game.state == "start":
        header = headerFont.render("Tetris!", True,COLORS["TEXT"])
        game.fall()
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            gameover = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                game.moveX(1)
            if event.key == pygame.K_LEFT:
                game.moveX(-1)
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                game.fall()

    if game.state == "gameover":
        header = headerFont.render("GAME OVER!", True,COLORS["TEXT"])

    window.blit(header, [game.columns * CELLSIZE + 2 * CELLSIZE, CELLSIZE])
    scoreText = scoreFont.render("Score: " + str(game.score), True,COLORS["TEXT"])
    window.blit(scoreText, [game.columns * CELLSIZE + 2 * CELLSIZE, CELLSIZE * 2])
    drawGrid()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()