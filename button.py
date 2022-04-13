import pygame

class Button():
    def __init__(self, x, y, image, scale, register):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, ((int)(width * scale), (int)(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.register = register
    
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False and self.register:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def startButton(self):
        print("test")
    
