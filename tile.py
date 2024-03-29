import pygame
from settings import *

class Tile():
    def __init__(self, r, c, color):
        self.surface = pygame.display.get_surface()
        self.size = TILE_SIZE - TILE_BORDER
        self.color = color
        self.update_position(r, c)

    def draw(self):
        tile_rect = pygame.Rect(self.left, self.top, self.size, self.size)
        pygame.draw.rect(self.surface, self.color, tile_rect)
        
    def shrink(self):
        self.left += 1
        self.top += 1
        self.size -= 2
        
    def update_position(self, r, c):
        self.left = GAME_BORDER + c*TILE_SIZE + TILE_BORDER
        self.top = GAME_BORDER + r*TILE_SIZE + TILE_BORDER
    