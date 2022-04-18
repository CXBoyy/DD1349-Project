import pygame
import button
import enemy
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
        
        self.map1_path = [(896, 222), (870, 222), (804, 222), (745, 232), (735, 285), (734, 349), (731, 415), (724, 465), 
                          (670, 479), (607, 481), (546, 480), (479, 480), (413, 476), (351, 472), (287, 478), (225, 478), 
                          (161, 482), (105, 470), (93, 412), (102, 356), (162, 348), (224, 347), (275, 340), (284, 288), 
                          (287, 220), (287, 160), (278, 106), (224, 97), (155, 95), (101, 96), (32, 97), (0, 97)]
        
        self.map1_pathDict = {
            (0, 97) : False, (32, 97) : False, (101, 96) : False, (155, 95) : False, (224, 97) : False, (278, 106) : False, (287, 160) : False, 
            (287, 220) : False, (284, 288) : False, (275, 340) : False, (224, 347) : False, (162, 348) : False, (102, 356) : False, (93, 412) : False, 
            (105, 470) : False, (161, 482) : False, (225, 478) : False, (287, 478) : False, (351, 472) : False, (413, 476) : False, (479, 480) : False, 
            (546, 480) : False, (607, 481) : False, (670, 479) : False, (724, 465) : False, (731, 415) : False, (734, 349) : False, (735, 285) : False, 
            (745, 232) : False, (804, 222) : False, (870, 222) : False, (896, 222) : False
        }

        self.enemies = [
                        enemy.Enemy(self.window, 0, 97, 5, 5, self.map1_path, self.map1_pathDict, self.map1_end),
                        enemy.Enemy(self.window, 0, 97, 5, 5, self.map1_path, self.map1_pathDict, self.map1_end),
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
                if counter >= 60:
                    self.enemies[1].draw()
                    
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
