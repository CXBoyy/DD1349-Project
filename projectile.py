import pygame
from enemies.enemy import Enemy
from math import sqrt

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

class Projectile(pygame.sprite.Sprite):
    """ A class for the tower projectiles.
        Inherits from the pygame.sprite.Sprite class.
    """
    def __init__(self, source ,target:Enemy, damage, speed):
        """ Projectile constructor
            source (Tower): the tower which shot the projectile
            target (Enemy): the enemy which the projectile is supposed to hit.
            damage (int): the damage of the projectile
            speed (int): the speed of the projectile
        """
        super().__init__()
        self.source = source
        self.x = source.x
        self.y = source.y
        self.target = target
        self.window = target.window
        self.directionalVector = normalize( (self.target.x - self.x), (self.target.y - self.y) )
        self.image = pygame.Surface((10, 10))
        self.rect = pygame.Rect(self.x, self.y, 5, 5)
        self.dead = False
        self.damage = damage
        self.speed = speed
        
    def check_collision(self):
        """Checks collision with the target enemy.

        Returns:
            bool: Returns true if there was a collision, false otherwise.
        """
        if self.target.rect is not None:
            if self.rect.colliderect(self.target.rect):
                self.target.hit(self.damage)
                self.dead = True
                return True
            else:
                return False
    
    def update(self):
        """ A function to update the drawing and movement of the projectile.
        """
        if not self.dead:
            self.move()
            self.rect = pygame.Rect(self.x, self.y, 5, 5)
            self.check_collision()
            
    def move(self):
        """ A function to update the coordinates of the projectile.
        """
        self.directionalVector = normalize( (self.target.x - self.x), (self.target.y - self.y) )
        new_x, new_y = (self.x + self.directionalVector[0] * self.speed, self.y + self.directionalVector[1] * self.speed)
        self.x, self.y = new_x, new_y
    