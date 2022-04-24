import pygame
from .enemy import Enemy

class SingleTrack(Enemy):
    imgs = [pygame.image.load("assets/New/Units/body_tracks.png")]
    
    def __init__(self, window, x, y, width, height, path, pathEnd):
        super().__init__(window, x, y, width, height, path, pathEnd)
        self.speed = 1