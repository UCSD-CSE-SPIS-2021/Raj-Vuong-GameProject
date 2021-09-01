import pygame
import os
import Fireball
import random

class Flying_Enemy:
    def __init__(self, speed, x_coord, y_coord, left_bound, right_bound, image, fireball_img, fireball_list):
        self.speed = speed
        self.x = x_coord
        self.y = y_coord
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.rect = pygame.Rect(self.x, self.y, 32, 20)
        self.img = image
        self.fb = fireball_img
        self.health = 1
        self.fireball_list = fireball_list
        self.direction = True
        self.counter = random.randint(1, 120)

    def draw(self, screen):
        screen.blit(self.img, self.rect)
    
    def movement(self, player, platform_list):
        self.counter += 1
        if player.rect.left > self.right_bound or player.rect.right < self.left_bound:
            self.rand_movement()
            if self.counter % 120 == 0:
                self.fireball_list.append(self.attack())
            if self.health <= 0:
                return False
            return True
        else:
            if player.get_x() < self.rect.left and self.rect.left > self.left_bound:
                self.rect.move_ip(-self.speed, 0)
            elif player.get_x() > self.rect.right and self.rect.right < self.right_bound:
                self.rect.move_ip(self.speed, 0)
            if self.health <= 0:
                return False
            if self.counter % 120 == 0:
                self.fireball_list.append(self.attack())
            return True

    def rand_movement(self):
        if random.randint(1,90) == 1:
            self.direction = not self.direction
        if not self.direction:
            if self.rect.left > self.left_bound:
                self.rect.move_ip(-2,0)
            else:
                self.direction = not self.direction
        elif self.direction:
            if self.rect.right < self.right_bound:
                self.rect.move_ip(2, 0)
            else:
                self.direction = not self.direction

    def attack(self):
        return Fireball.Fireball(self.rect.left+6, self.rect.bottom, self.fb)

    def decrement_health(self):
        self.health -= 1