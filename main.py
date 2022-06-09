import asyncio
import pygame
import game
import menu

# Variables
g = game.Game()
menuVar = menu.Menu(g)


SKY_BLUE_COLOR = (202, 228, 241)

pygame.display.set_caption("Tower defense")

async def main():
    """ Main method for game
    """
    clock = pygame.time.Clock()
    print(g.playing)
    while g.running:
        await menuVar.display_MainMenu(clock)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menuVar.to_display = False
                g.running = False
        pygame.display.update()
        clock.tick(g.FPS)
        await asyncio.sleep(0)
    pygame.quit()


if __name__ == "__main__":
    asyncio.run( main() )
