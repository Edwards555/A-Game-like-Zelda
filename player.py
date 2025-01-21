import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('C:/Users/86136/Desktop/A Game like Zelda/graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()
        #上下左右
        if keys[pygame.K_UP]:
            self.direction.y = -1
            print('up')
        elif keys[pygame.K_DOWN]:
            self.direction.y =  1
            print('down')
        else:
            self.direction =  0
        if keys[pygame.K_RIGHT]:
            self.direction.x =  1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction =  0

        def update(self):
            self.visble_sprites.draw(self.display_surface)
            self.visble_sprites.update()