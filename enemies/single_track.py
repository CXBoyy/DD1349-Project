import pygame
from .enemy import Enemy

class SingleTrack(Enemy):
    temp = pygame.image.load("assets/New/Units/body_tracks.png")
    temp = pygame.transform.rotate(temp, -90)
    imgs = [temp]
    
    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        super().__init__(window, x, y, width, height, path, pathEnd, game)
        self.name = "single_track"
        self.default_health = 10  
        self.health = self.default_health
        self.speed = 2
        self.reward = 40
        
class SingleTrackLvl2(SingleTrack):
    temp = pygame.image.load("assets/New/Units/body_tracks.png")
    temp = pygame.transform.rotate(temp, -90)
    imgs = [temp]
    
    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        super().__init__(window, x, y, width, height, path, pathEnd, game)
        self.name = "single_track_lvl2"
        self.default_health = 12 
        self.health = self.default_health
        self.speed = 2
        self.reward = 60
        
        
class SingleTrackLvl3(SingleTrack):
    temp = pygame.image.load("assets/New/Units/body_tracks.png")
    temp = pygame.transform.rotate(temp, -90)
    imgs = [temp]
    
    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        super().__init__(window, x, y, width, height, path, pathEnd, game)
        self.name = "single_track_lvl3"
        self.default_health = 15 
        self.health = self.default_health
        self.speed = 2
        self.reward = 80
        
class SingleTrackLvl4(SingleTrack):
    temp = pygame.image.load("assets/New/Units/body_tracks.png")
    temp = pygame.transform.rotate(temp, -90)
    imgs = [temp]
    
    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        super().__init__(window, x, y, width, height, path, pathEnd, game)
        self.name = "single_track_lvl4"
        self.default_health = 20
        self.health = self.default_health
        self.speed = 3
        self.reward = 100