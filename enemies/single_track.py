import pygame
from .enemy import Enemy

class SingleTrack(Enemy):
    temp = pygame.image.load("assets/New/Units/body_tracks.png")
    temp = pygame.transform.rotate(temp, -90)
    imgs = [temp]
    
    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        super().__init__(window, x, y, width, height, path, pathEnd, game)
        self.default_health = 6  
        self.health = self.default_health
        self.speed = 1