import pygame
import os
import random
import Player
import Enemy1
import Enemy2
import Levels
import Boss

# These are the dimensions of the background image for our game
screen_length = 1000
screen_height = 563
dim_field = (screen_length, screen_height)

screen = pygame.display.set_mode(dim_field)

rect_player = pygame.Rect(10, screen_height-40, 24, 30)

player = pygame.image.load(os.path.join("assets", "PlayerStill.png")).convert()
player.set_colorkey((0,0,0))

win_bg = pygame.image.load(os.path.join("assets", "winscreen.png")).convert()
lose_bg = pygame.image.load(os.path.join("assets", "losescreen.png")).convert()

enemy1_img = pygame.image.load(os.path.join("assets", "chargingenemy.png")).convert()
enemy1_img.set_colorkey((0,0,0))

pygame.font.init()
font = pygame.font.SysFont("dejavusansmono", 25)

print(pygame.font.get_fonts())

enemy2_img = pygame.image.load(os.path.join("assets", "FlyingEnemy.png")).convert()
enemy2_img.set_colorkey((0,0,0))

boss_img = pygame.image.load(os.path.join("assets", "boss.png")).convert()
boss_img.set_colorkey((0,0,0))
boss_img = pygame.transform.scale(boss_img, (120,120))

fireball_img = pygame.image.load(os.path.join("assets", "fireball.png")).convert()
fireball_img.set_colorkey((0,0,0))

fireball_list = list()

lvl_db = Levels.Levels(fireball_list)

rect_door = pygame.Rect(950, 40, 30, 35)
door = pygame.image.load(os.path.join("assets", "door.png")).convert()
door.set_colorkey((0,0,0))
open_door = pygame.image.load(os.path.join("assets", "opendoor.png")).convert()
open_door.set_colorkey((0,0,0))

current_door = door

#platform and enemy naming type_LVL_NUMBER
platform = pygame.image.load(os.path.join("assets", "Platform.gif")).convert()

ground = pygame.Rect(0, screen_height-10, screen_length, 10)

player_imgs = list()
player_imgs.append(pygame.image.load(os.path.join("assets", "PlayerStill.png")).convert())
player_imgs.append(pygame.transform.flip(player_imgs[0], True, False))

punch = pygame.image.load(os.path.join("assets", "punch.png")).convert()
punch.set_colorkey((0,0,0))

clock = pygame.time.Clock()
running = True
FPS = 60
step_size = 5
step_size_fall = 2
jump_size = 10

cur_lvl = 1

frame_counter = 0

p = Player.Player(player, rect_player, step_size, step_size_fall, punch, jump_size)

platform_list = lvl_db.cur_platforms(cur_lvl)

platform_img_list = lvl_db.cur_platform_imgs(cur_lvl)

fireball_collision = platform_list + [rect_player]

enemy_list = lvl_db.cur_enemy(cur_lvl)
enemy_rect_list = lvl_db.cur_enemy_rect(cur_lvl)

boss = Boss.Boss(lvl_db.cur_enemy(3), lvl_db.cur_enemy_rect(3), boss_img, enemy1_img, enemy2_img, fireball_img, fireball_list)

background = lvl_db.cur_bg(cur_lvl)

draw_door = True

win_state = 0

while(running):
    clock.tick(FPS)

    if win_state == 0:

        if len(enemy_list) == 0:
            current_door = open_door
            if p.rect.colliderect(rect_door):
                cur_lvl += 1
                current_door = door
                platform_list = lvl_db.cur_platforms(cur_lvl)
                platform_img_list = lvl_db.cur_platform_imgs(cur_lvl)
                enemy_list = lvl_db.cur_enemy(cur_lvl)
                enemy_rect_list = lvl_db.cur_enemy_rect(cur_lvl)
                background = lvl_db.cur_bg(cur_lvl)
                fireball_collision = platform_list + [rect_player]
                p.respawn()
        frame_counter += 1    

        running = p.states(screen_length, platform_list, pygame.event.get(), pygame.key.get_pressed())

        screen.fill((255, 255, 0))
        screen.blit(background, (0,0)) 
        if draw_door:
            screen.blit(current_door, rect_door)
        
        for enemy in enemy_list:
            if enemy.movement(p, platform_list):
                enemy.draw(screen)
            else:
                enemy_list.remove(enemy)
                enemy_rect_list.remove(enemy.rect)

        
        for i in range(len(platform_list)):
            screen.blit(platform_img_list[i], platform_list[i])
        for fireball in fireball_list:
            if fireball.fall(fireball_collision, p):
                fireball.draw(screen)
            else:
                fireball_list.remove(fireball)

        if cur_lvl == 3:
            draw_door = False
            if not boss.stage_1():
                cur_lvl = 4
                platform_list = lvl_db.cur_platforms(cur_lvl)
                platform_img_list = lvl_db.cur_platform_imgs(cur_lvl)
                enemy_list = lvl_db.cur_enemy(cur_lvl)
                enemy_rect_list = lvl_db.cur_enemy_rect(cur_lvl)
                background = lvl_db.cur_bg(cur_lvl)
                fireball_collision = platform_list + [rect_player]
            
        if cur_lvl == 4:
            if not boss.stage_2(p):
                cur_lvl = 5
                platform_list = lvl_db.cur_platforms(cur_lvl)
                platform_img_list = lvl_db.cur_platform_imgs(cur_lvl)
                enemy_list = lvl_db.cur_enemy(cur_lvl)
                enemy_rect_list = lvl_db.cur_enemy_rect(cur_lvl)
                background = lvl_db.cur_bg(cur_lvl)
                fireball_collision = platform_list + [rect_player]

        if cur_lvl == 5:
            boss.stage_3(p)
            if boss.health <= 0:
                win_state = 1

        if cur_lvl >= 3:
            boss.draw(screen)

        p.draw(screen)
        if cur_lvl <= 3:
            p.attack(screen, enemy_list, enemy_rect_list)
        else:
            p.attack(screen, [boss], [boss.rect])
        
        text = font.render("HEALTH: " + str(p.health), True, (255,255,255))

        screen.blit(text, (10,10))

        if cur_lvl >= 3:
            boss_text = font.render("BOSS HEALTH: " + str(boss.health), True, (255,255,255))
            screen.blit (boss_text, (10, 45))
        
        if p.health <= 0:
            win_state = 2

    elif win_state == 1:
        screen.blit(win_bg, (0,0))
        running = False 
    
    else:
        screen.blit(lose_bg, (0,0))
        running = False
    
    pygame.display.update()