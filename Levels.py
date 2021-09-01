import pygame
import os
import random
import Player
import Enemy1
import Enemy2

class Levels:

    def __init__(self, fireball_list):
        
        self.screen_length = 1000
        self.screen_height = 563
        self.dim_field = (self.screen_length, self.screen_height)

        self.fireball_list = fireball_list
        
        # lvl 1

        self.bg_1 = pygame.image.load(os.path.join("assets","lvl1.png")).convert()
        self.bg_1 = pygame.transform.scale(self.bg_1, self.dim_field)
        self.enemy1_img = pygame.image.load(os.path.join("assets", "chargingenemy.png")).convert()
        self.enemy1_img.set_colorkey((0,0,0))

        self.enemy2_img = pygame.image.load(os.path.join("assets", "FlyingEnemy.png")).convert()
        self.enemy2_img.set_colorkey((0,0,0))

        self.platform = pygame.image.load(os.path.join("assets", "Platform.gif")).convert()

        self.ground = pygame.Rect(0, self.screen_height-10, self.screen_length, 10)
        self.platform_1_0 = pygame.Rect(100, 450, 150, 10)
        self.platform_1_1 = pygame.Rect(500, 350, 125, 10)
        self.platform_1_2 = pygame.Rect(50, 275, 175, 10)
        self.platform_1_3 = pygame.Rect(800, 250, 100, 10)
        self.platform_1_4 = pygame.Rect(450, 175, 100, 10)
        self.platform_1_5 = pygame.Rect(200, 125, 125, 10)
        self.platform_1_6 = pygame.Rect(800, 75, 200, 10)

        self.platform_1_list = [self.ground, self.platform_1_0, self.platform_1_1, self.platform_1_2, self.platform_1_3, self.platform_1_4, self.platform_1_5, self.platform_1_6]

        self.platform_img_1_list = list()

        for i in range (len(self.platform_1_list)):
            self.platform_img_1_list.append(pygame.transform.scale(self.platform, (self.platform_1_list[i].w, self.platform_1_list[i].h)))

        self.enemy_1_0 = Enemy1.Charging_Enemy(1, 10, 500, 320, self.platform_1_1.left, self.platform_1_1.right, self.enemy1_img)
        self.enemy_1_1 = Enemy1.Charging_Enemy(1, 10, 75, 245, self.platform_1_2.left, self.platform_1_2.right, self.enemy1_img)
        self.enemy_1_2 = Enemy1.Charging_Enemy(1, 10, 850, 220, self.platform_1_3.left, self.platform_1_3.right, self.enemy1_img)
        self.enemy_1_3 = Enemy1.Charging_Enemy(1, 10, 450, 145, self.platform_1_4.left, self.platform_1_4.right, self.enemy1_img)
        self.enemy_1_4 = Enemy1.Charging_Enemy(1, 10, 250, 95, self.platform_1_5.left, self.platform_1_5.right, self.enemy1_img)
        self.enemy_1_5 = Enemy1.Charging_Enemy(1, 10, 800, 45, self.platform_1_6.left, self.platform_1_6.right, self.enemy1_img)

        self.enemy_1_list = [self.enemy_1_0, self.enemy_1_1, self.enemy_1_2, self.enemy_1_3, self.enemy_1_4, self.enemy_1_5]

        self.enemy_1_rect_list = list()
        for enemy in self.enemy_1_list:
            self.enemy_1_rect_list.append(enemy.rect)
        
        # lvl 2

        self.bg_2 = pygame.image.load(os.path.join("assets","lvl2.png")).convert()
        self.bg_2 = pygame.transform.scale(self.bg_2, self.dim_field)

        self.fireball_img = pygame.image.load(os.path.join("assets", "fireball.png")).convert()
        self.fireball_img.set_colorkey((0,0,0))

        self.platform_2_0 = pygame.Rect(150, 450, 150, 10)
        self.platform_2_1 = pygame.Rect(550, 325, 100, 10)
        self.platform_2_2 = pygame.Rect(75, 300, 175, 10)
        self.platform_2_3 = pygame.Rect(850, 250, 120, 10)
        self.platform_2_4 = pygame.Rect(475, 150, 80, 10)
        self.platform_2_5 = pygame.Rect(800, 75, 200, 10)

        self.platform_2_list = [self.ground, self.platform_2_0, self.platform_2_1, self.platform_2_2, self.platform_2_3, self.platform_2_4, self.platform_2_5]

        self.platform_img_2_list = list()

        for i in range (len(self.platform_2_list)):
            self.platform_img_2_list.append(pygame.transform.scale(self.platform, (self.platform_2_list[i].w, self.platform_2_list[i].h)))
        
        self.enemy_2_0 = Enemy1.Charging_Enemy(1, 10, 200, 420, self.platform_2_0.left, self.platform_2_0.right, self.enemy1_img)
        self.enemy_2_1 = Enemy1.Charging_Enemy(1, 10, 575, 295, self.platform_2_1.left, self.platform_2_1.right, self.enemy1_img)
        self.enemy_2_2 = Enemy1.Charging_Enemy(1, 10, 150, 270, self.platform_2_2.left, self.platform_2_2.right, self.enemy1_img)
        self.enemy_2_3 = Enemy1.Charging_Enemy(1, 10, 875, 220, self.platform_2_3.left, self.platform_2_3.right, self.enemy1_img)
        self.enemy_2_4 = Enemy1.Charging_Enemy(1, 10, 475, 120, self.platform_2_4.left, self.platform_2_4.right, self.enemy1_img)
        self.enemy_2_5 = Enemy1.Charging_Enemy(1, 10, 825, 45, self.platform_2_5.left, self.platform_2_5.right, self.enemy1_img)
        self.enemy_2_6 = Enemy2.Flying_Enemy(3, 300, 280, 300, 550, self.enemy2_img, self.fireball_img, self.fireball_list)
        self.enemy_2_7 = Enemy2.Flying_Enemy(3, 700, 220, 650, 850, self.enemy2_img, self.fireball_img, self.fireball_list)
        self.enemy_2_8 = Enemy2.Flying_Enemy(3, 350, 100, 150, 475, self.enemy2_img, self.fireball_img, self.fireball_list)
        self.enemy_2_9 = Enemy2.Flying_Enemy(3, 750, 25, 550, 1000, self.enemy2_img, self.fireball_img, self.fireball_list)

        self.enemy_2_list = [self.enemy_2_0, self.enemy_2_1, self.enemy_2_2, self.enemy_2_3, self.enemy_2_4, self.enemy_2_5, self.enemy_2_6, self.enemy_2_7, self.enemy_2_8, self.enemy_2_9]

        self.enemy_2_rect_list = list()
        for enemy in self.enemy_2_list:
            self.enemy_2_rect_list.append(enemy.rect)


        # lvl 3

        self.bg_3 = pygame.image.load(os.path.join("assets","lvl3.png")).convert()
        self.bg_3 = pygame.transform.scale(self.bg_3, self.dim_field)
        self.enemy_3_list = list()
        self.enemy_3_rect_list = list()
        self.platform_3_list =[self.ground]
        self.platform_img_3_list = [pygame.transform.scale(self.platform, (self.ground.w, self.ground.h))]

        # lvl 4
        
        self.bg_4 = pygame.image.load(os.path.join("assets","lvl3.png")).convert()
        self.bg_4 = pygame.transform.scale(self.bg_4, self.dim_field)

        self.enemy_4_list = list()
        self.enemy_4_rect_list = list()

        self.platform_4_0 = pygame.Rect(200, 400, 200, 10)
        self.platform_4_1 = pygame.Rect(600, 400, 200, 10)
        self.platform_4_list = [self.ground, self.platform_4_0, self.platform_4_1]

        self.platform_img_4_list = list()

        for i in range (len(self.platform_4_list)):
            self.platform_img_4_list.append(pygame.transform.scale(self.platform, (self.platform_4_list[i].w, self.platform_4_list[i].h)))

        # lvl 5

        self.bg_5 = pygame.image.load(os.path.join("assets","lvl3.png")).convert()
        self.bg_5 = pygame.transform.scale(self.bg_5, self.dim_field)

        self.enemy_5_list = list()
        self.enemy_5_rect_list = list()

        self.platform_5_0 = pygame.Rect(200, 400, 200, 10)
        self.platform_5_1 = pygame.Rect(600, 400, 200, 10)
        self.platform_5_2 = pygame.Rect(0, 250, 200, 10)
        self.platform_5_3 = pygame.Rect(800, 250, 200, 10)
        self.platform_5_list = [self.ground, self.platform_5_0, self.platform_5_1, self.platform_5_2, self.platform_5_3]

        self.platform_img_5_list = list()

        for i in range (len(self.platform_5_list)):
            self.platform_img_5_list.append(pygame.transform.scale(self.platform, (self.platform_5_list[i].w, self.platform_5_list[i].h)))
        

    def cur_platforms(self, lvl):
        if lvl == 1:
            return self.platform_1_list
        if lvl == 2:
            return self.platform_2_list
        if lvl == 3:
            return self.platform_3_list
        if lvl == 4:
            return self.platform_4_list
        if lvl == 5:
            return self.platform_5_list
        else:
            return self.platform_1_list
    
    def cur_platform_imgs(self, lvl):
        if lvl == 1:
            return self.platform_img_1_list
        if lvl == 2:
            return self.platform_img_2_list
        if lvl == 3:
            return self.platform_img_3_list
        if lvl == 4:
            return self.platform_img_4_list
        if lvl == 5:
            return self.platform_img_5_list
        else:
            return self.platform_img_1_list

    def cur_enemy(self, lvl):
        if lvl == 1:
            return self.enemy_1_list
        if lvl == 2:
            return self.enemy_2_list
        if lvl == 3:
            return self.enemy_3_list
        if lvl == 4:
            return self.enemy_4_list
        if lvl == 5:
            return self.enemy_5_list
        else:
            return self.enemy_1_list
    
    def cur_enemy_rect(self, lvl):
        if lvl == 1:
            return self.enemy_1_rect_list
        if lvl == 2:
            return self.enemy_2_rect_list
        if lvl == 3:
            return self.enemy_3_rect_list
        if lvl == 4:
            return self.enemy_4_rect_list
        if lvl == 5:
            return self.enemy_5_rect_list
        else:
            return self.enemy_1_rect_list

    def cur_bg(self, lvl):
        if lvl == 1:
            return self.bg_1
        if lvl == 2:
            return self.bg_2
        if lvl == 3:
            return self.bg_3
        if lvl == 4:
            return self.bg_4
        if lvl == 5:
            return self.bg_5
        else:
            return self.bg_1