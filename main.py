
import pygame
from levels.level_manager import LevelManager

class Player:
    def __init__(self):
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(topleft=(100, 100))
        self.speed = 5

    def handle_movement(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Superseed Demo: Bank & Factory Mini-Games")
clock = pygame.time.Clock()

player = Player()
level_manager = LevelManager()

running = True
while running:
    dt = clock.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if level_manager.current_scene == 'city':
        player.handle_movement(keys)

    level_manager.update(player, events)
    level_manager.draw(screen, player)

    pygame.display.flip()

pygame.quit()
