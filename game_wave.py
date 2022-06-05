import pygame

class Wave(pygame.sprite.Group):
    """ Class for waves, inherits from pygame.sprite.Group
    """
    
    def __init__(self):
        super().__init__(self)
        self.wave_started = False
        self.wave_finished = False