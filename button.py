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
    
    def draw(self, surface:pygame.Surface):
        #surface.blit(self.image, (self.rect.x, self.rect.y))
        surface.blit(self.image, (self.rect.topleft))
        
    def check_button_actions(self, pos, event):
        if self.rect.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                print("in here")
                self.clicked = True
        
    
