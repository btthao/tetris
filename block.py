import pygame
from settings import *
from random import randrange

class Block:
    def __init__(self, grid):
        choice = randrange(len(SHAPES))
        self.grid = grid
        self.shape = SHAPES[choice]
        self.color = COLORS[choice]
        self.rotatedShapes = self.create_block_rotations()
        self.index = 0
        self.startPoint = pygame.math.Vector2(GAME_BORDER + TILE_SIZE * int(NUM_COLS//3), GAME_BORDER)
        self.surface = pygame.display.get_surface()
        self.lastMoveTime = pygame.time.get_ticks()
        self.cooldown = 500
        self.freeze = False
        self.tiles_pos = self.get_tiles_pos()
    
    def __del__(self):
      print('Object gets destroyed')

    def draw(self):
        for (r,c) in self.tiles_pos:
            left = GAME_BORDER + c*TILE_SIZE + TILE_BORDER
            top = GAME_BORDER + r*TILE_SIZE + TILE_BORDER
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
        if self.freeze:
            return

        newIdx = self.index + 1
        
        if newIdx > 3:
            newIdx = 0
        
        newTilesPos = self.get_tiles_pos(self.rotatedShapes[newIdx])
        
        if not self.check_collision(newTilesPos):
            self.index = newIdx
            self.shape = self.rotatedShapes[newIdx]
            self.tiles_pos = newTilesPos
    
    def check_collision(self, tilesPos = None):
        if tilesPos == None:
            tilesPos = self.tiles_pos
            
        for (row,col) in tilesPos:
            if col < 0 or col >= NUM_COLS or row < 0 or row >= NUM_ROWS or self.grid[row][col]:
                return True
        
        return False
    
    def get_tiles_pos(self, shape = None): 
        if shape == None:
            shape = self.shape
            
        pos = []
        
        for i, row in enumerate(shape):
            for j, val in enumerate(row):
                if val == 1:
                    r = int((self.startPoint[1] + i*TILE_SIZE - GAME_BORDER) / TILE_SIZE)
                    c = int((self.startPoint[0] + j*TILE_SIZE - GAME_BORDER) / TILE_SIZE)
                    pos.append((r, c))
        
        return pos
    
    def check_can_move(self, direction):
        for (row,col) in self.tiles_pos:
            if direction == 'left':
                if col <= 0 or self.grid[row][col-1]:
                    return False
            if direction == 'right':
                if col >= NUM_COLS - 1 or self.grid[row][col+1]:
                    return False
            if direction == 'down':
                if row >= NUM_ROWS - 1 or self.grid[row+1][col]:
                    return False
        return True
    
    def move_down(self):
        if pygame.time.get_ticks() - self.lastMoveTime >= self.cooldown:
            if not self.check_can_move('down'):
                self.freeze = True
                return
            self.move_block(DOWN_MOVE)
            
    def move_left(self):
        if self.check_can_move('left'):
            self.move_block(LEFT_MOVE)
        
    def move_right(self):
        if self.check_can_move('right'):
            self.move_block(RIGHT_MOVE)
            
    def move_block(self, direction):
        if self.freeze:
            return

        self.lastMoveTime = pygame.time.get_ticks()
        self.startPoint += direction
        self.tiles_pos = self.get_tiles_pos()
        # self.check_collision()
