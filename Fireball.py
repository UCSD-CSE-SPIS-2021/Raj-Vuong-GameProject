import pygame
import os
import Enemy2

class Fireball:
    def __init__(self, x_coord, y_coord, img, scale = 1):
        self.fall_step = 4
        self.x = x_coord
        self.y = y_coord
        self.rect = pygame.Rect(self.x, self.y, 20 * scale, 30 * scale)
        self.img = img
        if scale > 1:
            self.img = pygame.transform.scale(self.img, (20*scale, 30*scale))
        
    
    def fall(self, collision_list, player):
        index = self.rect.collidelist(collision_list)
        if index == -1:
            self.rect.move_ip(0, self.fall_step)
            return True
        if index == len(collision_list)-1:
            player.decrement_health()
        return False

    def draw(self, screen):
        screen.blit(self.img, self.rect)