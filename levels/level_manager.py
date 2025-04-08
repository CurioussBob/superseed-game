
import pygame
from levels.bank import BankLevel
from levels.factory import FactoryLevel

class LevelManager:
    def __init__(self):
        self.current_scene = 'city'
        self.bank_level = BankLevel()
        self.factory_level = FactoryLevel()
        self.font = pygame.font.Font(None, 28)

    def update(self, player, events):
        if self.current_scene == 'bank':
            for event in events:
                self.bank_level.handle_event(event)
            if self.bank_level.finished:
                self.current_scene = 'city'
        elif self.current_scene == 'factory':
            for event in events:
                self.factory_level.handle_event(event)
            if self.factory_level.finished:
                self.current_scene = 'city'
        else:
            # Check for entering bank
            if player.rect.colliderect(pygame.Rect(500, 200, 100, 100)):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.enter_bank()

            # Check for entering factory
            if player.rect.colliderect(pygame.Rect(200, 400, 100, 100)):
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.enter_factory()

    def enter_bank(self):
        self.current_scene = 'bank'
        self.bank_level.enter()

    def enter_factory(self):
        self.current_scene = 'factory'
        self.factory_level.enter()

    def draw(self, screen, player):
        if self.current_scene == 'bank':
            self.bank_level.draw(screen)
        elif self.current_scene == 'factory':
            self.factory_level.draw(screen)
        else:
            screen.fill((93, 173, 236))  # City background
            pygame.draw.rect(screen, (0, 128, 255), (500, 200, 100, 100))  # Bank
            pygame.draw.rect(screen, (0, 200, 200), (200, 400, 100, 100))  # Factory
            screen.blit(player.image, player.rect)
            bank_txt = self.font.render("ESPACE: Entrer dans la Banque", True, (255, 255, 255))
            factory_txt = self.font.render("ESPACE: Entrer dans l'Usine", True, (255, 255, 255))
            screen.blit(bank_txt, (20, 20))
            screen.blit(factory_txt, (20, 50))
