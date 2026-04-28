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

        self.speed = 5
        self.distance = 0

        # 🏁 UPDATED FINISH DISTANCE
        self.finish_distance = 2000
        self.finished = False

        self.traffic = []
        self.bg_y = 0

    # -------- UPDATE --------
    def update(self):
        # increase distance
        self.distance += 0.1 * self.speed

        # check finish
        if self.distance >= self.finish_distance:
            self.finished = True

        # background scrolling
        self.bg_y += self.speed
        if self.bg_y >= self.HEIGHT:
            self.bg_y = 0

        # spawn enemies
        if random.randint(1, 60) == 1:
            self.traffic.append(
                pygame.Rect(random.randint(0, self.WIDTH - 50), -100, 50, 80)
            )

        # move enemies
        for car in self.traffic[:]:
            car.y += self.speed
            if car.top > self.HEIGHT:
                self.traffic.remove(car)

    # -------- COLLISION --------
    def check_collision(self):
        for car in self.traffic:
            if self.player.colliderect(car):
                if self.sound_enabled:
                    self.crash.play()
                return True
        return False

    # -------- DRAW --------
    def draw(self, screen):
        # road
        screen.blit(self.road_img, (0, self.bg_y))
        screen.blit(self.road_img, (0, self.bg_y - self.HEIGHT))

        # 🏁 DRAW FINISH LINE
        if self.finish_distance - self.distance < 200:
            pygame.draw.rect(screen, (255, 255, 255), (0, 100, self.WIDTH, 12))
            pygame.draw.rect(screen, (0, 0, 0), (0, 100, self.WIDTH, 6))

        # player
        screen.blit(self.player_img, self.player.topleft)

        # enemies
        for car in self.traffic:
            screen.blit(self.enemy_img, car.topleft)