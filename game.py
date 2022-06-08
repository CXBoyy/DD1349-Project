import pygame, sys, asyncio
import button
from enemies import single_track as st
from towers.basictower import basictower, dubbletower, heavytower, missiletower
from game_wave import Wave
from tower_menu import Buymenu


tower_names = ["buy_tower1", "buy_tower2", "buy_tower3", "buy_tower4"]


class Game():
    """ A class holding the main game loop and relevant methods and attributes.
    """

    def __init__(self):
        """ The constructor for the Game class.
            Initializes the map, path, grids, waves etc.
        """
        pygame.init()
        self.running, self.playing = True, False
        self.LEFTMOUSECLICK = False
        self.CANVAS_WIDTH, self.CANVAS_HEIGHT = 896, 640
        self.FPS = 60
        self.canvas = pygame.Surface((self.CANVAS_WIDTH, self.CANVAS_HEIGHT))
        self.window = pygame.display.set_mode(
            (self.CANVAS_WIDTH, self.CANVAS_HEIGHT))
        self.SKY_BLUE = (202, 228, 241)
        self.map = None
        self.show_grid = False
        self.font = pygame.font.Font(None, 32)

        # Buttons
        self.back_button_img = pygame.transform.scale(
            pygame.image.load("pics/back.png").convert_alpha(), (100, 100))
        self.back_button_img_2 = pygame.image.load(
            "pics/back.png").convert_alpha()
        self.back_button1 = button.Button(
            0, 0, self.back_button_img, 0.3, True)
        
        # Buy buttons
        buy_menu_img = pygame.image.load(r"assets/New/in-game_menu.png").convert_alpha()
        buy_tower = pygame.transform.scale(pygame.image.load(
            r"assets/New/Towers/tower1/tower1_1.png"), (45, 45)).convert_alpha()
        buy_tower_2 = pygame.transform.scale(pygame.image.load(
            r"assets/New/Towers/Tower3/Tower_3_body_cannon.png"), (45, 45)).convert_alpha()
        buy_tower_3 = pygame.transform.scale(pygame.image.load(
            r"assets/New/Towers/Tower4/Tower_4_body_cannon.png"), (45, 45)).convert_alpha()
        buy_tower_4 = pygame.transform.scale(pygame.image.load(
            r"assets/New/Towers/Tower5/Tower_5_body_cannon.png"), (45, 45)).convert_alpha()

        # Map
        self.map1_img = pygame.image.load(
            "assets/New/Terrain/map1_trial_final.png").convert_alpha()
        self.map1_end = (896, 222)
        # Make the grid blit onto the map if the buy button is pressed
        self.map1_grid_img = pygame.image.load(
            "assets/New/Terrain/map1_grid.png").convert_alpha()

        self.map1_path = [(0, 97), (16.0, 97.0), (66.5, 97.0), (128.0, 97.0), (189.5, 97.0), (242.0, 98.5), (266.5, 101.0), (278.0, 105.5),
                          (285.0, 119.5), (287.0, 145.0), (287.0, 190.0), (287.0, 254.0), (281.0, 314.0), (249.5, 344.0), (193.0, 348.0),
                          (132.0, 352.0), (100.0, 384.0), (101.5, 441.0), (133.0, 474.0), (193.0, 478.0), (256.0, 478.0), (319.0, 478.0),
                          (382.0, 478.0), (446.0, 478.0), (512.5, 478.0), (576.5, 478.0), (638.5, 478.0), (700.5, 471.5), (731.0, 440.0),
                          (731.0, 382.0), (731.0, 317.0), (738.0, 258.5), (774.5, 227.0), (837.0, 222.0), (883.0, 222.0), (898.0, 222.0),
                          (32, 97), (101, 97), (155, 97), (224, 97), (260, 100), (273, 102), (283, 109), (287, 130), (287, 160), (287, 220),
                          (287, 288), (275, 340), (224, 348), (162, 348), (102, 356), (98, 412), (105, 470), (161, 478), (225, 478), (287, 478),
                          (351, 478), (413, 478), (479, 478), (546, 478), (607, 478), (670, 478), (731, 465), (731, 415), (731, 349), (731, 285),
                          (745, 232), (804, 222), (870, 222), (896, 222), (900, 222)
                          ]
        self.map1_grid_rects = []
        self.map1_path_rects = []

        # Adding grid rects
        for x_coordinate in range(32, 896, 64):
            col = []
            for y_coordinate in range(32, 640, 64):
                col.append((x_coordinate, y_coordinate))
            self.map1_grid_rects.append(col)

        # Adding board dictionary
        self.map1_dict : dict[tuple, bool] = dict()
        for i in range (0, 14):
            for j in range (0, 10):
                self.map1_dict[(i,j)] = False
        for path_coordinate in self.map1_path:
            i = int(path_coordinate[0] / 64)
            j = int(path_coordinate[1] / 64)
            self.map1_dict[(i,j)] = True

        # Waves
        wave1 = [
            st.SingleTrack(
                self.window,
                0,
                97,
                5,
                5,
                self.map1_path,
                self.map1_end,
                self),
            st.SingleTrack(
                self.window,
                0,
                97,
                2,
                5,
                self.map1_path,
                self.map1_end,
                self)]

        wave2 = [
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 2, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self)
        ]

        wave3 = [
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 2, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self)
        ]

        wave4 = [
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 2, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
        ]

        wave5 = [
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl2(
                self.window,
                0,
                97,
                5,
                5,
                self.map1_path,
                self.map1_end,
                self)]

        wave6 = [
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl2(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self)
        ]

        wave7 = [
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self)
        ]

        wave8 = [
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl3(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self)
        ]
        wave9 = [
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self)

        ]
        wave10 = [
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
            st.SingleTrackLvl4(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self)
        ]

        self.waves = [
            wave1,
            wave2,
            wave3,
            wave4,
            wave5,
            wave6,
            wave7,
            wave8,
            wave9,
            wave10]
        self.wave_dict: dict[str, Wave] = dict()

        counter = 1
        for wave in self.waves:
            wave_string = "wave{}".format(counter)
            counter += 1
            self.wave_dict[wave_string] = Wave()
            for enemy in wave:
                self.wave_dict[wave_string].add(enemy)

        # Placed towers
        self.towers = pygame.sprite.Group()

        self.buying_tower = False
        self.current_tower_cost = 0
        self.selected_tower = None
        self.moving_object = None

        # Starting money and player lives
        self.health = 10
        self.money = 400

        self.life_font = pygame.font.SysFont("comicsans", 35)

        # Buy menu
        self.menu = Buymenu(
            self.CANVAS_WIDTH -
            buy_menu_img.get_width() /
            2,
            self.CANVAS_HEIGHT,
            buy_menu_img)

        # Tower prices
        self.menu.add_button(buy_tower, "buy_tower1", 100)
        self.menu.add_button(buy_tower_2, "buy_tower2", 200)
        self.menu.add_button(buy_tower_3, "buy_tower3", 400)
        self.menu.add_button(buy_tower_4, "buy_tower4", 550)

    async def game_loop(self, clock:pygame.time.Clock, map):
        """ The main game loop method.

        Args:
            clock (pygame.time.Clock): A clock object to keep a constant frame rate.
            map (str): Name of the map to play. There is only one map at the moment, however.
        """

        mainClock = clock
        self.map = map
        font = self.font

        #
        loop_counter = 0
        wave_counter = 1
        wave_delay = 6
        countdown = wave_delay
        spawn_delay = 45
        next_enemy = "1"
        game_won = False
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN])
        if self.map == "map1":
            start_tick = pygame.time.get_ticks()
            projectiles = pygame.sprite.Group()
            while self.playing:
                wave_string = "wave{}".format(wave_counter)
                current_wave = self.wave_dict[wave_string]

                pos = list(pygame.mouse.get_pos())
                
                if pos[0] > self.CANVAS_WIDTH:
                    pos[0] = self.CANVAS_WIDTH - 64
                if pos[0] < 0:
                    pos[0] = 32
                if pos[1] > self.CANVAS_HEIGHT:
                    pos[1] = self.CANVAS_HEIGHT - 64
                if pos[1] < 0:
                    pos[1] = 32

                # Check for moving object
                if self.moving_object is not None and self.moving_object.moving:
                    grid = ( int(pos[0] / 64), int(pos[1] / 64))
                    self.moving_object.moveTower(grid[0] * 64, grid[1] * 64)
                    colliding = False
                    if self.map1_dict[grid]:
                        colliding = True
                        self.moving_object.place_color = (255, 0, 0, 100)
                    elif not colliding:
                        self.moving_object.place_color = (0, 255, 0, 100)

                # Checking if the wave has started or not
                if not current_wave.wave_started:
                    end_tick = pygame.time.get_ticks()
                    countdown = wave_delay + 1 + \
                        ((start_tick - end_tick) // 1000)
                    if end_tick - start_tick > wave_delay * 1000:
                        loop_counter = 0
                        current_wave.wave_started = True
                        iterator = iter(current_wave)
                        next_enemy = next(iterator, "1")
                        spawned_enemies = Wave()

                if current_wave.wave_finished:
                    start_tick = pygame.time.get_ticks()
                    countdown = wave_delay
                    if wave_counter < len(self.wave_dict):
                        wave_counter += 1
                    else:
                        game_won = True

                # Initialize all text
                health_text = font.render(
                    (str.format("Lives: {}", self.health)), True, (0, 0, 0))
                health_rect = health_text.get_rect(center=(90, 11))
                
                wave_text = font.render(
                    (str.format("Currently on Wave {}", wave_counter)), True, (0, 0, 0))
                wave_rect = wave_text.get_rect(center=(425, 11))
                
                wave_timer_text = font.render(
                    (str.format("Time until wave {}:   {} seconds", wave_counter, countdown)), True, (0, 0, 0))
                wave_timer_rect = wave_timer_text.get_rect(center=(730, 11))
                
                money_text = font.render(
                    (str.format("Money: {}", self.money)), True, (0, 0, 0))
                money_rect = money_text.get_rect(center=(225, 11))
                
                esc_text = font.render(
                    (str.format("Press esc to cancel", )), True, (255, 0, 0))
                esc_rect = esc_text.get_rect(center=(110, 45))
                
                fps_text = font.render(
                        str.format("FPS: {}", int(mainClock.get_fps())), True, (0, 0, 0))
                fps_rect = fps_text.get_rect(center=(830, 50))

                # Drawing everything
                self.check_events()
                self.canvas.fill(self.SKY_BLUE)
                self.window.blit(self.canvas, (0, 0))
                self.window.blit(self.map1_img, (0, 0))
                self.window.blit(health_text, health_rect)
                self.window.blit(wave_text, wave_rect)
                self.window.blit(wave_timer_text, wave_timer_rect)
                self.window.blit(money_text, money_rect)
                self.window.blit(fps_text, fps_rect)
                if self.buying_tower:
                    self.window.blit(esc_text, esc_rect)
                self.back_button1.draw(self.window)

                if self.show_grid:
                    self.window.blit(self.map1_grid_img, (0, 0))

                if current_wave.wave_started:
                    # Spawning enemies
                    if loop_counter % spawn_delay == 0 and next_enemy != "1":
                        spawned_enemies.add(next_enemy)
                        next_enemy = next(iterator, "1")

                    spawned_enemies.update()
                    spawned_enemies.draw(self.window)

                    if not bool(spawned_enemies):
                        current_wave.wave_finished = True

                    # Tower attacks
                    for tw in self.towers:
                        for enemy in self.waves[wave_counter - 1]:
                            if not enemy.dead:
                                boolean_in_range = tw.is_in_range(enemy)
                                if tw.target is not None and tw.target != enemy and not tw.is_in_range(
                                        tw.target):
                                    tw.target = enemy
                                if boolean_in_range is True and tw.cooldown_counter % tw.cooldown == 0:
                                    if tw.target is None or tw.target == enemy or tw.target.dead is True or not tw.is_in_range(tw.target):
                                        tw.target = enemy
                                        projectiles.add(
                                            tw.attack2(enemy, tw.damage, tw.projectile_speed))
                            if enemy.dead:
                                enemy.kill()
                        for projectile in projectiles:
                            if projectile.dead:
                                #projectiles.remove(projectile)
                                projectile.kill()
                        tw.cooldown_counter += 1
                    for projectile in projectiles:
                        reward = projectile.update()
                        if reward is not None:
                            self.money += reward
                    projectiles.draw(self.window)

                # Draw towers
                self.towers.draw(self.window)

                # Draw moving tower
                if self.moving_object is not None and self.moving_object.moving:
                    self.moving_object.draw(self.window)
                    self.moving_object.draw_placement(self.window)

                # Draw menu
                self.menu.draw(self.window)

                # Button interactions
                if self.back_button1.clicked:
                    self.playing = False
                    self.back_button1.clicked = False

                if self.health <= 0:
                    await self.game_over_screen()
                if game_won:
                    await self.game_won_screen()
                    
                pygame.display.update()
                loop_counter += 1
                mainClock.tick(60)
                await asyncio.sleep(0)
                
                            

    def check_events(self):
        """ A method to check pygame events during the game loop.
            Checks for left mouse click, collisions, key presses etc.
        """
        pos = list(pygame.mouse.get_pos())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if self.buying_tower:
                    self.buying_tower = False
                    self.moving_object.selected = False
                    self.moving_object = None
                    self.show_grid = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Left mouse click
                if event.button == 1:

                    # Placement of new towers
                    if self.moving_object is not None and self.moving_object.moving:
                        not_allowed = False

                        # Check if player is trying to place a new tower on the
                        # enemy path or on top of another tower
                        grid = ( int(pos[0] / 64), int(pos[1] / 64))
                        if self.map1_dict[grid]:
                            not_allowed = True

                        # Check if player is pressing the buy buttons
                        if self.menu.rect.collidepoint(pos):
                            for button in self.menu.buttons:
                                if button.rect.collidepoint(pos):
                                    buy_menu_button = self.menu.get_clicked(
                                        pos[0], pos[1])
                                    if buy_menu_button:
                                        cost = self.menu.get_item_cost(
                                            buy_menu_button)
                                        if self.money >= cost:
                                            self.show_grid = True
                                            self.current_tower_cost = cost
                                            self.add_tower(buy_menu_button)
                            not_allowed = True

                        # Place a new tower on left click
                        if not not_allowed:
                            if self.moving_object.name in tower_names and self.buying_tower:
                                self.towers.add(self.moving_object)
                                self.money -= self.current_tower_cost
                                self.buying_tower = False
                                tower_pos = (int(self.moving_object.x / 64), int(self.moving_object.y / 64))
                                self.map1_dict[tower_pos] = True
                            self.moving_object.moving = False
                            self.moving_object.selected = False
                            self.moving_object.place_color = None
                            self.moving_object = None
                            self.show_grid = False
                            

                    # Start placement of a new tower upon buy button click
                    else:
                        buy_menu_button = self.menu.get_clicked(pos[0], pos[1])
                        if buy_menu_button:
                            cost = self.menu.get_item_cost(buy_menu_button)
                            if self.money >= cost:
                                self.show_grid = True
                                self.current_tower_cost = cost
                                self.add_tower(buy_menu_button)

                # Return to the main screen
                if self.back_button1.rect.collidepoint(pos) and event.button == 1:
                    self.back_button1.clicked = True

    def add_tower(self, name):
        """ Function that allows the player to buy a new tower by using the buy menu.

        Args:
            name (str): Name of the tower to buy. Has to be one of the strings in 'name_list'. Should be given by another method.
        """
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_tower1", "buy_tower2", "buy_tower3", "buy_tower4"]
        object_list = [
            basictower(x, y), 
            dubbletower(x, y),
            heavytower(x, y), 
            missiletower(x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            self.moving_object.selected = True
            obj.moving = True
            self.buying_tower = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")

    async def game_over_screen(self):
        """ A function that holds the game over screen.
        """
        show_screen = True
        text1 = self.font.render("Game Over", True, (0, 0, 0))
        text1_rect = text1.get_rect()
        text1_rect.center = (self.CANVAS_WIDTH / 2, self.CANVAS_HEIGHT / 2)
        back_button2 = button.Button(
            self.CANVAS_WIDTH / 2,
            self.CANVAS_HEIGHT / 2 + 50,
            self.back_button_img_2,
            0.1,
            True)

        while show_screen:
            self.check_events()
            self.window.fill((255, 255, 255))
            self.window.blit(text1, text1_rect)
            back_button2.draw(self.window)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                back_button2.check_button_actions(pos, event)
                if event.type == pygame.QUIT:
                    show_screen = False
                    pygame.quit()
                    sys.exit()
            if back_button2.clicked:
                self.playing = False
                back_button2.clicked = False
                show_screen = False
            pygame.display.update()
            await asyncio.sleep(0)
            
    async def game_won_screen(self):
        """ A function that holds the game won screen.
        """
        show_screen = True
        text1 = self.font.render("You won!", True, (0, 0, 0))
        text1_rect = text1.get_rect()
        text1_rect.center = (self.CANVAS_WIDTH / 2, self.CANVAS_HEIGHT / 2)
        back_button2 = button.Button(
            self.CANVAS_WIDTH / 2,
            self.CANVAS_HEIGHT / 2 + 50,
            self.back_button_img_2,
            0.1,
            True)

        while show_screen:
            self.check_events()
            self.window.fill((255, 255, 255))
            self.window.blit(text1, text1_rect)
            back_button2.draw(self.window)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                back_button2.check_button_actions(pos, event)
                if event.type == pygame.QUIT:
                    show_screen = False
                    pygame.quit()
                    sys.exit()

            if back_button2.clicked:
                self.playing = False
                back_button2.clicked = False
                show_screen = False
            pygame.display.update()
            await asyncio.sleep(0)
                    
