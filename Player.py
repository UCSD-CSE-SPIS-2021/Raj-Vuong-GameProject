import pygame
import os
import Enemy1
import Enemy2


class Player:

    def __init__(self, image, rectangle, step, fall, melee_image, jumpSize):
        self.health = 100
        self.imgs = list()
        self.imgs.append(image)
        self.imgs.append(pygame.transform.flip(image, True, False))
        self.score = 0
        self.rect = rectangle
        self.step_size = step
        self.step_size_fall = fall
        self.state = 0
        self.attack_state = 0
        self.jump_count = 0
        self.jump_number = 0
        self.direction = True
        self.melee_imgs = list()
        self.melee_imgs.append(melee_image)
        self.melee_imgs.append(pygame.transform.flip(melee_image, True, False))
        self.attack_count = 0
        self.jump_size = jumpSize
        self.acceleration = 0.05
        self.falling_counter = 0
        self.immunity_counter = 0
        self.attacked = False
        self.mask = pygame.mask.from_surface(image)

    def draw(self, screen):
        if self.direction:
            screen.blit(self.imgs[0], self.rect)
        else:
            screen.blit(self.imgs[1], self.rect)

    def input(self, events, keys, screen_length, platform_list):
        running = True
        click_up = False
        click_space = False
        for event in events:
            if event.type == pygame.QUIT:
                print("You killed the window")
                running = False
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        click_up = True
                    if event.key == pygame.K_SPACE:
                        click_space = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            # print("Left")
            self.direction = False
            # move the rect_player to the left by step_size
            overlap = False
            for platform in platform_list:
                if self.rect.top > platform.top - 25 and self.rect.top < platform.top + 10 and self.rect.left - self.step_size < platform.right and self.rect.left - self.step_size > platform.left:
                    overlap = True
            if self.rect.left > 0 and not overlap:
                self.rect.move_ip(-self.step_size, 0)
        elif keys[pygame.K_RIGHT]:
            # print("Right")
            self.direction = True
            # move the rect_player to the left by step_size
            overlap = False
            for platform in platform_list:
                if self.rect.top > platform.top - 25 and self.rect.top < platform.top + 10 and self.rect.right + self.step_size < platform.right and self.rect.right + self.step_size > platform.left:
                    overlap = True
            if self.rect.right < (screen_length) and not overlap:
                self.rect.move_ip(self.step_size, 0)
        
        return (running, click_up, click_space)

    def states(self, screen_length, platform_list, events, keys):

        (running, click_up, click_space) = self.input(events, keys, screen_length, platform_list)

        index = self.rect.collidelist(platform_list)

        if self.immunity_counter > 0:
            self.immunity_counter += 1
        if self.immunity_counter > 61:
            self.immunity_counter = 0

        if click_space:
            self.attack_state = 1
            self.attack_count = 0

        if self.state == 0:
            self.falling_counter += 1
            if self.falling_counter > 10:
                self.jump_number = max(1, self.jump_number)
            if click_up and self.jump_number < 2:
                self.jump_number += 1
                self.jump_count = 0
                self.state = 2
            if index != -1 and self.falling_counter > 4:
                self.state = 1
            else:
                dy = self.acceleration * self.falling_counter ** 2
                if dy > 5:
                    dy = 5
                self.rect.move_ip(0, dy)

        if self.state == 1:
            self.jump_number = 0
            if index == -1:
                self.falling_counter = 0
                self.state = 0
            if click_up:
                self.jump_number += 1
                self.jump_count = 0
                self.state = 2

        if self.state == 2:
            overlap = False
            for platform in platform_list:
                if self.rect.top - self.jump_size > platform.top - 25 and self.rect.top - self.jump_size < platform.top + 10 and self.rect.left < platform.right and self.rect.right > platform.left:
                    overlap = True
            if self.rect.top > self.jump_size and not overlap:
                self.rect.move_ip(0, -self.jump_size)
            self.jump_count += 1
            if self.jump_count == 10:
                self.falling_counter = 0
                self.state = 0
        return running
    
    def attack(self, screen, enemy_list, enemy_rect_list):
        if self.attack_state == 7:
            self.attack_state = 0
            self.attacked = False
            return
        if self.attack_state >= 1:
            pixel_distance = 0
            if self.attack_state < 4:
                pixel_distance = 2 * (self.attack_state)
            else:
                pixel_distance = 6 - 2  * ((self.attack_state-1)%3)
            if self.direction:
                melee_rect = pygame.Rect(self.rect.right + 3 + pixel_distance, (self.rect.top + self.rect.bottom)/2 - 10, 20, 20)
                index = melee_rect.collidelist(enemy_rect_list)
                if index != -1 and not self.attacked:
                    enemy_list[index].decrement_health()
                    self.attacked = True
                screen.blit(self.melee_imgs[0], melee_rect)
            else:
                melee_rect = pygame.Rect(self.rect.left - 23 - pixel_distance, (self.rect.top + self.rect.bottom)/2 - 10, 20, 20)
                index = melee_rect.collidelist(enemy_rect_list)
                if index != -1 and not self.attacked:
                    enemy_list[index].decrement_health()
                    self.attacked = True
                screen.blit(self.melee_imgs[1], melee_rect)
            self.attack_state += 1
    
    def get_x(self):
        return self.rect.left

    def get_rect(self):
        return self.rect

    def decrement_health(self):
        if self.immunity_counter == 0:
            self.health -= 10
            self.immunity_counter = 1
        print(self.health)

    def respawn(self):
        self.health = 100
        self.rect.x = 10
        self.rect.y = 523