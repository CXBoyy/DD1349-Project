from asyncio.proactor_events import _ProactorBaseWritePipeTransport
import pygame
from .tower import Tower 
import math

class basictower(Tower):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.tower_img = []
        self.basic_imgs = []
        self.basic_count = 0
        self.range = 200
        self.width = self.height = 60
        self.enemy_is_in_range = False
        self.cooldown = 90
        self.in_range = False
        self.moving = False
        self.name = "buy_tower1"
        self.damage = 2

        for x in range(1,9):
            self.tower_img.append(pygame.transform.scale(pygame.image.load(r"assets/New/Towers/tower1/tower1_1.png"), (64, 64)))
        
        self.tower_rect = self.tower_img[0].get_rect()
        print("Tower coordinates: ", (self.x, self.y))
        self.tower_rect.topleft = (self.x, self.y)
        print("Rect: " ,self.tower_rect)

    def draw(self, window):
        super().draw_radius(window)
        super().drawTower(window)
        
        if self.basic_count >= len(self.basic_imgs):
            self.basic_count = 0
        # window.blit(self.basic_imgs[self.basic_count], ((self.x + self.width/2) - (self.basic_imgs[self.basic_count].get_width()/2), (self.y - (self.basic_imgs[self.basic_count].height()))))
        self.basic_count += 1

    def change_range(self, r):
        self.range = r
        
     
    #def attack(self, enemies):
    #    pass
    #     self.in_range = False
    #     enemy_closest = []
    #     for enemy in enemies:
    #         #x = enemy_x
    #         #y = enemy_y
    #         dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
    #         if dis < self.range:
    #             self.in_range = True
    #             enemy_closest.append(enemy)
    #     enemy_closest.sort(key=lambda x: x.x)
    #     first_enemy = enemy_closest[0]
            
               
        

