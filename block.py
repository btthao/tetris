import pygame
from settings import *
from random import randrange

class Block:
    def __init__(self, grid):
        self.grid = grid
        choice = randrange(len(SHAPES))
        self.shape = SHAPES[choice]
        self.color = COLORS[choice]
        self.rotatedShapes = self.create_block_rotations()
        self.index = 0
        self.startPoint = pygame.math.Vector2(GAME_BORDER + TILE_SIZE * 3, GAME_BORDER)
        self.surface = pygame.display.get_surface()
        self.lastMoveTime = pygame.time.get_ticks()
        self.cooldown = 500
        self.speed = (0, TILE_SIZE)
        self.collided = False
        self.tiles_pos = []

    def draw(self):
        if self.collided:
            return

        self.move_down()
        
        for r, row in enumerate(self.shape):
            for c, val in enumerate(row):
                if val == 1:
                    left = self.startPoint[0] + c*TILE_SIZE + TILE_BORDER
                    top = self.startPoint[1] + r*TILE_SIZE + TILE_BORDER
                    size = TILE_SIZE - TILE_BORDER
                    block_rect = pygame.Rect(left, top, size, size)
                    pygame.draw.rect(self.surface, self.color, block_rect)

    def create_block_rotations(self):
        rotations = [self.shape]
        curr = self.shape
        
        for i in range(3):
            rotated_right_shape = [list(row) for row in zip(*curr[::-1])]
            rotations.append(rotated_right_shape)
            curr = rotated_right_shape

        return rotations
    
    def rotate(self):
        if self.collided:
            return
        
        self.index += 1
        
        if self.index > 3:
            self.index = 0
        
        self.shape = self.rotatedShapes[self.index]
    
    def check_collision(self):
        for (row,col) in self.tiles_pos:
            if row + 1 >= len(self.grid) or self.grid[row+1][col]:
                self.collided = True
                print('collided')
    
    def update_tiles_pos(self): 
        pos = []
        
        for i, _ in enumerate(self.shape):
            for j, val in enumerate(self.shape[i]):
                if val == 1:
                    row = int((self.startPoint[1] + i*TILE_SIZE - GAME_BORDER) / TILE_SIZE)
                    col = int((self.startPoint[0] + j*TILE_SIZE - GAME_BORDER) / TILE_SIZE)
                    pos.append((row,col))
        
        self.tiles_pos = pos
    def move_down(self):
        if self.collided:
            return
        
        now = pygame.time.get_ticks()

        if now - self.lastMoveTime >= self.cooldown:
            self.lastMoveTime = now
            self.startPoint += self.speed
            self.update_tiles_pos()
            self.check_collision()
            
    def move_left(self):
        if self.collided:
            return
        self.startPoint -= (TILE_SIZE, 0)
        
    def move_right(self):
        if self.collided:
            return
        self.startPoint += (TILE_SIZE, 0)
