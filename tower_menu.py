import pygame
pygame.font.init()

class Button:
    def __init__(self, x, y, img, name):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    
    def click(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

class Towermenu:
    def __init__(self, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.background = img
        self.font = pygame.font.SysFont("comicsans", 30)
        
    def add_button(self, img, name):
        self.items +=  1
        button_x = self.x - self.background.get_width()/2
        button_y = self.y - 70
        self.buttons.append(Button(button_x, button_y, img, name))
        
    def draw(self, window):
        window.blit(self.background, (self.x - self.background.get_width()/2, self.y - 70))
        for item in self.buttons:
            item.draw(window)
    
    def get_clicked(self, X, Y):
        for button in self.buttons:
            if button.click(X, Y):
                return button.name
        return None