import pygame

RED = (255, 0, 0)

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def move(self, dx, dy, screen_width, screen_height):
        new_x = self.x + dx
        new_y = self.y + dy

        # Boundary check
        if (self.radius <= new_x <= screen_width - self.radius and
            self.radius <= new_y <= screen_height - self.radius):
            self.x = new_x
            self.y = new_y
        # Else: ignore movement (requirement #5)

    def draw(self, screen):
        pygame.draw.circle(screen, RED, (self.x, self.y), self.radius)