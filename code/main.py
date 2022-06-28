import pygame
import sys
from settings import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()

    def new_game(self):
        pass

    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.screen.fill('black')

    def check_events(self):
        pass
    
    def run(self):
        while True:
            self.update()
            self.draw()