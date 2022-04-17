import pygame
import button
import enemy

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
        #self.map1_start = (0, 97)
        self.map1_path = [(32, 97), (101, 96), (155, 95), (224, 97), (278, 106), (287, 160), (287, 220), (284, 288), (275, 340), 
                     (224, 347), (162, 348), (102, 356), (93, 412), (105, 470), (161, 482), (225, 478), (287, 478), (351, 472), 
                     (413, 476), (479, 480), (546, 480), (607, 481), (670, 479), (724, 465), (731, 415), (734, 349), (735, 285), 
                     (745, 232), (804, 222), (870, 222)]

        
        self.test_enemy = enemy.Enemy(self.window, 0, 97, 5, 5, self.map1_path)
        
        

    def game_loop(self, clock:pygame.time.Clock, map):
        mainClock = clock 
        self.map = map
        font = pygame.font.Font(None, 32)
        text = font.render("Now playing Map 1", True, (0, 0, 0))
        rect = text.get_rect(center=(500, 300))
        if self.map == "map1":
            while self.playing:
                for point in self.map1_path:
                    self.check_events()
                    self.canvas.fill(self.SKY_BLUE)
                    self.window.blit(self.canvas, (0,0))
                    self.window.blit(self.map1_img, (0,0))
                    self.window.blit(text, rect)
                    self.test_enemy.move(self.window, point[0], point[1])
                    
                    
                    
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
                pos = pygame.mouse.get_pos()
                if event.button == 1:
                    self.LEFTMOUSECLICK = True


    def reset_vars(self):
        self.LEFTMOUSECLICK = False
