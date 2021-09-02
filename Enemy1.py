import pygame
import os
import random

class Charging_Enemy:
    def __init__(self, walk_speed, charge_speed, x_coord, y_coord, left_bound, right_bound, image):
        self.walk_speed = walk_speed
        self.charge_speed = charge_speed
        self.direction = True
        self.x = x_coord
        self.y = y_coord
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.rect = pygame.Rect(self.x, self.y, 35, 30)
        self.imgs = list()
        self.imgs.append(image)
        self.imgs.append(pygame.transform.flip(image, True, False))
        self.charge_state = 0
        self.charge_count = 0
        self.health = 2
        
    def draw(self, screen):
        if self.direction:
            screen.blit(self.imgs[0], self.rect)
        else:
            screen.blit(self.imgs[1], self.rect)

    
    def falling(self, platform_list):
        index = self.rect.collidelist(platform_list)
        if index == -1:
            self.rect.move_ip(0, 2)

    def walking(self):
        if random.randint(1,120) == 1:
            self.direction = not self.direction
        if not self.direction:
            if self.rect.left > self.left_bound:
                self.rect.move_ip(-self.walk_speed,0)
            else:
                self.direction = not self.direction
        elif self.direction:
            if self.rect.right < self.right_bound:
                self.rect.move_ip(self.walk_speed, 0)
            else:
                self.direction = not self.direction
        
    def charging(self, direction, player):
        if self.charge_state == 1:
            self.direction = direction
            self.charge_count += 1
            if self.charge_count > 60:
                self.charge_state = 2
                self.charge_count = 0
        elif self.charge_state == 2:
            if self.rect.colliderect(player.rect):
                player.decrement_health()
            if self.rect.left > self.left_bound and not self.direction:
                self.rect.move_ip(-self.charge_speed,0)
            elif self.rect.right < self.right_bound and self.direction:
                self.rect.move_ip(self.charge_speed, 0)
                return True
            else:
                self.charge_state = 0

    def movement(self, player, platform_list):
        self.falling(platform_list)
        if self.charge_state == 0:
            self.walking()
        if self.charge_state > 0:
            player_direction = True
            if player.rect.right < self.rect.left:
                player_direction = False
            self.charging(player_direction, player)
        if player.rect.left < self.right_bound and player.rect.right > self.left_bound and player.rect.bottom > self.rect.top and player.rect.top < self.rect.bottom and self.charge_state == 0:
            self.charge_state = 1
                
        if self.health <= 0:
            return False
        return True

    def decrement_health(self):
        self.health -= 1
