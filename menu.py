import pygame
import button

class Menu():

    def __init__(self, game):
        self.game = game
        self.MID_WIDTH, self.MID_HEIGHT = self.game.CANVAS_WIDTH / 2, self.game.CANVAS_HEIGHT / 2
        self.to_display = False

    def blit_screen(self):
        self.game.window.blit(self.game.canvas, (0,0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

        start_img = pygame.image.load("pics/start_button.png").convert_alpha()
        exit_img = pygame.image.load("pics/exit_button.png").convert_alpha()
        self.start_button = button.Button(100, 235, start_img, 0.4)
        self.exit_button = button.Button(400, 200, exit_img, 0.9)

    def display_MainMenu(self):
        self.to_display = True
        while self.to_display:
            self.check_events()
            self.game.canvas.fill(self.game.SKY_BLUE)
            self.game.window.blit(self.game.canvas, (0,0))
            if self.start_button.draw(self.game.window):
                self.game.playing = True
                self.to_display = False
                self.start_button.startButton()
            if self.exit_button.draw(self.game.window):
                self.game.running = False
                self.to_display = False
            pygame.display.update()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.to_display = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.LEFTMOUSECLICK = True
                    print("LMB Clicked")
        