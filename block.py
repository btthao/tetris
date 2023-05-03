import pygame
from settings import *
from random import randrange

class Block:
    def __init__(self, game):
        choice = randrange(len(SHAPES))
        self.game = game
        self.shape = SHAPES[choice]
        self.color = COLORS[choice]
        self.startPoint = pygame.math.Vector2(GAME_BORDER + TILE_SIZE * int(NUM_COLS//3), GAME_BORDER)
        self.surface = pygame.display.get_surface()
        self.lastMoveTime = pygame.time.get_ticks()
        self.cooldown = COOLDOWN_PERIOD
        self.freeze = False
        self.tiles_pos = self.get_tiles_pos()
    
    def __del__(self):
      print('Object gets destroyed')

    def draw(self, offset = (0,0)):
        for (r,c) in self.tiles_pos:
            left = GAME_BORDER + c*TILE_SIZE + TILE_BORDER + offset[0]
            top = GAME_BORDER + r*TILE_SIZE + TILE_BORDER + offset[1]
            size = TILE_SIZE - TILE_BORDER
            block_rect = pygame.Rect(left, top, size, size)
            pygame.draw.rect(self.surface, self.color, block_rect)

    
    def rotate(self):
        if self.freeze:
            return

        newShape = [list(row) for row in zip(*self.shape[::-1])]
        newTilesPos = self.get_tiles_pos(newShape)
        
        if not self.check_collision(newTilesPos):
            self.shape = newShape
            self.tiles_pos = newTilesPos
    
    def check_collision(self, tilesPos = None):
        if tilesPos == None:
            tilesPos = self.tiles_pos
            
        for (row,col) in tilesPos:
            if col < 0 or col >= NUM_COLS or row < 0 or row >= NUM_ROWS or self.game.grid[row][col]:
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
                if col <= 0 or self.game.grid[row][col-1]:
                    return False
            if direction == 'right':
                if col >= NUM_COLS - 1 or self.game.grid[row][col+1]:
                    return False
            if direction == 'down':
                if row >= NUM_ROWS - 1 or self.game.grid[row+1][col]:
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
    
    def speed_up(self):
        self.cooldown = int(COOLDOWN_PERIOD/10)
        
    def slow_down(self):
        self.cooldown = COOLDOWN_PERIOD
