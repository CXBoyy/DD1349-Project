import pygame

class Game():

    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.LEFTMOUSECLICK = False
        self.CANVAS_WIDTH, self.CANVAS_HEIGHT = 1000, 600
        self.FPS = 60
        self.canvas = pygame.Surface((self.CANVAS_WIDTH, self.CANVAS_HEIGHT))
        self.window = pygame.display.set_mode((self.CANVAS_WIDTH, self.CANVAS_HEIGHT))
        self.SKY_BLUE = (202, 228, 241)

    def game_loop(self):
        while self.playing:
            self.check_events()
            self.canvas.fill(self.SKY_BLUE)
            self.window.blit(self.canvas, (0,0))
            pygame.display.update()
        #pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.LEFTMOUSECLICK = True
                    print("LMB Clicked")


def reset_vars(self):
    self.LEFTMOUSECLICK = False
