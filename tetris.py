import pygame
from block import Block
from settings import *

class Tetris:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.grid = [[0 for c in range(NUM_COLS)] for r in range(NUM_ROWS)]
        self.currentBlock = Block(self.grid)
        
    def draw_grid(self):
        for r in range(0, NUM_ROWS+1):
            pygame.draw.line(self.surface, LINE_COLOR, (GAME_BORDER, GAME_BORDER + r * TILE_SIZE), (WIDTH + GAME_BORDER, GAME_BORDER + r * TILE_SIZE))
            
        for c in range(0, NUM_COLS+1):
            pygame.draw.line(self.surface, LINE_COLOR, (GAME_BORDER + c * TILE_SIZE, GAME_BORDER), (GAME_BORDER + c * TILE_SIZE, HEIGHT + GAME_BORDER))
            
        
    def fill_blocks(self):
        for r in range(0, NUM_ROWS):
            for c in range(0, NUM_COLS):
                if self.grid[r][c]:
                    left = GAME_BORDER + c*TILE_SIZE + TILE_BORDER
                    top = GAME_BORDER + r*TILE_SIZE + TILE_BORDER
                    size = TILE_SIZE - TILE_BORDER
                    color = self.grid[r][c]
                    block_rect = pygame.Rect(left, top, size, size)
                    pygame.draw.rect(self.surface, color, block_rect)
                    
    def input(self, key):
        
        if key == pygame.K_UP:
            self.currentBlock.rotate()
        
        if key == pygame.K_LEFT:
            self.currentBlock.move_left()
        
        if key == pygame.K_RIGHT:
            self.currentBlock.move_right()
    
    def update_grid(self, tiles_pos, color):
        for (r,c) in tiles_pos:
            self.grid[r][c] = color
            
    def update(self):
        self.draw_grid()
        self.fill_blocks()
        self.currentBlock.draw()
        
        if self.currentBlock.collided:
            self.update_grid(self.currentBlock.tiles_pos, self.currentBlock.color)
            del self.currentBlock
            self.currentBlock = Block(self.grid)