import pygame
from constants import *
from Creature import *
from Food import *


class Evolution:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Evolution")
        self.clock = pygame.time.Clock()
        self.last_update = 0

        self.all_sprites = pygame.sprite.Group()
        self.all_creatures = []
        self.first_population()
        self.all_food = []
        self.generate_food()

        self.running = True
        self.main_loop()

    def main_loop(self):
        while self.running:
            self.clock.tick(FPS)
            now = pygame.time.get_ticks()
            if now - self.last_update > CYCLE_TIME:
                self.last_update = now
                self.new_cycle()
            self.collision_check()
            for creature in self.all_creatures:
                creature.update(self.all_food)
            self.screen.fill(WHITE)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def first_population(self):
        for i in range(POPULATION):
            new_creature = Creature()
            self.all_sprites.add(new_creature)
            self.all_creatures.append(new_creature)

    def generate_food(self):
        for i in range(START_FOOD):
            new_food = Food()
            self.all_sprites.add(new_food)
            self.all_food.append(new_food)

    def new_cycle(self):
        for creature in self.all_creatures:
            if creature.has_eaten == 0:
                if creature.goal:
                    creature.goal.image.fill(BLACK)
                creature.kill()
                self.all_creatures.remove(creature)
                self.all_sprites.remove(creature)
            elif creature.has_eaten == 1:
                creature.has_eaten = 0
            else:
                new_creature = Creature(creature)
                self.all_sprites.add(new_creature)
                self.all_creatures.append(new_creature)
                creature.has_eaten = 0
        self.generate_food()

    def collision_check(self):
        for creature in self.all_creatures:
            for food in self.all_food:
                if self.collision(creature, food):
                    creature.has_eaten += 1
                    food.kill()
                    self.all_sprites.remove(food)
                    self.all_food.remove(food)

    @staticmethod
    def collision(obj1, obj2):
        return obj1.rect.right > obj2.rect.left and obj1.rect.left < obj2.rect.right and \
               obj1.rect.bottom > obj2.rect.top and obj1.rect.top < obj2.rect.bottom


if __name__ == '__main__':
    evo_instance = Evolution()
