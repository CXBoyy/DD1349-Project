import pygame
from math import sqrt
from projectile import Projectile
from tower_menu import Button, Towermenu


class Tower(pygame.sprite.DirtySprite):
    """ Abstract class for towers
    """

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.width = 0
        self.height = 0
        self.damage = 1
        self.projectile_speed = 1
        self.selected = False
        self.tower_img = []
        self.range = 10
        self.radius = self.range
        self.tower_rect = None
        self.moving = False
        self.target = None
        self.cooldown = 60
        self.cooldown_counter = 0
        self.place_color = None
        self.dirty = 0

    def drawTower(self, window: pygame.Surface):
        """ Draws the tower

        Args:
            window (pygame.Surface): surface
        """
        window.blit(self.tower_img[0].convert_alpha(), (self.x, self.y))

    def attack2(self, enemy, damage, speed):
        """ Attack a enemy

        Args:
            enemy (Enemy): enemy to attack
            damage (int): damage of the projectile
            speed (int): speed of the projectile

        Returns:
            Projectile: the projectile
        """
        return Projectile(self, enemy, damage, speed)

    def is_in_range(self, enemy):
        """ Check if enemy is in tower range

        Args:
            enemy (Enemy): enemy to attack

        Returns:
            boolean: True if in range
        """
        distance = sqrt((enemy.x - self.x)**2 + (enemy.y - self.y)**2)
        if distance <= self.range:
            return True
        else:
            return False

    def draw_radius(self, window):
        """ Draws tower range

        Args:
            window (pygame.Surface): surface
        """
        if self.selected:
            surface = pygame.Surface(
                (self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            circleRect = pygame.draw.circle(
                surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            circleRect.center = (self.x + 32, self.y + 32)
            window.blit(surface.convert_alpha(), ((self.x + (self.width / 2)) -
                        self.range, (self.y + (self.height / 2)) - self.range))

    def draw_placement(self, window):
        """ Draws range circle

        Args:
            window (pygame.Surface): surface
        """
        surface = pygame.Surface(
            (self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        if self.place_color is not None:
            pygame.draw.rect(
                surface, self.place_color, pygame.Rect(
                    0, 0, 64, 64))

        window.blit(surface.convert_alpha(), (self.x, self.y))

    def moveTower(self, x, y):
        """ Moves tower

        Args:
            x (int): x-pos
            y (int): y-pos
        """
        self.x = x
        self.y = y
        self.tower_rect.topleft = (x, y)
        self.dirty = 1

    def collide(self, otherTower):
        """ Check if tower collide with an other tower

        Args:
            otherTower (Tower): list of towers

        Returns:
            boolean: False if not collide
        """
        x2 = otherTower.x
        y2 = otherTower.y   
        dis = sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis > 0:
            return False
        else:
            return True
    
    def draw(self, window):
        """ Draws the tower

        Args:
            window (_type_): surface
        """
        if self.dirty == 1:
            self.draw_radius(window)
            self.drawTower(window)