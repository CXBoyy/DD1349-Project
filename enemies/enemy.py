import pygame
import copy
from math import cos, sin, atan2, degrees, sqrt


def normalize(e1, e2):
    """ A method to normalize a vector

    Args:
        e1 (double): x-coordinate of the vector
        e2 (double): y-coordinate of the vector

    Returns:
        tuple: the normalized vector
    """
    vector = (e1, e2)
    norm = sqrt(e1**2 + e2**2)
    newVector = (vector[0] / norm, vector[1] / norm)
    return newVector


class Enemy(pygame.sprite.Sprite):
    """ Abstract class for the enemies.
        Inherits from the pygame.sprite.Sprite class.
    """
    imgs = []

    def __init__(self, window, x, y, width, height, path, pathEnd, game):
        """ Constructor method for enemies.
        """
        super().__init__()

        # Position of
        self.x = x
        # the enemy.
        self.y = y

        # Size of the
        self.width = width
        # enemy image.
        self.height = height
        self.window = window
        self.image = None
        self.rect = None
        self.path = copy.deepcopy(path)
        self.currentPathNodePos = 0
        self.pathEnd = pathEnd
        self.animation_count = 0
        self.distanceTraveled = 0
        self.directionalVector = normalize(
            self.path[1][0] -
            self.x,
            self.path[1][1] -
            self.y)       # Setting the starting directional vector
        self.game = game

        # To be set individually for each enemy type
        self.default_health = 6
        # To be set individually for each enemy type
        self.health = self.default_health
        # To be set individually for each enemy type
        self.speed = 1
        # To be set individually for each enemy type
        self.reward = 0
        self.dead = False
        self.out_of_bounds = False
        self.angle1 = atan2(
            self.directionalVector[1],
            self.directionalVector[0])

    def update(self):
        """ Update method. Rotates enemies and draws them on the screen.
        """
        if (self.x, self.y) >= self.pathEnd:
            self.game.health -= 1
            self.out_of_bounds = True
        else:
            index = self.animation_count // len(self.imgs)
            self.image = self.imgs[index].convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = (self.x, self.y)
            nodeVector = self.move()
            angle2 = atan2(nodeVector[1], nodeVector[0])
            if self.angle1 != angle2:
                diff = (angle2 - self.angle1) / 5
                self.angle1 += diff
                self.rotate(degrees(-self.angle1))
            else:
                pass

            self.display_health(self.window)
            self.animation_count += 1
            if self.animation_count >= len(self.imgs):
                self.animation_count = 0

    def move(self):
        """ Update the coordinates of the enemy

        Returns:
            tuple: the vector denoting the direction of movement
        """
        x1, y1 = self.path[self.currentPathNodePos][0], self.path[self.currentPathNodePos][1]
        x2, y2 = self.path[self.currentPathNodePos + 1][0], self.path[self.currentPathNodePos + 1][1]
        distanceBetweenPoints = sqrt(
                                (x2-x1)**2 + (y2-y1)**2)
        nodeVector = normalize(x2-x1, y2-y1)
        new_x, new_y = (self.x + nodeVector[0] * self.speed, 
                        self.y + nodeVector[1] * self.speed)
        self.distanceTraveled += sqrt(
                                (new_x-self.x)**2 + (new_y - self.y)**2)
        self.x, self.y = new_x, new_y

        # check if we have passed the point
        if self.distanceTraveled >= distanceBetweenPoints:
            self.currentPathNodePos += 1
            self.distanceTraveled = 0

        return nodeVector

    def hit(self, damage):
        """ Register a hit and decrease enemy health.

        Args:
            damage (int): the damage dealt to enemy
        """
        self.health -= damage
        if self.health <= 0:
            self.dead = True

    def rotate(self, angle):
        """ Function for rotation of enemies

        Args:
            angle (double): angle to rotate
        """
        old_center = self.rect.center
        self.image = pygame.transform.rotate(self.image, angle).convert_alpha()
        self.rect.center = old_center

    def display_health(self, window):
        """ Function to display health bar for enemies.

        Args:
            window (pygame.Surface): the window to draw the health bar on
        """
        bar_x, bar_y = (self.x - 32), (self.rect.center[1] - 45)
        length, width = 64, 10
        increment = length / self.default_health
        pygame.draw.rect(window, (255, 0, 0), (bar_x, bar_y, length, width), 0)
        pygame.draw.rect(window, (0, 255, 0), (bar_x, bar_y,
                         increment * self.health, width), 0)
