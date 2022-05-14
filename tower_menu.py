import pygame
pygame.font.init()

test_img = pygame.transform.scale(pygame.image.load(r"assets/New/Towers/tower1/tower1_1.png"), (20, 20))
class Button:
    def __init__(self, menu, img, name):
        self.name = name
        self.img = img
        self.x = menu.x
        self.y = menu.y
        self.menu = menu
        self.width = self.img.get_width()
        self.height = self.img.get_height()
    
    def click(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        
    def update(self):
        self.x = self.menu.x - 50
        self.y = self.menu.y - 110

class BuyMenuButton(Button):
    def __init__(self, x, y, img, name, cost):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost
    

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
        #button_x = self.x - self.background.get_width()/2
        #button_y = self.y - 70
        self.buttons.append(Button(self, img, name))  
              
    def draw(self, window):
        window.blit(self.background, (self.x - self.background.get_width()/2, self.y - 70))
        for item in self.buttons:
            item.draw(window)
    
    def get_clicked(self, X, Y):
        for button in self.buttons:
            if button.click(X, Y):
                return button.name
        return None
    
    def update(self):
        for button in self.buttons:
            button.update()
            
class Buymenu(Towermenu):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.items = 0
        self.background = img
        self.font = pygame.font.SysFont("comicsans", 16)
    
    def add_button(self, img, name, cost):
        self.items += 1
        button_x = self.x - 200 + (self.items-1)*100
        button_y = self.y - 68
        self.buttons.append(BuyMenuButton(button_x, button_y, img, name, cost))
    
    def get_item_cost(self, name):
        for button in self.buttons:
            if button.name == name:
                return button.cost
        return -1
        
    def draw(self, window):
        window.blit(self.background, (self.x - self.background.get_width()/2, self.y-72))
        for item in self.buttons:
            item.draw(window)
            window.blit(test_img, (item.x - 5, item.y + item.height))
            text = self.font.render(str(item.cost), 1, (0,0,0))
            window.blit(text, (item.x + item.width/2 - text.get_width()/2 + 10, item.y + item.height))