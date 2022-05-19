import pygame
import button
import game
import menu

# Variables
g = game.Game()
menuVar = menu.Menu(g)


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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuVar.to_display = False
                g.running = False
        pygame.display.update()
        clock.tick(g.FPS)
    pygame.quit()

if __name__ == "__main__":
    main()