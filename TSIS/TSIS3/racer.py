import pygame
import random

class Game:
    def __init__(self, width, height):
        self.WIDTH = width
        self.HEIGHT = height

        # -------- IMAGES --------
        self.player_img = pygame.transform.scale(
            pygame.image.load("assets/player_red.png").convert_alpha(), (50, 80)
        )
        self.enemy_img = pygame.transform.scale(
            pygame.image.load("assets/enemy.png").convert_alpha(), (50, 80)
        )
        self.road_img = pygame.transform.scale(
            pygame.image.load("assets/road.png").convert(), (width, height)
        )

        # -------- SOUNDS --------
        self.engine = pygame.mixer.Sound("assets/engine.wav")
        self.crash = pygame.mixer.Sound("assets/crash.wav")

        self.sound_enabled = True

        self.reset()

    # -------- SETTINGS --------
    def apply_settings(self, settings):
        self.sound_enabled = settings.get("sound", True)
        if self.sound_enabled:
            self.engine.play(-1)
        else:
            self.engine.stop()

    def stop_engine(self):
        self.engine.stop()

    # -------- RESET --------
    def reset(self):
        self.player = pygame.Rect(self.WIDTH // 2 - 25, self.HEIGHT - 120, 50, 80)

        self.base_speed = 5
        self.distance = 0
        self.finish_distance = 2000
        self.finished = False

        self.traffic = []
        self.powerups = []

        # power-up states
        self.shield = False
        self.speed_boost = False
        self.score_multiplier = False

        # timers (frames)
        self.speed_timer = 0
        self.score_timer = 0

        self.bg_y = 0

    # -------- UPDATE --------
    def update(self):
        # ---- timers ----
        if self.speed_timer > 0:
            self.speed_timer -= 1
        else:
            self.speed_boost = False

        if self.score_timer > 0:
            self.score_timer -= 1
        else:
            self.score_multiplier = False

        # ---- effective speed ----
        current_speed = self.base_speed + (3 if self.speed_boost else 0)
        multiplier = 2 if self.score_multiplier else 1

        # ---- distance ----
        self.distance += 0.1 * current_speed * multiplier

        # finish check
        if self.distance >= self.finish_distance:
            self.finished = True

        # ---- background scroll ----
        self.bg_y += current_speed
        if self.bg_y >= self.HEIGHT:
            self.bg_y = 0

        # ---- spawn enemies ----
        if random.randint(1, 60) == 1:
            self.traffic.append(
                pygame.Rect(random.randint(0, self.WIDTH - 50), -100, 50, 80)
            )

        # ---- move enemies ----
        for car in self.traffic[:]:
            car.y += current_speed
            if car.top > self.HEIGHT:
                self.traffic.remove(car)

        # ---- spawn power-ups ----
        if random.randint(1, 200) == 1:
            p_type = random.choice(["shield", "speed", "score"])
            self.powerups.append({
                "rect": pygame.Rect(random.randint(0, self.WIDTH - 30), -50, 30, 30),
                "type": p_type
            })

        # ---- move power-ups ----
        for p in self.powerups[:]:
            p["rect"].y += current_speed
            if p["rect"].top > self.HEIGHT:
                self.powerups.remove(p)

        # ---- pickup power-ups ----
        for p in self.powerups[:]:
            if self.player.colliderect(p["rect"]):
                self.activate_powerup(p["type"])
                self.powerups.remove(p)

    # -------- POWER-UP EFFECTS --------
    def activate_powerup(self, p_type):
        if p_type == "shield":
            self.shield = True

        elif p_type == "speed":
            self.speed_boost = True
            self.speed_timer = 180  # ~3 seconds at 60 FPS

        elif p_type == "score":
            self.score_multiplier = True
            self.score_timer = 180

    # -------- COLLISION --------
    def check_collision(self):
        for car in self.traffic[:]:
            if self.player.colliderect(car):

                # shield absorbs one hit
                if self.shield:
                    self.shield = False
                    self.traffic.remove(car)
                    return False

                if self.sound_enabled:
                    self.crash.play()
                return True
        return False

    # -------- DRAW --------
    def draw(self, screen):
        # road
        screen.blit(self.road_img, (0, self.bg_y))
        screen.blit(self.road_img, (0, self.bg_y - self.HEIGHT))

        # finish line
        if self.finish_distance - self.distance < 200:
            pygame.draw.rect(screen, (255, 255, 255), (0, 100, self.WIDTH, 12))
            pygame.draw.rect(screen, (0, 0, 0), (0, 100, self.WIDTH, 6))

        # player
        screen.blit(self.player_img, self.player.topleft)

        # enemies
        for car in self.traffic:
            screen.blit(self.enemy_img, car.topleft)

        # ---- draw power-ups ----
        for p in self.powerups:
            if p["type"] == "shield":
                color = (0, 200, 255)   # blue
            elif p["type"] == "speed":
                color = (255, 255, 0)   # yellow
            else:
                color = (0, 255, 0)     # green
            pygame.draw.rect(screen, color, p["rect"])

        # ---- UI indicators ----
        font = pygame.font.SysFont("Arial", 20)

        if self.shield:
            screen.blit(font.render("Shield", True, (0, 200, 255)), (10, 40))

        if self.speed_boost:
            screen.blit(font.render("Speed Boost", True, (255, 255, 0)), (10, 65))

        if self.score_multiplier:
            screen.blit(font.render("x2 Score", True, (0, 255, 0)), (10, 90))