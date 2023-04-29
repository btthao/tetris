import pygame
from block import Block
from settings import *

class Tetris:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.nextBlock = Block()
    
    def draw_grid(self):
        for r in range(0, NUM_ROWS+1):
            pygame.draw.line(self.surface, LINE_COLOR, (BORDER_WIDTH, BORDER_WIDTH + r * TILE_SIZE), (WIDTH + BORDER_WIDTH, BORDER_WIDTH + r * TILE_SIZE))
            
        for c in range(0, NUM_COLS+1):
            pygame.draw.line(self.surface, LINE_COLOR, (BORDER_WIDTH + c * TILE_SIZE, BORDER_WIDTH), (BORDER_WIDTH + c * TILE_SIZE, HEIGHT + BORDER_WIDTH))
            
    def rotate(self):
        self.nextBlock.rotate()
        
    def play(self):
        self.draw_grid()
        self.nextBlock.draw()