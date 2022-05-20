import pygame
import numpy as np
import math
from projectile import Projectile
from tower_menu import Button, Towermenu


class Tower():
    """ Abstract class for towers
    """
    def __init__(self, x, y):
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
        self.moving_tower = False
        self.target = None
        self.cooldown = 60
        self.cooldown_counter = 0
        self.place_color = None


    def drawTower(self, window : pygame.Surface):
        """ Draws the tower

        Args:
            window (pygame.Surface): surface 
        """
        window.blit(self.tower_img[0], (self.x, self.y))
        
                    
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
        distance = np.hypot(enemy.x - self.x, enemy.y - self.y)
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
            surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
            circleRect = pygame.draw.circle(surface, (128, 128, 128, 100), (self.range, self.range), self.range, 0)
            circleRect.center = (self.x+32, self.y+32)
            window.blit(surface, ((self.x + (self.width/2)) - self.range, (self.y + (self.height/2)) - self.range))
        
    def draw_placement(self, window):
        """ Draws range circle 

        Args:
            window (pygame.Surface): surface
        """
        surface = pygame.Surface((self.range * 4, self.range * 4), pygame.SRCALPHA, 32)
        if self.place_color is not None:
            pygame.draw.rect(surface, self.place_color, pygame.Rect(0,0,64,64))

        window.blit(surface, (self.x, self.y))



    def check_tower_actions(self, pos : tuple, event : pygame.event): 
        """ A method to check pygame events during the game loop.
        """   
        if self.tower_rect.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:                   # Right mouse click
                    if self.selected is False:
                        self.selected = True
                        return self                 
                    if self.selected is True:
                        self.selected = False
                        return None
                
        if not self.tower_rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.selected is True:
                self.selected = False
                return None
            
        else:
            return False

    def moveTower(self,x,y):
        """ Moves tower 

        Args:
            x (int): x-pos
            y (int): y-pos
        """
        self.x = x
        self.y = y
        self.tower_rect.topleft = (x, y)
        
        
    def collide(self, otherTower):
        """ Check if tower collide with an other tower

        Args:
            otherTower (Tower): list of towers

        Returns:
            boolean: False if not collide
        """
        x2 = otherTower.x
        y2 = otherTower.y   
        dis = math.sqrt((x2 - self.x)**2 + (y2 - self.y)**2)
        if dis > 0:
            return False
        else:
            return True