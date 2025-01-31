import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice

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
        #生成地图
        layout = {
            'boundary': import_csv_layout('map\map_FloorBlocks.csv'),
            'grass': import_csv_layout('map\map_Grass.csv'),
            'ojects': import_csv_layout('map\map_Objects.csv'),
        }
        graphics = {
            'grass': import_folder('graphics\grass'),
            'objects': import_folder('graphics\objects'),
        }
        for style,layout in layout.items():
            for row_index,row in enumerate(layout):
                for col_index,col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y), [self.obstacle_sprites],'invisible',surface = pygame.Surface((TILESIZE, TILESIZE)))
                        if style == 'grass':
                            #渲染草皮
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),[self.visble_sprites,self.obstacle_sprites],'grass',surface = random_grass_image)
                        if style == 'objects':
                            #渲染物体
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visble_sprites,self.obstacle_sprites],'objects',surf)
            #     if col == 'x':
            #         Tile((x,y),[self.visble_sprites,self.obstacle_sprites])
            #     if col == 'p':
                    # self.player = Player((x,y),[self.visble_sprites],self.obstacle_sprites)
        self.player = Player((x,y),[self.visble_sprites],self.obstacle_sprites)

    def run(self):
        #更新以及绘制游戏
        self.visble_sprites.custom_draw(self.player)
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

        #创造地板
        self.floor_surf = pygame.image.load('C:/Users/86136/Desktop/A Game like Zelda/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0,0))

    def custom_draw(self,player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        # 渲染地板
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)

        # for sprite in self.sprites():
        # 确保靠近屏幕底部的精灵出现在更高位置的精灵前面
        for sprite in sorted(self.sprites(),key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)
