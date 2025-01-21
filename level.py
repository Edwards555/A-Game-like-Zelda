import pygame

class Level:
    def __init__(self):
        #获取展示屏幕
        self.display_surface = pygame.display.get_surface()
        #设置精灵组别
        self.visble_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    def run(self):
        #更新以及绘制游戏
        pass
