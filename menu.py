import pygame
import button
import game

class Menu():

    def __init__(self, game1:game.Game):
        self.game = game.Game()
        self.MID_WIDTH, self.MID_HEIGHT = self.game.CANVAS_WIDTH / 2, self.game.CANVAS_HEIGHT / 2
        self.to_display = False
        
        start_img = pygame.image.load("pics/start_button.png").convert_alpha()
        exit_img = pygame.image.load("pics/exit_button.png").convert_alpha()
        self.start_button = button.Button(100, 235, start_img, 0.4, self.to_display)
        self.exit_button = button.Button(400, 200, exit_img, 0.9, self.to_display)
        
        map1_img = pygame.image.load("pics/WIP.png").convert_alpha()
        back_button_img = pygame.image.load("pics/back.png").convert_alpha()
        self.back_button = button.Button(20, 20, back_button_img, 0.3, self.to_display)
        self.map1_button = button.Button(self.MID_WIDTH, self.MID_HEIGHT, map1_img, 0.5, self.to_display)

    def blit_screen(self):
        self.game.window.blit(self.game.canvas, (0,0))
        pygame.display.update()
        self.game.reset_vars()

    def display_MainMenu(self, clock:pygame.time.Clock):
        mainClock = clock
        self.to_display = True
        self.activate_buttons()
        while self.to_display:
            self.check_events()
            self.game.canvas.fill(self.game.SKY_BLUE)
            self.game.window.blit(self.game.canvas, (0,0))
            if self.start_button.draw(self.game.window):
                self.display_MapMenu(clock)
            if self.exit_button.draw(self.game.window):
                self.game.running = False
                self.game.playing= False
                self.to_display = False
            pygame.display.update()
            mainClock.tick(60)
            
    def display_MapMenu(self, clock:pygame.time.Clock):
        mainClock = clock
        self.to_display = True
        self.activate_buttons()
        while self.to_display:
            self.check_events()
            self.game.canvas.fill(self.game.SKY_BLUE)
            self.game.window.blit(self.game.canvas, (0,0))
            if self.back_button.draw(self.game.window):
                self.to_display = False
            if self.map1_button.draw(self.game.window):
                g = game.Game()
                print("map1")
                g.playing = True
                g.game_loop(clock=mainClock, map="map1")
            pygame.display.update()
            mainClock.tick(60)


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
        self.back_button.register = True
        self.map1_button.register = True

        