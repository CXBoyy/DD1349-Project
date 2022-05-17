import pygame
from .enemy import Enemy

class SingleTrack(Enemy):
    temp = pygame.image.load("assets/New/Units/body_tracks.png")
    temp = pygame.transform.rotate(temp, -90)
    imgs = [temp]
    
    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        super().__init__(window, x, y, width, height, path, pathEnd, game)
        self.name = "single_track"
        self.money = 10
        self.default_health = 10  
        self.health = self.default_health
        self.speed = 2
        self.reward = 30