import pygame
import button
import game

# Variables
g = game.Game()

SKY_BLUE_COLOR = (202, 228, 241)

pygame.display.set_caption("Test")

# Images
start_img = pygame.image.load("pics/start_button.png").convert_alpha()
exit_img = pygame.image.load("pics/exit_button.png").convert_alpha()

# Buttons
start_button = button.Button(100, 235, start_img, 0.4)
exit_button = button.Button(400, 200, exit_img, 0.9)

run = True

def draw_screen():
    if start_button.draw():
        start_button.startButton()
    if exit_button.draw():
        run = False

def main():
    clock = pygame.time.Clock()
    g.playing = True
    print(g.playing)
    while g.running:
        g.game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g.running = False
        pygame.display.update()
        clock.tick(g.FPS)
    pygame.quit()

if __name__ == "__main__":
    main()