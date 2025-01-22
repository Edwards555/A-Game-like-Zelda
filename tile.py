import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('C:/Users/86136/Desktop/A Game like Zelda/graphics/test/rock.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,-10)
        # self.hitbox.topleft = self.rect.topleft + pygame.math.Vector2(0,10)