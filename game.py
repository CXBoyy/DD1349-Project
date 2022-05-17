from xmlrpc.client import boolean
from numpy import not_equal
import pygame, sys
import math
import button
from enemies import enemy
from enemies import single_track as st
from towers.basictower import basictower
import time
from game_wave import Wave
from projectile import Projectile
from tower_menu import Buymenu



money_button = pygame.image.load(r"assets/New/button_test_1.png")
buy_menu_img = pygame.image.load(r"assets/New/buy_menu_test_1.png")
buy_tower = pygame.image.load(r"assets/New/buy_tower_test.png")

tower_names = ["buy_tower1", "buy_tower2", "buy_tower3", "buy_tower4"]

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
        self.font = pygame.font.Font(None, 32)
        
        # Buttons
        self.back_button_img = pygame.image.load("pics/back.png").convert_alpha()
        self.back_button1 = button.Button(500, 50, self.back_button_img, 0.3, True)
        self.buy_button_img = pygame.transform.scale(pygame.image.load("pics/buy.png").convert_alpha(), (86, 37))
        self.buy_button = button.Button(600, 20, self.buy_button_img, 1, True)

        
        self.map1_img = pygame.image.load("assets/New/Terrain/map1_trial.png").convert_alpha()
        self.map1_end = (896, 222)
        self.map1_grid_img = pygame.image.load("assets/New/Terrain/map1_grid.png").convert_alpha()              # Make the grid blit onto the map if the buy button is pressed
        
        self.map1_path = [(0, 97), (32, 97), (101, 97), (155, 97), (224, 97), (287, 97), (287, 160), (287, 220), (287, 288), (275, 340), 
                          (224, 348), (162, 348), (102, 356), (98, 412), (105, 470), (161, 478), (225, 478), (287, 478), (351, 478), (413, 478), 
                          (479, 478), (546, 478), (607, 478), (670, 478), (731, 465), (731, 415), (731, 349), (731, 285), (745, 232), (804, 222), 
                          (870, 222), (896, 222), (900, 222)
                          ]
        
        self.map1_grid_rects = []
        self.map1_path_rects = []

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
            
        # Adding path rects
        #self.map1_path_rects = [self.map1_grid_rects[14], self.map1_grid_rects[15], self.map1_grid_rects[16], self.map1_grid_rects[17], self.map1_grid_rects[18], self.map1_grid_rects[32], self.map1_grid_rects[46], self.map1_grid_rects[60], self.map1_grid_rects[71], self.map1_grid_rects[72], self.map1_grid_rects[73], self.map1_grid_rects[74], self.map1_grid_rects[85], self.map1_grid_rects[99], self.map1_grid_rects[100], self.map1_grid_rects[101], self.map1_grid_rects[102], self.map1_grid_rects[103], self.map1_grid_rects[104], self.map1_grid_rects[105], self.map1_grid_rects[106], self.map1_grid_rects[107], self.map1_grid_rects[108], self.map1_grid_rects[109], self.map1_grid_rects[95], self.map1_grid_rects[81], self.map1_grid_rects[67], self.map1_grid_rects[53], self.map1_grid_rects[54], self.map1_grid_rects[55]]
        self.map1_path_rects = [self.map1_grid_rects[1], self.map1_grid_rects[11], self.map1_grid_rects[21], self.map1_grid_rects[31], self.map1_grid_rects[41], self.map1_grid_rects[42], self.map1_grid_rects[43], self.map1_grid_rects[44], self.map1_grid_rects[45], self.map1_grid_rects[35], self.map1_grid_rects[25], self.map1_grid_rects[15], self.map1_grid_rects[16], self.map1_grid_rects[17], self.map1_grid_rects[27], self.map1_grid_rects[37], self.map1_grid_rects[47], self.map1_grid_rects[57], self.map1_grid_rects[67], self.map1_grid_rects[77], self.map1_grid_rects[87], self.map1_grid_rects[97], self.map1_grid_rects[107], self.map1_grid_rects[117], self.map1_grid_rects[116], self.map1_grid_rects[115], self.map1_grid_rects[114], self.map1_grid_rects[113], self.map1_grid_rects[123], self.map1_grid_rects[133]] 
            
        
        self.towers = []
        
        self.selected_tower = None
        
        # Test projectile
        #self.test_projectile = Projectile(self.towers[0], wave1[3])
    
        self.money = 1000
        self.life_font = pygame.font.SysFont("comicsans", 35)
        
        self.menu = Buymenu(self.CANVAS_WIDTH - buy_menu_img.get_width()/2, self.CANVAS_HEIGHT, buy_menu_img)
        self.menu.add_button(buy_tower, "buy_tower1", 250)
        self.menu.add_button(buy_tower, "buy_tower2", 350)
        self.menu.add_button(buy_tower, "buy_tower3", 450)
        self.menu.add_button(buy_tower, "buy_tower4", 550)
        
        self.moving_object = None
        

    def game_loop(self, clock:pygame.time.Clock, map):
        mainClock = clock 
        self.map = map
        font = self.font
        text = font.render("Now playing Map 1", True, (0, 0, 0))
        rect = text.get_rect(center=(500, 300))
        loop_counter = 0
        wave_counter = 1
        wave_delay = 6
        spawn_delay = 120
        next_enemy = "1"
        countdown = wave_delay
        game_won = False
        wave_clock = pygame.time.Clock()
        if self.map == "map1":
            start_tick = pygame.time.get_ticks()
            projectiles = pygame.sprite.Group()
            while self.playing:
                timer = wave_clock.tick()
                wave_string = "wave{}".format(wave_counter)
                current_wave = self.wave_dict[wave_string]
                
                pos = pygame.mouse.get_pos()
                
                # check for moving object
                if self.moving_object:
                    for grid_rect in self.map1_grid_rects:
                        if grid_rect.collidepoint(pos):
                            self.moving_object.moveTower(grid_rect.center[0] - 32, grid_rect.center[1] - 32)
                            tower_list = self.towers[:]
                            collide = False
                    for tower in tower_list:
                        if tower.collide(self.moving_object):
                            collide = True
                            tower.place_color = (255, 0, 0, 100)
                            self.moving_object.place_color = (255, 0, 0, 100)
                        if self.moving_object.tower_rect.collidelist(self.map1_path_rects) != -1:
                            collide = True
                            self.moving_object.place_color = (255, 0, 0, 100)
                        else:
                            tower.place_color = (0, 255, 0, 100)
                            if not collide:
                                self.moving_object.place_color = (0, 255, 0, 100)
                
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
                        game_won = True
                
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
                
                # Draw currency
                text_money = self.life_font.render(str(self.money), 1, (255, 255, 255))
                money = pygame.transform.scale(money_button, (50, 50))
                start_x = self.CANVAS_WIDTH - money_button.get_width() - 10

                self.window.blit(text_money, (start_x - text_money.get_width() - 10, 75))
                self.window.blit(money, (start_x, 65))
                
                if self.show_grid:
                    self.window.blit(self.map1_grid_img, (0,0))
                
                for tw in self.towers:
                    print("Inside tower loop")
                    # Moving towers when left clicking on them.
                    if self.selected_tower == tw and tw.moving_tower:
                        for grid_rect in self.map1_grid_rects:
                            if grid_rect.collidepoint(pos):
                                tw.moveTower(grid_rect.center[0] - 32, grid_rect.center[1] - 32)
                                
                if current_wave.wave_started:
                    if loop_counter % spawn_delay == 0 and next_enemy != "1":
                        spawned_enemies.add(next_enemy)
                        next_enemy = next(iterator, "1")
                    
                    spawned_iterator = iter(spawned_enemies)
                    #print("List: ", self.enemy_group.sprites())
                    for spawned_enemy in spawned_iterator:
                        #print("Enemy: ", spawnedEnemy)
                        if loop_counter % 150 == 0:
                            #spawned_enemy.hit()
                            pass
                        if spawned_enemy.dead:
                            spawned_enemies.remove(spawned_enemy)
                        
                    spawned_enemies.update()
                    spawned_enemies.draw(self.window)
                    if not bool(spawned_enemies):
                        current_wave.wave_finished = True
                    for tw in self.towers:
                        # Moving towers when left clicking on them.
                        if self.selected_tower == tw and tw.moving_tower:
                            for grid_rect in self.map1_grid_rects:
                                if grid_rect.collidepoint(pos):
                                    tw.moveTower(grid_rect.center[0] - 32, grid_rect.center[1] - 32)
                                    
                        for enemy in self.waves[wave_counter - 1]:
                            if not enemy.dead:
                                boolean_in_range = tw.is_in_range(enemy)
                                if tw.target is not None and tw.target != enemy and not tw.is_in_range(tw.target):
                                    tw.target = enemy
                                if boolean_in_range is True and tw.cooldown_counter % tw.cooldown == 0:
                                    if tw.target == None or tw.target == enemy or tw.target.dead is True or not tw.is_in_range(tw.target):
                                        tw.target = enemy
                                        projectiles.add(tw.attack2(enemy, tw.damage))
                                # projectiles.update()
                                # projectiles.draw(self.window)
                        for projectile in projectiles:
                            if projectile.dead:
                                projectiles.remove(projectile)
                                print("Projectiles: ", projectiles.sprites())
                        tw.cooldown_counter += 1
                    projectiles.update()
                    projectiles.draw(self.window)
                        
                    
                for point in self.map1_path:
                    pygame.draw.circle(self.window, (255, 0, 0), point, 5)
                

                # Temporary point for center of tower, delete later
                pygame.draw.circle(self.window, (255, 0, 0), (500, 400), 5)
                
                # draw tower
                for tw in self.towers:
                    tw.draw(self.window)
                    pygame.draw.rect(self.window, (0,0,255), tw.button_rect)
                    
                # draw moving tower
                if self.moving_object:
                    self.moving_object.draw(self.window)
                    self.moving_object.draw_placement(self.window)
                    for tower in self.towers:
                        tower.draw_placement(self.window)
                
                # draw menu
                self.menu.draw(self.window)
                
                # Button interactions
                if self.back_button1.clicked:
                    self.playing = False
                    self.back_button1.clicked = False
                if self.buy_button.clicked:
                    print("Buying a tower")
                    self.show_grid = True
                    pass
                    # Place a tower
                if self.health <= 0:
                    self.game_over_screen()
                if game_won:
                    self.game_won_screen()
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
                    
                
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 3:
                            if self.moving_object:
                                not_allowed = False
                                tower_list = self.towers[:]
                                for tower in tower_list:
                                    if tower.collide(self.moving_object):
                                        not_allowed = True
                                    if self.moving_object.tower_rect.collidelist(self.map1_path_rects) != -1:
                                        not_allowed = True
                                if not not_allowed:
                                    if self.moving_object.name in tower_names:
                                        self.towers.append(self.moving_object)
                                    self.moving_object.moving = False
                                    self.moving_object = None 
                                    self.show_grid = False
                            else:
                                buy_menu_button = self.menu.get_clicked(pos[0], pos[1])
                                if buy_menu_button:
                                    print(buy_menu_button)
                                    cost = self.menu.get_item_cost(buy_menu_button)
                                    if self.money >= cost:
                                        self.show_grid = True
                                        self.money -= cost
                                        self.add_tower(buy_menu_button)
                    
    def reset_vars(self):
        self.LEFTMOUSECLICK = False
        
    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_tower1", "buy_tower2", "buy_tower3", "buy_tower3"]
        object_list = [basictower(x,y), basictower(x,y), basictower(x,y), basictower(x,y)]
        
        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")

    def game_over_screen(self):
        show_screen = True
        text1 = self.font.render("Game Over", True, (0, 0, 0))
        text1_rect = text1.get_rect()
        text1_rect.center = (self.CANVAS_WIDTH/2, self.CANVAS_HEIGHT/2)
        back_button2 = button.Button(self.CANVAS_WIDTH/2, self.CANVAS_HEIGHT/2 + 50, self.back_button_img, 0.1, True)
        
        while show_screen:
            self.window.fill((255,255,255))
            self.window.blit(text1, text1_rect)
            back_button2.draw(self.window)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                back_button2.check_button_actions(pos, event)
            if back_button2.clicked:
                print("Clicked game over")
                self.playing = False
                back_button2.clicked = False
                show_screen = False
            pygame.display.update()
            
    def game_won_screen(self):
        show_screen = True
        text1 = self.font.render("You won!", True, (0, 0, 0))
        text1_rect = text1.get_rect()
        text1_rect.center = (self.CANVAS_WIDTH/2, self.CANVAS_HEIGHT/2)
        back_button2 = button.Button(self.CANVAS_WIDTH/2, self.CANVAS_HEIGHT/2 + 50, self.back_button_img, 0.1, True)
        
        while show_screen:
            self.window.fill((255,255,255))
            self.window.blit(text1, text1_rect)
            back_button2.draw(self.window)
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()
                back_button2.check_button_actions(pos, event)
            if back_button2.clicked:
                self.playing = False
                back_button2.clicked = False
                show_screen = False
            pygame.display.update()
                    