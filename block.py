import pygame
from settings import *
from random import randrange

class Block:
    def __init__(self):
        choice = randrange(len(SHAPES))
        self.shape = SHAPES[choice]
        self.color = COLORS[choice]
        self.rotatedShapes = self.create_block_rotations()
        self.index = 0
        self.startPoint = pygame.math.Vector2(BORDER_WIDTH + TILE_SIZE * 3, BORDER_WIDTH)
        self.surface = pygame.display.get_surface()
        self.offset = 1
        self.size = TILE_SIZE - self.offset

    def draw(self):
        block = self.rotatedShapes[self.index]
        
        for r, row in enumerate(block):
            for c, val in enumerate(row):
                if val == 1:
                    block_rect = pygame.Rect(self.startPoint[0] + c*TILE_SIZE + self.offset, self.startPoint[1] + r*TILE_SIZE + self.offset, self.size, self.size)
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
        self.index += 1
        
        if self.index > 3:
            self.index = 0
    def move_left(self):
        self.startPoint -= (TILE_SIZE, 0)
        
    def move_right(self):
        self.startPoint += (TILE_SIZE, 0)
