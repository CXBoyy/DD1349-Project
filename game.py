import pygame, sys
import button
from enemies import enemy
from enemies import single_track as st
from towers.basictower import basictower
import time
from game_wave import Wave

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
        self.show_grid = False
        
        # Buttons
        back_button_img = pygame.image.load("pics/back.png").convert_alpha()
        self.back_button1 = button.Button(500, 50, back_button_img, 0.3, True)
        buy_button_img = pygame.transform.scale(pygame.image.load("pics/buy.png").convert_alpha(), (86, 37))
        self.buy_button = button.Button(600, 20, buy_button_img, 1, True)
        
        self.map1_img = pygame.image.load("assets/New/Terrain/map1_trial.png").convert_alpha()
        self.map1_end = (896, 222)
        self.map1_grid_img = pygame.image.load("assets/New/Terrain/map1_grid.png").convert_alpha()              # Make the grid blit onto the map if the buy button is pressed
        
        self.map1_path = [(0, 97), (32, 97), (101, 97), (155, 97), (224, 97), (287, 97), (287, 160), (287, 220), (287, 288), (275, 340), 
                          (224, 348), (162, 348), (102, 356), (98, 412), (105, 470), (161, 478), (225, 478), (287, 478), (351, 478), (413, 478), 
                          (479, 478), (546, 478), (607, 478), (670, 478), (731, 465), (731, 415), (731, 349), (731, 285), (745, 232), (804, 222), 
                          (870, 222), (896, 222), (900, 222)
                          ]
        
        self.map1_grid_rects = []

        wave1 = [
                 st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
                 st.SingleTrack(self.window, 0, 97, 2, 5, self.map1_path, self.map1_end, self),
                 st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
                 st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self)
                ]
        
        wave2 = [
                 st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
                 st.SingleTrack(self.window, 0, 97, 2, 5, self.map1_path, self.map1_end, self),
                 st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
                 st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
                 st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self),
                 st.SingleTrack(self.window, 0, 97, 5, 5, self.map1_path, self.map1_end, self)
                ]
        
        self.waves = [wave1, wave2]
        self.wave_dict : dict[str, Wave] = dict()
        
        self.health = 10
        counter = 1
        for wave in self.waves:
            wave_string = "wave{}".format(counter)
            counter += 1
            self.wave_dict[wave_string] = Wave()
            for enemy in wave:
                self.wave_dict[wave_string].add(enemy)
        
        # Adding grid rects        
        for x_coordinate in range (0, 896, 64):
            for y_coordinate in range (0, 640, 64):
                self.map1_grid_rects.append(pygame.Rect(x_coordinate, y_coordinate, 64, 64))
                
        
        #print("\n\n", self.map1_grid_rects)
        #print("length: ", len(self.map1_grid_rects))
            
        
        self.towers = [basictower(500,400)
                       ]
        
        self.selected_tower = None
        
        

    def game_loop(self, clock:pygame.time.Clock, map):
        mainClock = clock 
        self.map = map
        font = pygame.font.Font(None, 32)
        text = font.render("Now playing Map 1", True, (0, 0, 0))
        rect = text.get_rect(center=(500, 300))
        loop_counter = 0
        wave_counter = 1
        wave_delay = 6
        next_enemy = "1"
        countdown = wave_delay
        wave_clock = pygame.time.Clock()
        if self.map == "map1":
            start_tick = pygame.time.get_ticks()
            while self.playing:
                timer = wave_clock.tick()
                wave_string = "wave{}".format(wave_counter)
                current_wave = self.wave_dict[wave_string]
                
                pos = pygame.mouse.get_pos()
                
                if not current_wave.wave_started:
                    pass
                
                if not current_wave.wave_started:                           # Checking if the wave has started or not
                    end_tick = pygame.time.get_ticks()
                    countdown = wave_delay + 1 + ((start_tick - end_tick) // 1000)
                    if end_tick - start_tick > wave_delay*1000:
                        loop_counter = 0
                        current_wave.wave_started = True
                        iterator = iter(current_wave)
                        next_enemy = next(iterator, "1")
                        spawned_enemies = Wave()
                
                if current_wave.wave_finished:
                    start_tick = pygame.time.get_ticks()
                    countdown = wave_delay
                    if wave_counter < len(self.wave_dict):
                        wave_counter +=1
                    else:
                        pass
                        #Game won, all waves are over
                
                health_text = font.render((str.format("Lives: {}", self.health)), True, (0, 0, 0))
                health_rect = health_text.get_rect()
                wave_text = font.render((str.format("Currently on Wave {}", wave_counter)), True, (0, 0, 0))
                wave_rect = wave_text.get_rect(center=(250, 11))
                wave_timer_text = font.render((str.format("Time until wave {}:   {} seconds", wave_counter, countdown)), True, (0, 0, 0))
                wave_timer_rect = wave_timer_text.get_rect(center=(600, 11))
                
                # Drawing everything
                self.check_events()
                self.canvas.fill(self.SKY_BLUE)
                self.window.blit(self.canvas, (0,0))
                self.window.blit(self.map1_img, (0,0))
                self.window.blit(text, rect)
                self.window.blit(health_text, health_rect)
                self.window.blit(wave_text, wave_rect)
                self.window.blit(wave_timer_text, wave_timer_rect)
                self.back_button1.draw(self.window)
                self.buy_button.draw(self.window)
                if self.show_grid:
                    self.window.blit(self.map1_grid_img, (0,0))
                
                if current_wave.wave_started:
                    if loop_counter % 120 == 0 and next_enemy != "1":
                        spawned_enemies.add(next_enemy)
                        next_enemy = next(iterator, "1")
                    
                    spawned_iterator = iter(spawned_enemies)
                    #print("List: ", self.enemy_group.sprites())
                    for spawned_enemy in spawned_iterator:
                        #print("Enemy: ", spawnedEnemy)
                        if loop_counter % 150 == 0:
                            spawned_enemy.hit()
                        if spawned_enemy.dead:
                            spawned_enemies.remove(spawned_enemy)
                        
                    spawned_enemies.update()
                    spawned_enemies.draw(self.window)
                    if not bool(spawned_enemies):
                        current_wave.wave_finished = True
                        
                if self.health <= 0:
                    #Game over
                    pass
                    
                for point in self.map1_path:
                    pygame.draw.circle(self.window, (255, 0, 0), point, 5)
                

                # Temporary point for center of tower, delete later
                pygame.draw.circle(self.window, (255, 0, 0), (500, 400), 5)
                
                # draw tower
                for tw in self.towers:
                    tw.draw(self.window)
                    pygame.draw.rect(self.window, (0,0,255), tw.button_rect)

                # loop towers
                for tw in self.towers:
                    #tw.attack(self.enemies)
                    
                    # Moving towers when left clicking on them.
                    if self.selected_tower == tw and tw.moving_tower:
                        for grid_rect in self.map1_grid_rects:
                            if grid_rect.collidepoint(pos):
                                tw.moveTower(grid_rect.center[0] - 32, grid_rect.center[1] - 32)
                
                # Button interactions
                if self.back_button1.clicked:
                    self.playing = False
                    self.back_button1.clicked = False
                if self.buy_button.clicked:
                    print("Buying a tower")
                    self.show_grid = True
                    pass
                    # Place a tower
                pygame.display.update()
                loop_counter += 1
                mainClock.tick(60)
        #pygame.quit()

    def check_events(self):
        pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                pygame.quit()
                sys.exit()
                
            for tw in self.towers:
                result_of_action = tw.check_tower_actions(pos, event)
                if not isinstance(result_of_action, bool):
                    self.selected_tower = result_of_action
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.buy_button.rect.collidepoint(pos) and event.button == 1:
                    if self.show_grid is False:
                        self.show_grid = True
                    else:
                        self.show_grid = False
                if event.button == 1:
                    self.LEFTMOUSECLICK = True
                    
                if self.back_button1.rect.collidepoint(pos) and event.button == 1:
                    self.back_button1.clicked = True
                    


    def reset_vars(self):
        self.LEFTMOUSECLICK = False
