import pygame, sys, json
from config import *
from game import Game
from db import *

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")

font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 48)
clock = pygame.time.Clock()

# -------- BUTTON --------
class Button:
    def __init__(self, text, x, y, w, h):
        self.text = text
        self.rect = pygame.Rect(x,y,w,h)

    def draw(self, screen):
        mouse = pygame.mouse.get_pos()
        color = (100,100,100)
        if self.rect.collidepoint(mouse):
            color = (150,150,150)

        pygame.draw.rect(screen, color, self.rect)
        pygame.draw.rect(screen, WHITE, self.rect,2)

        txt = font.render(self.text, True, WHITE)
        screen.blit(txt, (self.rect.x+20, self.rect.y+12))

    def clicked(self, e):
        return e.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(e.pos)

# -------- SETTINGS --------
with open("settings.json") as f:
    settings = json.load(f)

# -------- SOUNDS --------
eat_sound = pygame.mixer.Sound("assets/eat.wav")
gameover_sound = pygame.mixer.Sound("assets/gameover.wav")
pygame.mixer.music.load("assets/music.mp3")

game = Game(settings, {"eat":eat_sound,"gameover":gameover_sound})

# -------- BUTTONS --------
start_btn = Button("START",200,280,200,50)
leader_btn = Button("LEADERBOARD",200,350,200,50)
settings_btn = Button("SETTINGS",200,420,200,50)
quit_btn = Button("QUIT",200,490,200,50)

grid_btn = Button("TOGGLE GRID",180,0,240,50)
sound_btn = Button("TOGGLE SOUND",180,0,240,50)
back_btn = Button("BACK",200,0,200,50)

retry_btn = Button("RETRY",200,320,200,50)
menu_btn = Button("MENU",200,390,200,50)

color_buttons = [
    (pygame.Rect(0,0,40,40),(0,255,0)),
    (pygame.Rect(0,0,40,40),(255,0,0)),
    (pygame.Rect(0,0,40,40),(0,0,255)),
    (pygame.Rect(0,0,40,40),(255,255,0)),
]

# -------- STATES --------
MENU, PLAY, OVER, SETTINGS, LEADER = 0,1,2,3,4
state = MENU

username=""
player_id=None
music=False

running=True
while running:
    screen.fill(BLACK)

    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            running=False

        # -------- KEYBOARD --------
        if e.type==pygame.KEYDOWN:
            if state==MENU:
                if e.key==pygame.K_BACKSPACE:
                    username=username[:-1]
                elif e.key==pygame.K_RETURN and username:
                    player_id=create_player(username)
                    game.reset()
                    state=PLAY
                else:
                    if e.unicode.isascii() and e.unicode.isprintable():
                        username+=e.unicode

            elif state==PLAY:
                if e.key == pygame.K_UP: game.direction=(0,-CELL)
                elif e.key == pygame.K_DOWN: game.direction=(0,CELL)
                elif e.key == pygame.K_LEFT: game.direction=(-CELL,0)
                elif e.key == pygame.K_RIGHT: game.direction=(CELL,0)

        # -------- MENU --------
        if state==MENU:
            if start_btn.clicked(e) and username:
                player_id=create_player(username)
                game.reset()
                state=PLAY

            if leader_btn.clicked(e):
                state=LEADER

            if settings_btn.clicked(e):
                state=SETTINGS

            if quit_btn.clicked(e):
                running=False

        # -------- SETTINGS --------
        if state==SETTINGS:
            if grid_btn.clicked(e):
                settings["grid"]=not settings["grid"]

            if sound_btn.clicked(e):
                settings["sound"]=not settings["sound"]

            if back_btn.clicked(e):
                with open("settings.json","w") as f:
                    json.dump(settings,f)
                state=MENU

            for rect,color in color_buttons:
                if e.type==pygame.MOUSEBUTTONDOWN and rect.collidepoint(e.pos):
                    settings["snake_color"]=list(color)

        # -------- GAME OVER --------
        if state==OVER:
            if retry_btn.clicked(e):
                game.reset()
                state=PLAY

            if menu_btn.clicked(e):
                state=MENU
                username=""

        # -------- LEADERBOARD --------
        if state==LEADER:
            if back_btn.clicked(e):
                state=MENU

    # -------- MUSIC --------
    if state==PLAY and settings["sound"]:
        if not music:
            pygame.mixer.music.play(-1)
            music=True
    else:
        if music:
            pygame.mixer.music.stop()
            music=False

    # -------- DRAW --------
    if state==MENU:
        screen.blit(big_font.render("Enter Username",True,WHITE),(140,160))
        screen.blit(font.render(username,True,WHITE),(200,210))

        start_btn.draw(screen)
        leader_btn.draw(screen)
        settings_btn.draw(screen)
        quit_btn.draw(screen)

    elif state==PLAY:
        if settings["grid"]:
            for x in range(0,WIDTH,CELL):
                pygame.draw.line(screen,(40,40,40),(x,0),(x,HEIGHT))
            for y in range(0,HEIGHT,CELL):
                pygame.draw.line(screen,(40,40,40),(0,y),(WIDTH,y))

        if not game.update():
            pygame.mixer.music.stop()
            if settings["sound"]:
                gameover_sound.play()
            save_score(player_id,game.score,game.level)
            state=OVER

        game.draw(screen,font)

        best = get_best(player_id)
        screen.blit(font.render(f"Best: {best}", True, WHITE), (10,40))

    elif state==OVER:
        screen.blit(big_font.render("GAME OVER",True,RED),(150,200))
        screen.blit(font.render(f"Score: {game.score}",True,WHITE),(240,260))

        retry_btn.draw(screen)
        menu_btn.draw(screen)

    elif state==SETTINGS:
        screen.blit(big_font.render("SETTINGS",True,WHITE),(180,50))

        start_y = 120
        gap = 90

        # GRID
        screen.blit(font.render(f"Grid: {settings['grid']}", True, WHITE), (220, start_y))
        grid_btn.rect.y = start_y + 35
        grid_btn.draw(screen)

        # SOUND
        screen.blit(font.render(f"Sound: {settings['sound']}", True, WHITE), (220, start_y + gap))
        sound_btn.rect.y = start_y + gap + 35
        sound_btn.draw(screen)

        # COLORS
        color_y = start_y + gap*2 + 20
        screen.blit(font.render("Snake Color:", True, WHITE), (200, color_y))

        for i,(rect,color) in enumerate(color_buttons):
            rect.x = 180 + i*60
            rect.y = color_y + 40
            pygame.draw.rect(screen,color,rect)

            if list(color)==settings["snake_color"]:
                pygame.draw.rect(screen,WHITE,rect,3)

        # BACK
        back_btn.rect.y = color_y + 120
        back_btn.draw(screen)

    elif state==LEADER:
        screen.blit(big_font.render("LEADERBOARD",True,WHITE),(120,60))

        scores = get_top()
        start_y = 140
        line_h = 35

        for i,(name,score) in enumerate(scores[:10]):
            y = start_y + i*line_h
            screen.blit(font.render(f"{i+1}. {name} - {score}",True,WHITE),(160,y))

        back_btn.rect.y = start_y + len(scores[:10])*line_h + 20
        back_btn.draw(screen)

    pygame.display.flip()
    clock.tick(game.speed)

pygame.quit()
sys.exit()