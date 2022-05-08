import pygame
from tower_menu import Towermenu

menu_bg = pygame.image.load(r"assets/New/menu_test_1.png")
upgrade_button = pygame.image.load(r"assets/New/button_test_1.png")

class Tower():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.sell_cost = [0,0,0]
        self.cost = [0,0,0]
        self.level = 1
        self.damage = 1
        self.selected = False
        self.menu = Towermenu(self.x, self.y, menu_bg)
        self.menu.add_button(upgrade_button, "Upgrade")
        self.tower_img = []
        self.range = 10
        self.tower_rect = None

    def buyTower(self):
        pass

    def sellTower(self):
        return self.sell_cost[self.level-1]

    def upgradeTower(self, towerType):
        self.level += 1
        self.damage += 1

    def uppgradeCost(self):
        return self.cost[self.level-1]
     
    def drawTower(self, window : pygame.Surface):
        #window.blit(self.tower_img[self.level-1], (self.x-self.tower_img[self.level-1].get_width()//2, self.y-self.tower_img[self.level-1].get_height()//2))
        window.blit(self.tower_img[self.level-1], (self.x, self.y))
        
        if self.selected:
            self.menu.draw(window)

    def draw_radius(self, window):
        if self.selected:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            print("Height and width: ", self.width, self.height)
            window.blit(surface, ((self.x + (self.width/2)) - self.range, (self.y + (self.height/2)) - self.range))

    def check_tower_actions(self, pos : tuple, event : pygame.event):
        # if X <= self.x - self.tower_img[self.level-1].get_width()//2 + self.width and X >= self.x - self.tower_img[self.level-1].get_width()//2:
        #     if Y <= self.y + self.height - self.tower_img[self.level-1].get_height()//2 and Y >= self.y - self.tower_img[self.level-1].get_height()//2:
        #         return True
        # return False
        
        # if self.tower_rect.collidepoint((X, Y)):
        #     return True
        # else:
        #     return False
        
        # Define this method in sub classes
        pass

    def moveTower(self,x,y):
        self.x = x
        self.y = y
        
