import pygame

class Tower():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.widht = 0
        self.hight = 0
        self.sell_cost = [0,0,0]
        self.cost = [0,0,0]
        self.level = 1
        self.selected = False
        self.menu = None
        self.tower_img = []

    def buyTower(self):
        pass

    def sellTower(self):
        return self.sell_cost[self.level-1]

    def upgradeTower(self, towerType):
        self.level += 1

    def uppgradeCost(self):
        return self.cost[self.level-1]

    def drawTower(self, window):
        window.blit(self.tower_img[self.level-1], (self.x-self.tower_img[self.level-1].get_width()//2, self.y-self.tower_img[self.level-1].get_height()//2))

    def clickTower(self,X,Y):
        if X <= self.x + self.widht and X >= self.x:
            if Y <= self.y + self.hight and Y >= self.y:
                return True
        return False 

    def moveTower(self,x,y):
        self.x = x
        self.y = y
