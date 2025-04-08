
import pygame
from minigames.bank_quiz import BankQuizGame

class BankLevel:
    def __init__(self):
        self.quiz = BankQuizGame()
        self.font = pygame.font.Font(None, 32)
        self.active = False
        self.finished = False

    def enter(self):
        self.active = True
        self.quiz = BankQuizGame()

    def handle_event(self, event):
        if not self.active or self.finished:
            return
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_1, pygame.K_KP1]:
                self.quiz.answer(0)
            elif event.key in [pygame.K_2, pygame.K_KP2]:
                self.quiz.answer(1)
            elif event.key in [pygame.K_3, pygame.K_KP3]:
                self.quiz.answer(2)
            if self.quiz.finished:
                self.finished = True

    def draw(self, screen):
        if self.active:
            self.quiz.render(screen, self.font)
