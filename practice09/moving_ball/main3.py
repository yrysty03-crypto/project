import pygame
from ball import Ball

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball Game")

# Colors
WHITE = (255, 255, 255)

# Create ball
ball = Ball(x=WIDTH // 2, y=HEIGHT // 2, radius=25)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball.move(0, -20, WIDTH, HEIGHT)
            elif event.key == pygame.K_DOWN:
                ball.move(0, 20, WIDTH, HEIGHT)
            elif event.key == pygame.K_LEFT:
                ball.move(-20, 0, WIDTH, HEIGHT)
            elif event.key == pygame.K_RIGHT:
                ball.move(20, 0, WIDTH, HEIGHT)

    # Draw ball
    ball.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()