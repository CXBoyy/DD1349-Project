import pygame

class Menu():

    def __init__(self, game):
        self.game = game
        self.MID_WIDTH, self.MID_HEIGHT = self.game.CANVAS_WIDTH, self.game.CANVAS_HEIGHT