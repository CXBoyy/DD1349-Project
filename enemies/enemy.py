import pygame
import copy
import numpy as np
import operator
import time
from math import cos, sin

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
        self.dead = False
    
    """ Draws the enemy.
    """  
    def update(self):
        if (self.x, self.y) >= self.pathEnd:
            print("Lost one life")
            self.game.health -= 1
            self.dead = True
            # Remove enemy from the map and take away one life
            # return True                                                   # Maybe use this to signal that the enemy should be removed from the map?
        else:
            index = self.animation_count // len(self.imgs)
            self.image = self.imgs[index]
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            nodeVector = self.move()
            factor1 = np.around(nodeVector[0] * self.directionalVector[1], 2)
            factor2 = np.around(nodeVector[1] * self.directionalVector[0], 2)
            #print("\nFactors: ", factor1, factor2)
            #print(self.directionalVector)
            #print("\nVectors: ", nodeVector, self.directionalVector)
            if factor1 != factor2:
                self.rotate(nodeVector)
            #pygame.Surface.blit(self.window, self.image, (self.x-60, self.y-60))
            #self.rect.center = (self.x, self.y)
            pygame.draw.rect(self.window, (0, 255, 0), self.rect)
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
        if self.currentPathNodePos >= len(self.path):
            # Remove enemy from screen
            pass
        
        else:
            x1, y1 = self.path[self.currentPathNodePos][0], self.path[self.currentPathNodePos][1]
            x2, y2 = self.path[self.currentPathNodePos + 1][0], self.path[self.currentPathNodePos + 1][1]
            distanceBetweenPoints = np.hypot((x2-x1), (y2-y1))
            nodeVector = normalize(x2-x1, y2-y1)
            new_x, new_y = (self.x + nodeVector[0] * self.speed, self.y + nodeVector[1] * self.speed)
            #self.directionalVector = normalize(new_x-self.x, new_y - self.y)
            #self.directionalVector = (new_x-self.x, new_y - self.y)
            self.distanceTraveled += np.hypot((new_x-self.x), (new_y - self.y))
            self.x, self.y = new_x, new_y
            
            if self.distanceTraveled >= distanceBetweenPoints:                           # check if we have passed the point
                self.currentPathNodePos += 1
                self.distanceTraveled = 0
        
        return nodeVector
    
    # Returns true if the enemy has died.
    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.dead = True
        
    def rotate(self, nodeVector):
        #print("Trying to rotate")
        dotProduct = np.dot(nodeVector, self.directionalVector)
        radianAngleBetweenVectors = np.arccos(dotProduct)/10
        degreeAngleBetweenVectors = np.degrees(radianAngleBetweenVectors)
        rotationalMatrix1 = np.array([[cos(-radianAngleBetweenVectors), -sin(-radianAngleBetweenVectors)], 
                                      [sin(-radianAngleBetweenVectors), cos(-radianAngleBetweenVectors)]])
        
        rotationalMatrix2 = np.array([[cos(-radianAngleBetweenVectors*10), -sin(-radianAngleBetweenVectors*10)], 
                                      [sin(-radianAngleBetweenVectors*10), cos(-radianAngleBetweenVectors*10)]])
        #print("Angle: ", degreeAngleBetweenVectors)
        goalVector = np.dot(rotationalMatrix2, self.directionalVector)
        #while self.directionalVector != goalVector:
        self.image = pygame.transform.rotate(self.image, -degreeAngleBetweenVectors)   
        #self.img = pygame.transform.rotate(self.img, 90)
        self.directionalVector = np.dot(rotationalMatrix1, self.directionalVector)
        #print("Directional vector: ", self.directionalVector)
        #time.sleep(0.1)
        
    def display_health(self, window):
        bar_x, bar_y = (self.x - 32), (self.rect.center[1] - 45)
        length, width = 64, 10
        increment = length / self.default_health
        pygame.draw.rect(window, (255, 0, 0), (bar_x, bar_y, length, width), 0)
        pygame.draw.rect(window, (0, 255, 0), (bar_x, bar_y, increment * self.health, width), 0)
        
        
        