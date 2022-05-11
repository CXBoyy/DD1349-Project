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
        self.moving_tower = False
        self.target = None

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
            
    def attack(self, )

    def draw_radius(self, window):
        if self.selected:
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            window.blit(surface, ((self.x + (self.width/2)) - self.range, (self.y + (self.height/2)) - self.range))

    def check_tower_actions(self, pos : tuple, event : pygame.event):
        
        if self.tower_rect.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:                   # Right mouse click
                    if self.selected is False:
                        print("Showing radius")
                        self.selected = True
                        return self
                                    
                    elif self.selected is True:
                        print("Not showing radius")
                        self.selected = False
                        return None
        
                if event.button == 1:                   # Left mouse click
                    print("\nClicked")
                    if self.moving_tower is True:
                        self.moving_tower = False
                        return None
                    elif self.moving_tower is False:
                        self.moving_tower = True
                        return self
                
        if not self.tower_rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if self.selected is True:
                self.selected = False
                return None
            
        else:
            return False

    def moveTower(self,x,y):
        self.x = x
        self.y = y
        self.tower_rect.topleft = (x, y)
        
        
        
