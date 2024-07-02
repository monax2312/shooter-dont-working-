import pygame
import random
from time import time
import os, sys

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    elif hasattr(sys, "_MEIPASS2"):
        return os.path.join(sys._MEIPASS2, relative_path)
    else:
        return os.path.join(os.path.abspath("."), relative_path)

image_folder = resource_path(".")
pygame.init()

counter = 0
kills = 0
lives = 3

cur_fire = 0
rel_time = False

shot = pygame.mixer.Sound(os.path.join(image_folder, 'fire.ogg'))

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, img, speed, x, y, w, h):
        super().__init__()
        self.speed = speed
        self.image = pygame.transform.scale(img, (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self, d):
        d.blit(self.image, self.rect)

class Bullet(GameSprite):
    def update(self, enemies):
        global kills
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                enemy.rect.y = int('-' + str(random.randint(20, 52)))
                enemy.rect.x = random.randint(100, 600)
                kills += 1

class Player(GameSprite):
    def __init__(self, img, speed, x, y, w, h):
        super().__init__(img, speed, x, y, w, h)
        self.cur_fire = 0
        self.rel_time = False

    def move(self, d, group):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= self.speed
        if key[pygame.K_d]:
            self.rect.x += self.speed
        if key[pygame.K_SPACE]:
            if self.cur_fire < 5 and not self.rel_time:
                self.cur_fire += 1
                self.fire(group)
                shot.play()
            if self.cur_fire >= 5 and not self.rel_time:
                global last_time
                last_time = time()
                self.rel_time = True
        self.reset(d)

    def fire(self, group):
        group.add(Bullet(pygame.image.load(os.path.join(image_folder, 'bullet.png')), 15, self.rect.x + 35, self.rect.y, 10, 50))

class Enemy(GameSprite):
    def update(self, d):
        global counter
        self.reset(d)
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = int('-' + str(random.randint(20, 52)))
            self.rect.x = random.randint(100, 600)
            counter += 1

class Asteroid(Enemy):
    def update(self, d, player):
        global lives
        self.reset(d)
        self.rect.y += self.speed
        if self.rect.colliderect(player.rect):
            lives -= 1
            self.rect.y = int('-' + str(random.randint(20, 52)))
            self.rect.x = random.randint(100, 600)