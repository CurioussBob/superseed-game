
import pygame
from minigames.factory_manager import FactoryManagerGame

class FactoryLevel:
    def __init__(self):
        self.manager_game = FactoryManagerGame()
        self.active = False
        self.finished = False

    def enter(self):
        self.active = True
        self.manager_game = FactoryManagerGame()

    def handle_event(self, event):
        if not self.active or self.finished:
            return
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_KP1]:
                self.manager_game.answer(0)
            elif event.key in [pygame.K_2, pygame.K_KP2]:
                self.manager_game.answer(1)
            elif event.key in [pygame.K_3, pygame.K_KP3]:
                self.manager_game.answer(2)
            if self.manager_game.finished:
                self.finished = True

    def draw(self, screen):
        if self.active:
            self.manager_game.render(screen)
