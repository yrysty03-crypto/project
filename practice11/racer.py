import pygame
import random
import sys

# -------- INIT --------
pygame.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

clock = pygame.time.Clock()
FPS = 60

# -------- COLORS --------
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GOLD = (255, 215, 0)
BLUE = (0, 150, 255)

font = pygame.font.SysFont("Arial", 24)

# -------- PLAYER --------
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 120, 50, 80)
player_speed = 6

# -------- ENEMY --------
enemy = pygame.Rect(random.randint(0, WIDTH - 50), -100, 50, 80)
enemy_speed = 5

# -------- COINS WITH WEIGHTS --------
# Each coin has (rect, value, color)
def create_coin():
    value = random.choice([1, 2, 5])  # weight/value
    x = random.randint(0, WIDTH - 30)

    # Different color based on value
    if value == 1:
        color = YELLOW
    elif value == 2:
        color = BLUE
    else:
        color = GOLD

    rect = pygame.Rect(x, -100, 30, 30)
    return {"rect": rect, "value": value, "color": color}

coin = create_coin()

# -------- GAME VARIABLES --------
score = 0
coins_collected = 0
LEVEL_UP_COINS = 5  # N coins to increase difficulty

# -------- MAIN LOOP --------
running = True
while running:
    screen.fill(GRAY)

    # -------- EVENTS --------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # -------- PLAYER MOVEMENT --------
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # -------- ENEMY MOVEMENT --------
    enemy.y += enemy_speed
    if enemy.top > HEIGHT:
        enemy.y = -100
        enemy.x = random.randint(0, WIDTH - 50)

    # -------- COIN MOVEMENT --------
    coin["rect"].y += 5
    if coin["rect"].top > HEIGHT:
        coin = create_coin()

    # -------- COLLISIONS --------
    # Player hits enemy → Game Over
    if player.colliderect(enemy):
        print("Game Over! Score:", score)
        pygame.quit()
        sys.exit()

    # Player collects coin
    if player.colliderect(coin["rect"]):
        score += coin["value"]            # add weighted value
        coins_collected += 1              # count coins
        coin = create_coin()

        # Increase difficulty every N coins
        if coins_collected % LEVEL_UP_COINS == 0:
            enemy_speed += 1
            print("Speed increased! Enemy speed:", enemy_speed)

    # -------- DRAW --------
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, YELLOW, enemy)
    pygame.draw.ellipse(screen, coin["color"], coin["rect"])

    # -------- UI --------
    score_text = font.render(f"Score: {score}", True, WHITE)
    coins_text = font.render(f"Coins: {coins_collected}", True, WHITE)
    speed_text = font.render(f"Speed: {enemy_speed}", True, WHITE)

    screen.blit(score_text, (WIDTH - 150, 20))
    screen.blit(coins_text, (WIDTH - 150, 50))
    screen.blit(speed_text, (WIDTH - 150, 80))

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()