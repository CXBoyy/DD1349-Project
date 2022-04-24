import pygame
import button
from enemies import enemy
from enemies import single_track as st
import time

class Game():

    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.LEFTMOUSECLICK = False
        self.CANVAS_WIDTH, self.CANVAS_HEIGHT = 896, 640
        self.FPS = 60
        self.canvas = pygame.Surface((self.CANVAS_WIDTH, self.CANVAS_HEIGHT))
        self.window = pygame.display.set_mode((self.CANVAS_WIDTH, self.CANVAS_HEIGHT))
        self.SKY_BLUE = (202, 228, 241)
        self.map = None
        back_button_img = pygame.image.load("pics/back.png").convert_alpha()
        self.back_button1 = button.Button(500, 50, back_button_img, 0.3, True)
        
        self.map1_img = pygame.image.load("assets/New/Terrain/map1_trial.png").convert_alpha()
        self.map1_end = (896, 222)
        
        self.map1_path = [(0, 97), (32, 97), (101, 97), (155, 97), (224, 97), (287, 106), (287, 160), (287, 220), (287, 288), (275, 340), 
                          (224, 348), (162, 348), (102, 356), (98, 412), (105, 470), (161, 478), (225, 478), (287, 478), (351, 478), (413, 478), 
                          (479, 478), (546, 478), (607, 478), (670, 478), (731, 465), (731, 415), (731, 349), (731, 285), (745, 232), (804, 222), 
                          (870, 222), (896, 222), (900, 222)
                          ]

        self.enemies = [
                        #st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end),
                        st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end),
                        ]
        
        

    def game_loop(self, clock:pygame.time.Clock, map):
        mainClock = clock 
        self.map = map
        font = pygame.font.Font(None, 32)
        text = font.render("Now playing Map 1", True, (0, 0, 0))
        rect = text.get_rect(center=(500, 300))
        counter = 0
        if self.map == "map1":
            while self.playing:
                counter += 1
                self.check_events()
                self.canvas.fill(self.SKY_BLUE)
                self.window.blit(self.canvas, (0,0))
                self.window.blit(self.map1_img, (0,0))
                self.window.blit(text, rect)
                #for enemy in self.enemies:
                    #time.sleep(1)
                    #enemy.draw()
                self.enemies[0].draw()
                for point in self.map1_path:
                    pygame.draw.circle(self.window, (255, 0, 0), point, 5)
                if counter >= 60:
                    #self.enemies[1].draw()
                    pass
                
                if self.back_button1.draw(self.window):
                    self.playing = False
                pygame.display.update()
                mainClock.tick(60)
        #pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.LEFTMOUSECLICK = True


    def reset_vars(self):
        self.LEFTMOUSECLICK = False
