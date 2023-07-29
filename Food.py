import random
import pygame
from constants import *
from os import path


class Food(pygame.sprite.Sprite):
    def __init__(self, parent=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(path.dirname(__file__), 'sprites/food.bmp')).convert()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 1)
        self.rect.y = random.randint(0, HEIGHT - 1)
