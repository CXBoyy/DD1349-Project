import pygame
import copy

class Enemy():
    imgs = []
    
    def __init__(self, window, x, y, width, height, path, pathDict, pathEnd):
        self.x = x                                                              # Position of
        self.y = y                                                              # the enemy.
    
        self.width = width                                                      # Size of the
        self.height = height                                                    # enemy image.
        self.health = 1
        self.window = window
        self.img = None
        self.speed = 1                                                          # amount of pixels the enemy can move per frame, might have to be changed because this is probably too fast.
        self.path = copy.deepcopy(path)
        self.currentPos = self.path.pop()
        self.pathDict = copy.deepcopy(pathDict)
        self.pathEnd = pathEnd
        self.animation_count = 0
        #TODO: Path
      
    """ Draws the enemy.
    """  
    def draw(self):
        if (self.x, self.y) == self.pathEnd:
            print("Lost one life")
            # Remove enemey from the map and take away one life
        else:
            self.move()
            pygame.draw.circle(self.window, (255, 0, 0), (self.x, self.y), 5, 0)
            pygame.display.update()
        
    
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
        if self.pathDict[self.currentPos] and len(self.path) != 0:
            self.currentPos = self.path.pop()
        targetX = self.currentPos[0]
        targetY = self.currentPos[1]
        if not self.pathDict[self.currentPos]:
            if self.x < targetX:
                if self.x + self.speed <= targetX:
                    self.x += self.speed
                else:
                    self.x = targetX
            elif self.x > targetX:
                if self.x - self.speed >= targetX:
                    self.x -= self.speed
                else:
                    self.x = targetX
            if self.y < targetY:
                if self.y + self.speed <= targetY:
                    self.y += self.speed
                else:
                    self.y = targetY
            elif self.y > targetY:
                if self.y - self.speed >= targetY:
                    self.y -= self.speed
                else:
                    self.y = targetY
        if self.x == targetX and self.y == targetY:
            self.pathDict[self.currentPos] = True
    
    # Returns true if the enemy has died.
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True