from tkinter import W
import pygame

class Enemy():
    imgs = []
    
    def __init__(self, x, y, width, height):
        self.enemyX = x                                                         # Position of
        self.enemyY = y                                                         # the enemy.
        
        self.width = width                                                      # Size of the
        self.height = height                                                    # enemy image.
        self.health = 1
        self.img = None
        #TODO: Path
      
    """ Draws the enemy.
    """  
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
        self.move()
    
    """ Returns true if the enemy was hit
    :return: Bool
    """
    def collide(self, x, y):
        if x <= self.enemyX + self.width and x >= self.enemyX:                  # Hitbox of the
            if y <= self.enemyY + self.height and y >= self.enemyY:             # enemy unit.
                return True
        else:
            return False
    
    def move(self):
        pass
    
    # Returns true if the enemy has died.
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True