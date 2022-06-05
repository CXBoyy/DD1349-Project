import pygame
from .tower import Tower


class basictower(Tower):
    """ Class for basictower

    Args:
        Tower (_type_): Tower lvl 1
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_img = []
        self.range = 300
        self.width = self.height = 60
        self.enemy_is_in_range = False
        self.cooldown = 90
        self.in_range = False
        self.moving = False
        self.name = "buy_tower1"
        self.damage = 2
        self.projectile_speed = 4

        self.tower_img.append(pygame.transform.scale(pygame.image.load(
            r"assets/New/Towers/tower1/tower1_1.png"), (64, 64)))

        self.tower_rect = self.tower_img[0].get_rect()
        self.tower_rect.topleft = (self.x, self.y)

    def draw(self, window):
        """ Draws the tower

        Args:
            window (_type_): surface
        """
        super().draw_radius(window)
        super().drawTower(window)


class dubbletower(basictower):
    """ Class for dubbletower

    Args:
        basictower (Tower): Tower lvl 2
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_img = []
        self.range = 250
        self.width = self.height = 60
        self.enemy_is_in_range = False
        self.cooldown = 30
        self.in_range = False
        self.moving = False
        self.name = "buy_tower2"
        self.damage = 1
        self.projectile_speed = 6

        self.tower_img.append(pygame.transform.scale(pygame.image.load(
            r"assets/New/Towers/Tower3/Tower_3_body_cannon.png"), (64, 64)))

        self.tower_rect = self.tower_img[0].get_rect()
        self.tower_rect.topleft = (self.x, self.y)


class heavytower(basictower):
    """ Class for heavytower

    Args:
        basictower (_type_): Tower lvl 3
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_img = []
        self.range = 150
        self.width = self.height = 60
        self.enemy_is_in_range = False
        self.cooldown = 120
        self.in_range = False
        self.moving = False
        self.name = "buy_tower3"
        self.damage = 6
        self.projectile_speed = 4

        self.tower_img.append(pygame.transform.scale(pygame.image.load(
            r"assets/New/Towers/Tower4/Tower_4_body_cannon.png"), (64, 64)))

        self.tower_rect = self.tower_img[0].get_rect()
        self.tower_rect.topleft = (self.x, self.y)


class missiletower(basictower):
    """ Class for missiletower

    Args:
        basictower (_type_): Tower lvl 4
    """

    def __init__(self, x, y):
        super().__init__(x, y)
        self.tower_img = []
        self.range = 250
        self.width = self.height = 60
        self.enemy_is_in_range = False
        self.cooldown = 300
        self.in_range = False
        self.moving = False
        self.name = "buy_tower4"
        self.damage = 10
        self.projectile_speed = 4

        self.tower_img.append(pygame.transform.scale(pygame.image.load(
            r"assets/New/Towers/Tower5/Tower_5_body_cannon.png"), (64, 64)))

        self.tower_rect = self.tower_img[0].get_rect()
        self.tower_rect.topleft = (self.x, self.y)
