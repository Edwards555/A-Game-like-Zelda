import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug

class Level:
    def __init__(self):
        #获取展示屏幕
        self.display_surface = pygame.display.get_surface()

        #设置精灵组别
        self.visble_sprites = YSortCameraGroup()
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
                    self.player = Player((x,y),[self.visble_sprites],self.obstacle_sprites)

    def run(self):
        #更新以及绘制游戏
        self.visble_sprites.custom.draw(self.player)
        self.visble_sprites.update()
        debug(self.player.direction)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        #初始化
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2

    def custom_draw(self,player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
