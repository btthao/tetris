import pygame, sys
from settings import *
from tetris import Tetris

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH + INFO_AREA_WIDTH + 2*BORDER_WIDTH, HEIGHT+ 2*BORDER_WIDTH))
        pygame.display.set_caption('Tetris')
        self.clock = pygame.time.Clock()
        self.tetris = Tetris()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(BG_COLOR)
            self.tetris.play()
            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()