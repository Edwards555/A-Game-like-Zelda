import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        #获取展示屏幕
        self.display_surface = pygame.display.get_surface()

        #设置精灵组别
        self.visble_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        #生成地图
        self.create_map()

    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            # print(row_index)
            # print(row)
            for col_index,col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'x':
                    Tile((x,y),[self.visble_sprites,self.obstacle_sprites])
                if col == 'p':
                    self.player = Player((x,y),[self.visble_sprites])

    def run(self):
        #更新以及绘制游戏
        self.visble_sprites.draw(self.display_surface)
