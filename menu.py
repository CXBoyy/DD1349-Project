import pygame
import button
import game

class Menu():

    def __init__(self, game1:game.Game):
        self.game = game1
        self.MID_WIDTH, self.MID_HEIGHT = self.game.CANVAS_WIDTH / 2, self.game.CANVAS_HEIGHT / 2
        self.to_display = False
        
        start_img = pygame.image.load("pics/start_button.png").convert_alpha()
        exit_img = pygame.image.load("pics/exit_button.png").convert_alpha()
        self.start_button = button.Button(self.MID_WIDTH - 422, 235, start_img, 0.4, self.to_display)
        self.exit_button = button.Button(self.MID_WIDTH + 11, 200, exit_img, 0.9, self.to_display)
        
        self.font = pygame.font.Font(None, 32)
        self.creator_text = self.font.render((str.format("Game made by: Alexander Jäderberg and Johan Abdi", )), True, (0, 0, 0))
        self.creator_rect = self.creator_text.get_rect(center=(self.MID_WIDTH, 500))
        
        self.buttons = [self.start_button,
                        self.exit_button,
                        ]

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
            self.start_button.draw(self.game.window)
            self.exit_button.draw(self.game.window)
            self.game.window.blit(self.creator_text, self.creator_rect)
            if self.start_button.clicked:
                self.activate_buttons()
                self.activate_buttons()
                g = game.Game()
                g.playing = True
                g.game_loop(clock=mainClock, map="map1")
            if self.exit_button.clicked:
                self.activate_buttons()
                self.game.running = False
                self.game.playing= False
                self.to_display = False
            pygame.display.update()
            mainClock.tick(60)
            

    def check_events(self):
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
                self.game.playing= False
                self.to_display = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    button.check_button_actions(pos, event)
                if event.button == 1:
                    self.LEFTMOUSECLICK = True
    
    def activate_buttons(self):
        self.start_button.clicked = False
        self.exit_button.clicked = False        