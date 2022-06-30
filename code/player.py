from settings import *
import pygame
import math


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGEL

    def movement(self):
        pass

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y
        