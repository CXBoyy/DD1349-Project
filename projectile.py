import pygame

class Projectile():
    def __init__(self, target):
            self.x = None
            self.y = None
            self.target = target
            self.directionalVector = None
            self.img = None
            self.damage = 1
            
    