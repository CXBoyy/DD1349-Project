import pygame
from .enemy import Enemy


class SingleTrack(Enemy):
    """ Enemy Lvl 1. Inherits from the abstract Enemy class.
    """
    temp = pygame.image.load("assets/New/Units/body_tracks.png")
    temp = pygame.transform.rotate(temp, -90)
    imgs = [temp]

    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        """ Constructor for the enemy object.

        Args:
            window (pygame.Surface): window to draw the enemy on.
            x (double): x coordinate
            y (double): y coordinate
            width (int): width of enemy
            height (int): height of enemy
            path (list): list with path coordinates
            pathEnd (tuple): end of the path
            game (Game): game object that the game runs on.
        """
        super().__init__(window, x, y, width, height, path, pathEnd, game)
        self.name = "single_track"
        self.default_health = 10
        self.health = self.default_health
        self.speed = 2
        self.reward = 40


class SingleTrackLvl2(SingleTrack):
    """ Enemy Lvl 4. Inherits from the Enemy Lvl1 class.
    """
    temp = pygame.image.load("assets/New/Units/body_tracks.png")
    temp = pygame.transform.rotate(temp, -90)
    imgs = [temp]

    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        """ Constructor for the enemy object.

        Args:
            window (pygame.Surface): window to draw the enemy on.
            x (double): x coordinate
            y (double): y coordinate
            width (int): width of enemy
            height (int): height of enemy
            path (list): list with path coordinates
            pathEnd (tuple): end of the path
            game (Game): game object that the game runs on.
        """
        super().__init__(window, x, y, width, height, path, pathEnd, game)
        self.name = "single_track_lvl2"
        self.default_health = 12
        self.health = self.default_health
        self.speed = 2
        self.reward = 60


class SingleTrackLvl3(SingleTrack):
    """ Enemy Lvl 4. Inherits from the Enemy Lvl1 class.
    """
    temp = pygame.image.load("assets/New/Units/body_tracks.png")
    temp = pygame.transform.rotate(temp, -90)
    imgs = [temp]

    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        """ Constructor for the enemy object.

        Args:
            window (pygame.Surface): window to draw the enemy on.
            x (double): x coordinate
            y (double): y coordinate
            width (int): width of enemy
            height (int): height of enemy
            path (list): list with path coordinates
            pathEnd (tuple): end of the path
            game (Game): game object that the game runs on.
        """
        super().__init__(window, x, y, width, height, path, pathEnd, game)
        self.name = "single_track_lvl3"
        self.default_health = 15
        self.health = self.default_health
        self.speed = 2
        self.reward = 80


class SingleTrackLvl4(SingleTrack):
    """ Enemy Lvl 4. Inherits from the Enemy Lvl1 class.
    """
    temp = pygame.image.load("assets/New/Units/body_tracks.png")
    temp = pygame.transform.rotate(temp, -90)
    imgs = [temp]

    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        """ Constructor for the enemy object.

        Args:
            window (pygame.Surface): window to draw the enemy on.
            x (double): x coordinate
            y (double): y coordinate
            width (int): width of enemy
            height (int): height of enemy
            path (list): list with path coordinates
            pathEnd (tuple): end of the path
            game (Game): game object that the game runs on.
        """
        super().__init__(window, x, y, width, height, path, pathEnd, game)
        self.name = "single_track_lvl4"
        self.default_health = 20
        self.health = self.default_health
        self.speed = 3
        self.reward = 100
