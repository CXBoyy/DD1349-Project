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

class Projectile(pygame.sprite.Sprite):
    def __init__(self, source ,target:Enemy, damage, speed):
        super().__init__()
        self.source = source
        self.x = source.x
        self.y = source.y
        self.target = target
        self.window = target.window
        self.directionalVector = normalize( (self.target.x - self.x), (self.target.y - self.y) )
        self.image = pygame.Surface((10, 10))
        self.rect = pygame.Rect(self.x, self.y, 5, 5)
        self.dead = False
        self.damage = damage
        self.speed = speed
        
    def check_collision(self):
        if self.target.rect is not None:
            if self.rect.colliderect(self.target.rect):
                self.target.hit(self.damage)
                self.dead = True
                return True
            else:
                return False
    
    def update(self):
        if not self.dead:
            self.move()
            #self.directionalVector = ((self.target.x - self.x), (self.target.y - self.y))
            #print(self.directionalVector)
            #self.x = self.x + self.directionalVector[0] * self.speed
            #self.y = self.y + self.directionalVector[1] * self.speed
            #self.rect.center = (self.x, self.y)
            self.rect = pygame.Rect(self.x, self.y, 5, 5)
            self.check_collision()
            #time.sleep(0.05)
            
    def move(self):
        self.directionalVector = normalize( (self.target.x - self.x), (self.target.y - self.y) )
        #self.directionalVector = ((self.target.x - self.x), (self.target.y - self.y))
        new_x, new_y = (self.x + self.directionalVector[0] * self.speed, self.y + self.directionalVector[1] * self.speed)
        self.x, self.y = new_x, new_y
            
    def draw(self):
        pygame.draw.rect(self.window, (255, 255, 0), self.rect, )
        #pygame.display.update()
    