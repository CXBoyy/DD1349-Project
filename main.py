import pygame
import button
import game
import menu

# Variables
g = game.Game()
menuVar = menu.Menu(g)
#CANVAS_WIDTH, CANVAS_HEIGHT = 1000, 600

#window = pygame.display.set_mode((CANVAS_WIDTH, CANVAS_HEIGHT))


SKY_BLUE_COLOR = (202, 228, 241)

pygame.display.set_caption("Test")

# Images
start_img = pygame.image.load("pics/start_button.png").convert_alpha()
exit_img = pygame.image.load("pics/exit_button.png").convert_alpha()

def main():
    clock = pygame.time.Clock()
    print(g.playing)
    while g.running:
        menuVar.display_MainMenu(clock)
        #g.game_loop(clock)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuVar.to_display = False
                g.running = False
        pygame.display.update()
        clock.tick(g.FPS)
    pygame.quit()

if __name__ == "__main__":
    main()