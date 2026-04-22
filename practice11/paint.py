import pygame
import sys
import math

pygame.init()

# -------- SCREEN --------
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint with UI")

# -------- COLORS --------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

current_color = BLACK

# -------- BUTTON CLASS --------
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        font = pygame.font.SysFont("Arial", 18)
        txt = font.render(self.text, True, BLACK)
        screen.blit(txt, (self.rect.x + 5, self.rect.y + 5))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# -------- BUTTONS --------
buttons = {
    "draw": Button(10, 10, 80, 30, "Draw"),
    "square": Button(100, 10, 80, 30, "Square"),
    "rtriangle": Button(190, 10, 110, 30, "R-Triangle"),
    "etriangle": Button(310, 10, 130, 30, "E-Triangle"),
    "rhombus": Button(450, 10, 100, 30, "Rhombus"),
    "erase": Button(560, 10, 80, 30, "Eraser"),
}

# Color buttons
color_buttons = [
    (BLACK, pygame.Rect(700, 10, 30, 30)),
    (RED, pygame.Rect(740, 10, 30, 30)),
    (GREEN, pygame.Rect(780, 10, 30, 30)),
    (BLUE, pygame.Rect(820, 10, 30, 30)),
]

# -------- VARIABLES --------
mode = "draw"
drawing = False
start_pos = None

# Fill canvas
screen.fill(WHITE)

# -------- MAIN LOOP --------
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # -------- MOUSE DOWN --------
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            # Check shape buttons
            for key, btn in buttons.items():
                if btn.is_clicked(pos):
                    mode = key

            # Check color buttons
            for col, rect in color_buttons:
                if rect.collidepoint(pos):
                    current_color = col

            # Start drawing
            drawing = True
            start_pos = pos

        # -------- MOUSE UP --------
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            end_pos = event.pos

            x1, y1 = start_pos
            x2, y2 = end_pos

            # -------- SQUARE --------
            if mode == "square":
                size = min(abs(x2 - x1), abs(y2 - y1))
                pygame.draw.rect(screen, current_color, (x1, y1, size, size), 2)

            # -------- RIGHT TRIANGLE --------
            elif mode == "rtriangle":
                points = [(x1, y1), (x2, y1), (x1, y2)]
                pygame.draw.polygon(screen, current_color, points, 2)

            # -------- EQUILATERAL TRIANGLE --------
            elif mode == "etriangle":
                size = abs(x2 - x1)
                height = int(size * math.sqrt(3) / 2)

                points = [
                    (x1, y1),
                    (x1 + size, y1),
                    (x1 + size // 2, y1 - height)
                ]
                pygame.draw.polygon(screen, current_color, points, 2)

            # -------- RHOMBUS --------
            elif mode == "rhombus":
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2

                points = [
                    (cx, y1),
                    (x2, cy),
                    (cx, y2),
                    (x1, cy)
                ]
                pygame.draw.polygon(screen, current_color, points, 2)

        # -------- DRAW / ERASE --------
        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == "draw":
                pygame.draw.circle(screen, current_color, event.pos, 3)
            elif mode == "erase":
                pygame.draw.circle(screen, WHITE, event.pos, 10)

    # -------- DRAW UI --------
    # Draw buttons
    for btn in buttons.values():
        btn.draw()

    # Draw color palette
    for col, rect in color_buttons:
        pygame.draw.rect(screen, col, rect)
        pygame.draw.rect(screen, BLACK, rect, 2)

    pygame.display.flip()