import pygame
from settings import *

class Tile():
    def __init__(self, r, c, color):
        self.left = GAME_BORDER + c*TILE_SIZE + TILE_BORDER
        self.top = GAME_BORDER + r*TILE_SIZE + TILE_BORDER
        self.size = TILE_SIZE - TILE_BORDER
        self.color = color
        self.surface = pygame.display.get_surface()

    def draw(self):
        block_rect = pygame.Rect(self.left, self.top, self.size, self.size)
        pygame.draw.rect(self.surface, self.color, block_rect)
        
    def shrink(self):
        self.left += 1
        self.top += 1
        self.size -= 2
        
    def change_position(self, r, c):
        self.left = GAME_BORDER + c*TILE_SIZE + TILE_BORDER
        self.top = GAME_BORDER + r*TILE_SIZE + TILE_BORDER
    