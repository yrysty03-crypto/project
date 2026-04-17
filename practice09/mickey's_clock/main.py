import pygame
import sys
from clock import MickeyClock

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock (Kazakhstan Time)")

clock = pygame.time.Clock()
CENTER = (WIDTH // 2, HEIGHT // 2)

mickey = MickeyClock(screen, CENTER)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mickey.update()

    pygame.display.flip()
    clock.tick(60)