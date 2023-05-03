import pygame
from block import Block
from settings import *
from math import ceil
from tile import Tile

class Tetris:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        self.grid = [[0 for c in range(NUM_COLS)] for r in range(NUM_ROWS)]
        self.currentBlock = Block(self)
        self.nextBlock = Block(self)
        self.gameOver = False
        self.score = 0
        self.full_rows = [False for r in range(NUM_ROWS)]
        self.isAnimating = False
        
    def draw_grid_lines(self):
        for r in range(0, NUM_ROWS+1):
            pygame.draw.line(self.surface, LINE_COLOR, (GAME_BORDER, GAME_BORDER + r * TILE_SIZE), (WIDTH + GAME_BORDER, GAME_BORDER + r * TILE_SIZE))
            
        for c in range(0, NUM_COLS+1):
            pygame.draw.line(self.surface, LINE_COLOR, (GAME_BORDER + c * TILE_SIZE, GAME_BORDER), (GAME_BORDER + c * TILE_SIZE, HEIGHT + GAME_BORDER))
            
        
    def draw_tiles(self):
        for r in range(0, NUM_ROWS):
            for c in range(0, NUM_COLS):
                if self.grid[r][c]:
                    self.grid[r][c].draw()
                    
    def input(self, type, key):
        if type == pygame.KEYDOWN:
            if key == pygame.K_UP:
                self.currentBlock.rotate()
            
            if key == pygame.K_LEFT:
                self.currentBlock.move_left()
            
            if key == pygame.K_RIGHT:
                self.currentBlock.move_right()
            
            if key == pygame.K_DOWN:
                self.currentBlock.speed_up()
            else:
                self.currentBlock.slow_down()
        
        if type == pygame.KEYUP:
            self.currentBlock.slow_down()
    
    def place_block_in_grid(self, tiles_pos, color):
        for (r,c) in tiles_pos:
            if (self.grid[r][c]):
                print('gameover')
                self.gameOver = True
            self.grid[r][c] = Tile(r,c,color)
            
    def check_full_rows(self):
        for r, row in enumerate(self.grid):
            isFull = True
            
            for col in row:
                if not col:
                    isFull = False
                    break
                    
            self.full_rows[r] = isFull
            
            if isFull:
                self.isAnimating = True
    
    def clear_full_rows(self):
        finished = False
        
        for r in range(0, NUM_ROWS):
            if self.full_rows[r]:
                finished = self.grid[r][0].size < -5
                for c in range(0, NUM_COLS):
                    self.grid[r][c].shrink()

        if finished:
            self.move_tiles_to_bottom()
            self.get_score()
            self.full_rows = [False for r in range(NUM_ROWS)]
            self.isAnimating = False
    
    def get_score(self):
        for full_row in self.full_rows:
            if full_row:
                self.score += 40
    
    def move_tiles_to_bottom(self):
        filled_row = NUM_ROWS - 1
        r = NUM_ROWS - 1
        while r >= 0:
            if filled_row < 0:
                self.grid[r] = [0 for c in range(NUM_COLS)]
                r -= 1
                continue
            
            if not self.full_rows[filled_row]:
                self.grid[r] = self.grid[filled_row]
                for c in range(NUM_COLS):
                    if self.grid[r][c]:
                        self.grid[r][c].change_position(r,c)
                r -= 1

            filled_row -= 1
        
    def text(self, text, pos, size = 40):
        font = pygame.font.Font(FONT, size)
        text_surface = font.render(text, False, TEXT_COLOR)
        text_rect = text_surface.get_rect(midtop = pos)
        self.surface.blit(text_surface, text_rect)
        
    def display_game_stat(self):
        x = int(INFO_AREA_WIDTH/2) + WIDTH + 1.5*GAME_BORDER
        y = GAME_BORDER + 20
        self.text('Next', (x,y))
        self.text('Score', (x,y + int(HEIGHT/2)))
        self.text(str(self.score), (x, y + int(HEIGHT/2) + 60), 28)
            
    def update(self):
        self.clear_full_rows()
        self.draw_grid_lines()
        self.draw_tiles()
        self.display_game_stat()
        self.nextBlock.draw((int((ceil(NUM_COLS*2/3) - (len(self.nextBlock.shape)-1)/2)*TILE_SIZE + INFO_AREA_WIDTH/2), GAME_BORDER + 60))
        
        if self.gameOver or self.isAnimating:
            return
        
        self.currentBlock.draw()
        self.currentBlock.move_down()
        
        if self.currentBlock.freeze:
            self.place_block_in_grid(self.currentBlock.tiles_pos, self.currentBlock.color)
            self.check_full_rows()
            del self.currentBlock
            self.currentBlock = self.nextBlock
            self.nextBlock = Block(self)