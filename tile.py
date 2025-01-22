import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups,sprite_type,surface = pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        # self.image = pygame.image.load('C:/Users/86136/Desktop/A Game like Zelda/graphics/test/rock.png').convert_alpha()
        self.image = surface
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        # self.hitbox.topleft = self.rect.topleft + pygame.math.Vector2(0,10)