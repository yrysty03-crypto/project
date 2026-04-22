import pygame
import random
import sys
import time

pygame.init()

# -------- SCREEN --------
WIDTH, HEIGHT = 600, 600
CELL = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# -------- COLORS --------
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 150, 255)
WHITE = (255, 255, 255)

font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 48)

clock = pygame.time.Clock()

# -------- GAME STATES --------
MENU, PLAYING, GAME_OVER = 0, 1, 2
state = MENU

# -------- FUNCTIONS --------
def generate_food():
    """
    Create food with:
    - random position
    - random weight (score)
    - timer (disappears after time)
    """
    while True:
        x = random.randrange(0, WIDTH, CELL)
        y = random.randrange(0, HEIGHT, CELL)
        if (x, y) not in snake:
            value = random.choice([1, 2, 5])

            # Color based on value
            if value == 1:
                color = RED
            elif value == 2:
                color = BLUE
            else:
                color = YELLOW

            return {
                "pos": (x, y),
                "value": value,
                "color": color,
                "spawn_time": time.time(),  # for timer
                "lifetime": 5               # seconds before disappearing
            }

def reset_game():
    """Reset game variables"""
    global snake, direction, food, score

    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (20, 0)

    food = generate_food()
    score = 0

# Initialize
reset_game()

# -------- MAIN LOOP --------
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            # MENU
            if state == MENU and event.key == pygame.K_SPACE:
                reset_game()
                state = PLAYING

            # GAME OVER
            elif state == GAME_OVER:
                if event.key == pygame.K_r:
                    reset_game()
                    state = PLAYING
                if event.key == pygame.K_ESCAPE:
                    running = False

            # PLAYING
            elif state == PLAYING:
                if event.key == pygame.K_UP and direction != (0, 20):
                    direction = (0, -20)
                if event.key == pygame.K_DOWN and direction != (0, -20):
                    direction = (0, 20)
                if event.key == pygame.K_LEFT and direction != (20, 0):
                    direction = (-20, 0)
                if event.key == pygame.K_RIGHT and direction != (-20, 0):
                    direction = (20, 0)

    # -------- MENU --------
    if state == MENU:
        screen.blit(big_font.render("SNAKE GAME", True, WHITE), (150, 250))
        screen.blit(font.render("Press SPACE to start", True, WHITE), (180, 320))

    # -------- GAME --------
    elif state == PLAYING:

        # Move snake
        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Wall collision
        if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
            state = GAME_OVER

        # Self collision
        elif head in snake:
            state = GAME_OVER
        else:
            snake.insert(0, head)

            # -------- FOOD TIMER --------
            # If food exists too long → replace it
            if time.time() - food["spawn_time"] > food["lifetime"]:
                food = generate_food()

            # -------- EAT FOOD --------
            if head == food["pos"]:
                score += food["value"]  # weighted score
                food = generate_food()
            else:
                snake.pop()

        # Draw snake
        for s in snake:
            pygame.draw.rect(screen, GREEN, (*s, CELL, CELL))

        # Draw food
        pygame.draw.rect(screen, food["color"], (*food["pos"], CELL, CELL))

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    # -------- GAME OVER --------
    elif state == GAME_OVER:
        screen.blit(big_font.render("GAME OVER", True, RED), (150, 250))
        screen.blit(font.render(f"Score: {score}", True, WHITE), (230, 320))
        screen.blit(font.render("Press R to restart", True, WHITE), (180, 360))

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit()