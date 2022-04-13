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
        self.start_button = button.Button(100, 235, start_img, 0.4, self.to_display)
        self.exit_button = button.Button(400, 200, exit_img, 0.9, self.to_display)

    def display_MainMenu(self):
        self.to_display = True
        self.activate_buttons()
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
    
    def activate_buttons(self):
        self.start_button.register = True
        self.exit_button.register = True

class MapMenu(Menu):
    def __init__(self, game, mainmenu):
        Menu.__init__(self, game)
        self.mainmenu = mainmenu
        map1_img = pygame.image.load("pics/WIP.png").convert_alpha()
        back_button_image = pygame.image.load("pics/back.png").convert_alpha()
        self.back_button = button.Button(20, 20, back_button_image, 1, self.to_display)
        self.map1_button = button.Button(self.MID_WIDTH, self.MID_HEIGHT, map1_img, 0.5, self.to_display)

    def display_MapMenu(self):
        self.to_display = True
        self.activate_buttons()
        while self.to_display:
            self.check_events()
            self.game.canvas.fill(self.game.SKY_BLUE)
            self.game.window.blit(self.game.canvas, (0,0))
            if self.back_button.draw(self.game.window):
                self.to_display = False
                #self.mainmenu.to_display = True                                 #how to access to_display in MainMenu class? 
            if self.map1_button.draw(self.game.window):
                print("map1")
            pygame.display.update()
    
    def activate_buttons(self):
        self.back_button.register = True
        self.map1_button.register = True

    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.to_display = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.LEFTMOUSECLICK = True
                    print("LMB Clicked")

        