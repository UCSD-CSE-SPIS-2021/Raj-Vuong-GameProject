import pygame
import os
import random
import Enemy1
import Enemy2
import Fireball
import math

class Boss:
    def __init__(self, enemy_list, enemy_rect_list, img, enemy1_img, enemy2_img, fireball_img, fireball_list):
        self.stage = 1
        self.img = img
        self.rect = pygame.Rect(440, 203, 120, 120)
        self.enemy_list = enemy_list
        self.enemy_rect_list = enemy_rect_list
        self.counter = 0
        self.enemy_count = 0
        self.mask = pygame.mask.from_surface(img)
        self.enemy1_img = enemy1_img
        self.enemy2_img = enemy2_img
        self.fireball_img = fireball_img
        self.fireball_list = fireball_list
        self.health = 300
        self.charge_state = 1
        self.charge_count = 0
        self.degree = 0
        self.dx = 0
        self.dy = 0
        
    def draw(self, screen):
        # pygame.draw.rect(screen, (255,0,0), self.rect)
        screen.blit(self.img, self.rect)

    def stage_1(self):
        self.counter += 1
        if self.counter % 120 == 0 and self.enemy_count < 10:
            if random.randint(1,2) == 1:
                rand_num = random.randint(1,4)
                x_coord = random.randint((rand_num-1)*250, rand_num*250)
                left_bound = (rand_num-1) * 250
                right_bound = rand_num * 250
                enemy = Enemy1.Charging_Enemy(1, 10, x_coord, 523, left_bound, right_bound, self.enemy1_img)
                self.enemy_list.append(enemy)
                self.enemy_rect_list.append(enemy.rect)
                self.enemy_count += 1
            else:
                rand_num = random.randint(1,4)
                x_coord = random.randint((rand_num-1)*250, rand_num*250)
                left_bound = (rand_num-1) * 250
                right_bound = rand_num * 250
                y_coord = random.randint(320 ,503)
                if random.randint(1,2) == 1:
                    x_coord = random.randint(530, 710)
                    left_bound = 530
                    right_bound = 1000
                enemy = Enemy2.Flying_Enemy(3, x_coord, y_coord, left_bound, right_bound, self.enemy2_img, self.fireball_img, self.fireball_list)
                self.enemy_list.append(enemy)
                self.enemy_rect_list.append(enemy.rect)
                self.enemy_count += 1
        if self.enemy_count >= 10 and len(self.enemy_list) == 0:
            self.counter = 0
            return False
        else:
            return True
    
    def stage_2(self, player):
        self.counter += 1
        if self.counter < 90:
            self.rect.move_ip(0, -1)
        else:
            if self.counter % 90 == 0:
                self.fireball_list.append(self.fireball_atk())
            if self.health <= 150:
                return False
            if player.get_x() <= (self.rect.left+self.rect.right)//2 and self.rect.left > 0:
                self.rect.move_ip(-3, 0)
            elif player.get_x() >= (self.rect.left+self.rect.right)//2 and self.rect.right < 1000:
                self.rect.move_ip(3, 0)
        return True
    
    def stage_3(self, player):
        if self.charge_state == 1:
            self.charge_count += 1
            if self.charge_count > 90:
                self.charge_state = 2
                self.charge_count = 0
                self.degree = math.atan2(player.rect.top-(self.rect.bottom-20), player.rect.left - (self.rect.left+self.rect.right)/2)
                self.dx = 10*math.cos(self.degree)
                self.dy = 10*math.sin(self.degree)
        elif self.charge_state == 2:
            if self.collide(player.rect, player.mask):
                player.decrement_health()
            if self.rect.bottom + self.dy < 563 and self.rect.top + self.dy > 0 and self.rect.left + self.dx > 0 and self.rect.right + self.dx < 1000:
                self.rect.move_ip(self.dx, self.dy)
            else:
                self.charge_state = 1
        
            
    def decrement_health(self):
        self.health -= 10
        
    
    def fireball_atk(self):
        return Fireball.Fireball(self.rect.left+40, self.rect.bottom, self.fireball_img, 2)

    def collide(self, rect, mask):
        offset_x = self.rect.left - rect.left
        offset_y = self.rect.top - rect.top
        return mask.overlap(self.mask,(offset_x,offset_y)) != None



