import pygame
import random


class Alien(pygame.sprite.Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.tipe = type
        path = f'images/enemy_{type}.png'
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction):
        self.rect.x += direction


class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_wight, offset):
        super().__init__()
        self.screen_wight = screen_wight
        self.offset = offset
        self.image = pygame.image.load('images/mystery.png')
        self.mystery_sound = pygame.mixer.Sound('sounds/mysteryentered.wav')

        x = random.choice([self.offset / 2, self.screen_wight + self.offset - self.image.get_width()])
        if x == self.offset / 2:
            self.speed = 3
            self.mystery_sound.play()
        else:
            self.speed = -3

        self.rect = self.image.get_rect(topleft=(x, 90))

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_wight + self.offset / 2:
            self.kill()
        elif self.rect.left < self.offset / 2:
            self.kill()
