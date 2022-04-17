import pygame
import time

class Enemy():
    imgs = []
    
    def __init__(self, window, x, y, width, height, path):
        self.enemyX = x                                                         # Position of
        self.enemyY = y                                                         # the enemy.
    
        self.width = width                                                      # Size of the
        self.height = height                                                    # enemy image.
        self.health = 1
        self.window = window
        self.img = None
        #self.img = pygame.draw.circle(self.window, (255, 0, 0), (x, y), 5, 0)
        self.speed = 0
        self.path = path
        self.animation_count = 0
        #TODO: Path
      
    """ Draws the enemy.
    """  
    def draw(self, window:pygame.Surface, x, y):
        #window.blit(self.img, (x, y))
        pygame.draw.circle(window, (255, 0, 0), (x, y), 5, 0)
        pygame.display.update()
        self.enemyX = x
        self.enemyY = y
        
    
    """ Returns true if the enemy was hit
    :return: Bool
    """
    def collide(self, x, y):
        if x <= self.enemyX + self.width and x >= self.enemyX:                  # Hitbox of the
            if y <= self.enemyY + self.height and y >= self.enemyY:             # enemy unit.
                return True
        else:
            return False
    
    def move(self, window:pygame.Surface, targetX, targetY):
        while(self.enemyX != targetX or self.enemyY != targetY):
            time.sleep(0.01)
            if self.enemyX < targetX:
                if self.enemyY < targetY:
                    self.draw(window, self.enemyX + 1, self.enemyY + 1)
                elif self.enemyY > targetY:
                    self.draw(window, self.enemyX + 1, self.enemyY - 1)
                else:
                    self.draw(window, self.enemyX + 1, self.enemyY)
            elif self.enemyX > targetX:
                if self.enemyY < targetY:
                    self.draw(window, self.enemyX - 1, self.enemyY + 1)
                elif self.enemyY > targetY:
                    self.draw(window, self.enemyX - 1, self.enemyY - 1)
                else:
                    self.draw(window, self.enemyX - 1, self.enemyY)
            else:
                if self.enemyY < targetY:
                    self.draw(window, self.enemyX, self.enemyY + 1)
                elif self.enemyY > targetY:
                    self.draw(window, self.enemyX, self.enemyY - 1)
                else:
                    self.draw(window, self.enemyX, self.enemyY)
            # print("\nx pos: " + str(self.enemyX))
            # print("\ny pos: " + str(self.enemyY))
            # print("\ntarget x pos: " + str(targetX))
            # print("\ntarget y pos: " + str(targetY))
    
    # Returns true if the enemy has died.
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True