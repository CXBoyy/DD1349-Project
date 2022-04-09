import pygame
import button

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")

start_img = pygame.image.load("pics/start_button.png").convert_alpha()
exit_img = pygame.image.load("pics/exit_button.png").convert_alpha()

start_button = button.Button(100, 235, start_img, 0.4)
exit_button = button.Button(400, 200, exit_img, 0.9)

run = True
while run:
    
    screen.fill((202, 228, 241))
    if start_button.draw(screen):
        print("start")
    if exit_button.draw(screen):
        run = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()