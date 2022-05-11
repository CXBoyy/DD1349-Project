import pygame
from enemies.enemy import Enemy
#from towers.tower import Tower, normalize
import numpy as np
import time

def normalize(e1, e2):
        vector = (e1, e2)
        norm = np.linalg.norm(vector)
        newVector = (vector[0] / norm, vector[1] / norm)
        return newVector

class Projectile():
    def __init__(self, source ,target:Enemy):
        self.source = source
        self.x = source.x
        self.y = source.y
        self.target = target
        self.window = target.window
        self.directionalVector = normalize( (self.target.x - self.x), (self.target.y - self.y) )
        self.image = None
        self.rect = pygame.Rect(self.x, self.y, 5, 5)
        self.dead = False
        self.damage = 1
        self.speed = 1
        
    def check_collision(self):
        if self.target.rect is not None:
            if self.rect.colliderect(self.target.rect):
                print("Hit")
                self.target.health -= 1
                self.dead = True
                return True
        else:
            print("No hit")
            return False
    
    def update(self):
        if not self.dead:
            if not self.check_collision():
                print("Moving")
                self.directionalVector = normalize( (self.target.x - self.x), (self.target.y - self.y) )
                #print(self.directionalVector)
                self.x = self.x + self.directionalVector[0] * self.speed
                self.y = self.y + self.directionalVector[1] * self.speed
            
            self.rect = pygame.Rect(self.x, self.y, 5, 5)
            self.draw()
            time.sleep(0.005)
            
    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 0), self.rect, )
        #pygame.display.update()
    