from platform import node
import pygame
import copy
import numpy as np
import operator
import time
from math import cos, sin, atan2, degrees

def normalize(e1, e2):
        vector = (e1, e2)
        norm = np.linalg.norm(vector)
        newVector = (vector[0] / norm, vector[1] / norm)
        return newVector

class Enemy(pygame.sprite.Sprite):
    imgs = []
    
    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        super().__init__()
        
        self.x = x                                                              # Position of
        self.y = y                                                              # the enemy.
    
        self.width = width                                                      # Size of the
        self.height = height                                                    # enemy image.
        self.window = window
        self.image = None
        self.rect = None
        self.path = copy.deepcopy(path)
        self.currentPathNodePos = 0
        self.pathEnd = pathEnd
        self.animation_count = 0
        self.distanceTraveled = 0
        self.directionalVector = normalize(self.path[1][0] - self.x, self.path[1][1] - self.y)       # Setting the starting directional vector
        self.game = game
        
        self.default_health = 6                                                 # To be set individually for each enemy type
        self.health = self.default_health                                       # To be set individually for each enemy type
        self.speed = 1                                                          # To be set individually for each enemy type
        self.reward = 0                                                         # To be set individually for each enemy type
        self.dead = False
        self.out_of_bounds = False
        self.angle1 = atan2(self.directionalVector[1], self.directionalVector[0])
    
    """ Draws the enemy.
    """  
    def update(self):
        if (self.x, self.y) >= self.pathEnd:
            self.game.health -= 1
            self.out_of_bounds = True
            # Remove enemy from the map and take away one life
            # return True                                                   # Maybe use this to signal that the enemy should be removed from the map?
        else:
            index = self.animation_count // len(self.imgs)
            self.image = self.imgs[index]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            nodeVector = self.move()
            angle2 = atan2(nodeVector[1], nodeVector[0])
            one_degree_in_radian = (np.pi)/180
            angle1_deg = degrees(atan2(self.directionalVector[1], self.directionalVector[0]))
            angle2_deg = degrees(atan2(nodeVector[1], nodeVector[0]))
            if self.angle1 != angle2:
                diff = (angle2 - self.angle1)/5
                self.angle1 += diff
                self.rotate(degrees(-self.angle1))
            else:
                pass
                
            self.display_health(self.window)
            self.animation_count += 1
            if self.animation_count >= len(self.imgs):
                self.animation_count = 0
        
    
    """ Returns true if the enemy was hit
    :return: Bool
    """
    def collide(self, x, y):
        if x <= self.x + self.width and x >= self.x:                  # Hitbox of the
            if y <= self.y + self.height and y >= self.y:             # enemy unit.
                return True
        else:
            return False
    
    def move(self):
       
        x1, y1 = self.path[self.currentPathNodePos][0], self.path[self.currentPathNodePos][1]
        x2, y2 = self.path[self.currentPathNodePos + 1][0], self.path[self.currentPathNodePos + 1][1]
        distanceBetweenPoints = np.hypot((x2-x1), (y2-y1))
        nodeVector = normalize(x2-x1, y2-y1)
        new_x, new_y = (self.x + nodeVector[0] * self.speed, self.y + nodeVector[1] * self.speed)
        self.distanceTraveled += np.hypot((new_x-self.x), (new_y - self.y))
        self.x, self.y = new_x, new_y
        
        if self.distanceTraveled >= distanceBetweenPoints:                           # check if we have passed the point
            self.currentPathNodePos += 1
            self.distanceTraveled = 0
        
        return nodeVector
    
    # Returns true if the enemy has died.
    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.dead = True
        
    def rotate(self, angle):
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect.center = old_center
    
    def display_health(self, window):
        bar_x, bar_y = (self.x - 32), (self.rect.center[1] - 45)
        length, width = 64, 10
        increment = length / self.default_health
        pygame.draw.rect(window, (255, 0, 0), (bar_x, bar_y, length, width), 0)
        pygame.draw.rect(window, (0, 255, 0), (bar_x, bar_y, increment * self.health, width), 0)
        
        
        