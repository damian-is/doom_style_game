from re import S
import pygame
from settings import *


class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = self.game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/sky.png', (WIDHT, HALF_HEIGHT))
        self.sky_offset = 0

    def draw(self):
        self.draw_background()
        self.render_game_objects()

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDHT
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDHT, 0))
        
        # floor
        pygame.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDHT, HEIGHT))

    def render_game_objects(self):
        list_objects = self.game.raycasting.object_to_render
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res = (TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pygame.image.load(path).convert_alpha()
        return pygame.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png')
        }