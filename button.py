import pygame


class Button():
    """ Class for buttons
    """

    def __init__(self, x, y, image, scale, register):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(
            image, ((int)(width * scale), (int)(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.register = register

    def draw(self, surface: pygame.Surface):
        """ Draw button

        Args:
            surface (pygame.Surface): game window
        """
        surface.blit(self.image, (self.rect.topleft))

    def check_button_actions(self, pos, event):
        """Check if button is clicked

        Args:
            pos (_type_): mouse pos
            event (_type_): the pygame event to check for
        """
        if self.rect.collidepoint(pos):
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.clicked = True
