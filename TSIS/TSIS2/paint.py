import pygame
import sys
import math
from datetime import datetime
from tools import flood_fill

pygame.init()

# -------- SCREEN --------
WIDTH, HEIGHT = 1200, 700
TOOLBAR_HEIGHT = 80

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Paint App")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

screen.fill(WHITE)

# -------- SETTINGS --------
color = BLACK
brush_size = 5
mode = "pencil"

drawing = False
start_pos = None

# -------- TEXT TOOL --------
text_input = ""
text_pos = None
typing = False

font = pygame.font.SysFont("Arial", 18)
big_font = pygame.font.SysFont("Arial", 24)

clock = pygame.time.Clock()

# -------- BUTTON CLASS --------
class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, GRAY, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        txt = font.render(self.text, True, BLACK)
        screen.blit(txt, (self.rect.x + 5, self.rect.y + 5))

    def clicked(self, pos):
        return self.rect.collidepoint(pos)

# -------- TOOLBAR BUTTONS --------
buttons = {
    "pencil": Button(10, 10, 80, 30, "Pencil"),
    "line": Button(100, 10, 80, 30, "Line"),
    "square": Button(190, 10, 80, 30, "Square"),
    "rtriangle": Button(280, 10, 100, 30, "R-Tri"),
    "etriangle": Button(390, 10, 110, 30, "E-Tri"),
    "rhombus": Button(510, 10, 100, 30, "Rhombus"),
    "fill": Button(620, 10, 80, 30, "Fill"),
    "text": Button(710, 10, 80, 30, "Text"),
    "clear": Button(800, 10, 80, 30, "Clear"),
}

# -------- EXTENDED COLORS --------
colors = [
    # Row 1
    (BLACK, pygame.Rect(900, 10, 30, 30)),
    ((255, 0, 0), pygame.Rect(940, 10, 30, 30)),
    ((0, 255, 0), pygame.Rect(980, 10, 30, 30)),
    ((0, 0, 255), pygame.Rect(1020, 10, 30, 30)),
    ((255, 255, 0), pygame.Rect(1060, 10, 30, 30)),
    ((255, 165, 0), pygame.Rect(1100, 10, 30, 30)),
    ((128, 0, 128), pygame.Rect(1140, 10, 30, 30)),

    # Row 2
    ((0, 255, 255), pygame.Rect(900, 45, 30, 30)),
    ((255, 192, 203), pygame.Rect(940, 45, 30, 30)),
    ((165, 42, 42), pygame.Rect(980, 45, 30, 30)),
    ((128, 128, 128), pygame.Rect(1020, 45, 30, 30)),
    ((0, 100, 0), pygame.Rect(1060, 45, 30, 30)),
    ((0, 0, 139), pygame.Rect(1100, 45, 30, 30)),
    ((255, 255, 255), pygame.Rect(1140, 45, 30, 30)),
]

# -------- MAIN LOOP --------
while True:

    temp_surface = screen.copy()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # -------- KEYBOARD --------
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_1:
                brush_size = 2
            elif event.key == pygame.K_2:
                brush_size = 5
            elif event.key == pygame.K_3:
                brush_size = 10

            elif event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                filename = datetime.now().strftime("drawing_%Y%m%d_%H%M%S.png")
                pygame.image.save(screen, filename)

            # TEXT INPUT
            if typing:
                if event.key == pygame.K_RETURN:
                    screen.blit(big_font.render(text_input, True, color), text_pos)
                    typing = False
                elif event.key == pygame.K_ESCAPE:
                    typing = False
                    text_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

        # -------- MOUSE --------
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos

            # Buttons
            for key, btn in buttons.items():
                if btn.clicked(pos):
                    if key == "clear":
                        pygame.draw.rect(screen, WHITE, (0, TOOLBAR_HEIGHT, WIDTH, HEIGHT))
                    else:
                        mode = key
                        typing = False

            # Colors
            for col, rect in colors:
                if rect.collidepoint(pos):
                    color = col

            # Drawing area
            if pos[1] > TOOLBAR_HEIGHT:
                drawing = True
                start_pos = pos

                if mode == "fill":
                    flood_fill(screen, pos[0], pos[1], color, WIDTH, HEIGHT)

                elif mode == "text":
                    text_pos = pos
                    text_input = ""
                    typing = True

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False
            x1, y1 = start_pos
            x2, y2 = event.pos

            if mode == "line":
                pygame.draw.line(screen, color, start_pos, event.pos, brush_size)

            elif mode == "square":
                size = min(abs(x2-x1), abs(y2-y1))
                pygame.draw.rect(screen, color, (x1, y1, size, size), 2)

            elif mode == "rtriangle":
                pygame.draw.polygon(screen, color, [(x1,y1),(x2,y1),(x1,y2)], 2)

            elif mode == "etriangle":
                size = abs(x2-x1)
                h = int(size * math.sqrt(3)/2)
                pygame.draw.polygon(screen, color,
                    [(x1,y1),(x1+size,y1),(x1+size//2,y1-h)], 2)

            elif mode == "rhombus":
                cx = (x1+x2)//2
                cy = (y1+y2)//2
                pygame.draw.polygon(screen, color,
                    [(cx,y1),(x2,cy),(cx,y2),(x1,cy)], 2)

        if event.type == pygame.MOUSEMOTION:

            if drawing and mode == "pencil":
                pygame.draw.line(screen, color, start_pos, event.pos, brush_size)
                start_pos = event.pos

            if drawing and mode == "line":
                screen.blit(temp_surface, (0,0))
                pygame.draw.line(screen, color, start_pos, event.pos, brush_size)

    # -------- TEXT PREVIEW --------
    if typing and text_pos:
        temp = screen.copy()
        temp.blit(big_font.render(text_input, True, color), text_pos)
        screen.blit(temp, (0,0))

    # -------- UI --------
    pygame.draw.rect(screen, WHITE, (0, 0, WIDTH, TOOLBAR_HEIGHT))

    for btn in buttons.values():
        btn.draw()

    for col, rect in colors:
        pygame.draw.rect(screen, col, rect)
        border = (255, 0, 0) if col == color else BLACK
        pygame.draw.rect(screen, border, rect, 2)

    pygame.display.flip()
    clock.tick(60)