import random
import pygame
from os import path
import numpy as np
import math
from constants import *
from CreatureAI import *
from SimpleCreatureAI import *


class Creature(pygame.sprite.Sprite):
    def __init__(self, parent=None):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(path.dirname(__file__), 'sprites/creature.bmp')).convert()
        self.rect = self.image.get_rect()
        self.goal = None
        self.has_eaten = 0
        if parent is None:
            self.rect.x = random.randint(0, WIDTH - 1)
            self.rect.y = random.randint(0, HEIGHT - 1)
            self.color = random.choice([RED, GREEN, BLUE, BLACK])
            self.image.fill(self.color)
            self.speed = random.randint(0, 10)
            self.size = random.random() + 0.5
            pygame.transform.scale(self.image, (int(self.size), int(self.size)))
            self.AI = SimpleCreatureAI()
        else:
            self.rect.x = parent.rect.x + random.randint(-20, 20)
            self.rect.y = parent.rect.y + random.randint(-20, 20)
            old_color = parent.color
            new_color = (Creature.mutate_color_channel(old_color[0]),
                         Creature.mutate_color_channel(old_color[1]),
                         Creature.mutate_color_channel(old_color[2]))
            self.color = new_color
            self.image.fill(new_color)
            self.size = parent.size + random.random() / 2
            pygame.transform.scale(self.image, (int(self.size), int(self.size)))
            self.speed = parent.speed + random.randint(-1, 1)
            self.AI = SimpleCreatureAI(parent.AI)

    @staticmethod
    def mutate_color_channel(old):
        return min(255, max(0, old + random.randint(-50, 50)))

    def update(self, all_food):
        x = self.rect.x
        y = self.rect.y
        food_index = np.argmin([math.sqrt((x - food.rect.x)**2 + (y - food.rect.y)**2) for food in all_food])
        if self.goal:
            self.goal.image.fill(BLACK)
        all_food[food_index].image.fill(RED)
        self.goal = all_food[food_index]
        x_move, y_move = self.AI.predict(np.array(all_food[food_index].rect.x - x),
                                         np.array(all_food[food_index].rect.y - y))
        self.rect.x += x_move * self.speed
        self.rect.y += y_move * self.speed
        if self.rect.x > WIDTH:
            self.rect.x = WIDTH - 10
        if self.rect.y > HEIGHT:
            self.rect.y = HEIGHT - 10
        if self.rect.x < 0:
            self.rect.x = 10
        if self.rect.y < 0:
            self.rect.y = 10
