import pygame

class Tower():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 0
        self.hight = 0
        self.sell_cost = [0,0,0]
        self.cost = [0,0,0]
        self.level = 1
        self.damage = 1
        self.selected = False
        self.menu = None
        self.tower_img = []

    def buyTower(self):
        pass

    def sellTower(self):
        return self.sell_cost[self.level-1]

    def upgradeTower(self, towerType):
        self.level += 1
        self.damage += 1

    def uppgradeCost(self):
        return self.cost[self.level-1]

    def drawTower(self, window):
        window.blit(self.tower_img[self.level-1], (self.x-self.tower_img[self.level-1].get_width()//2, self.y-self.tower_img[self.level-1].get_height()//2))

    def draw_radius(self, window):
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
        window.blit(surface, (self.x - self.range, self.y - self.range))

    def clickTower(self, X, Y):
        img = self.tower_img[self.level - 1]
        if X <= self.x - img.get_width() + self.width and X >= self.x - img.get_width():
            if Y <= self.y + self.height - img.get_height() and Y >= self.y - img.get_height():
                return True
        return False

    def moveTower(self,x,y):
        self.x = x
        self.y = y
        
