import pygame
from datetime import datetime, timedelta
import math

class MickeyClock:
    def __init__(self, screen, center):
        self.screen = screen
        self.center = center
        self.font = pygame.font.SysFont("Arial", 20, bold=True)

    def draw_numbers(self):
        radius = 140
        for i in range(1, 13):
            angle = math.radians(i * 30 - 90)

            x = self.center[0] + radius * math.cos(angle)
            y = self.center[1] + radius * math.sin(angle)

            text = self.font.render(str(i), True, (0, 0, 0))
            rect = text.get_rect(center=(x, y))
            self.screen.blit(text, rect)

    def draw_hand(self, angle, length, thickness, color):
        radians = math.radians(angle - 90)

        x = self.center[0] + length * math.cos(radians)
        y = self.center[1] + length * math.sin(radians)

        pygame.draw.line(self.screen, color, self.center, (x, y), thickness)

    def get_time(self):
        # 🇰🇿 Kazakhstan time (UTC+5)
        now = datetime.utcnow() + timedelta(hours=5)

        seconds = now.second + now.microsecond / 1_000_000
        minutes = now.minute + seconds / 60
        hours = (now.hour % 12) + minutes / 60

        return hours, minutes, seconds

    def update(self):
        self.screen.fill((255, 255, 255))

        # 🐭 Mickey head
        head_radius = 180
        ear_radius = 70

        pygame.draw.circle(self.screen, (0, 0, 0), self.center, head_radius)

        left_ear = (self.center[0] - 120, self.center[1] - 130)
        right_ear = (self.center[0] + 120, self.center[1] - 130)

        pygame.draw.circle(self.screen, (0, 0, 0), left_ear, ear_radius)
        pygame.draw.circle(self.screen, (0, 0, 0), right_ear, ear_radius)

        pygame.draw.circle(self.screen, (255, 255, 255), self.center, 160)

        # Numbers
        self.draw_numbers()

        # Time
        hours, minutes, seconds = self.get_time()

        hour_angle = hours * 30
        minute_angle = minutes * 6
        second_angle = seconds * 6

        # Draw arrows
        self.draw_hand(hour_angle, 80, 6, (0, 0, 0))
        self.draw_hand(minute_angle, 110, 4, (0, 0, 0))
        self.draw_hand(second_angle, 130, 2, (255, 0, 0))

        # Center dot
        pygame.draw.circle(self.screen, (0, 0, 0), self.center, 6)