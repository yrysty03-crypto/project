import pygame
from racer import Game
from ui import *
from persistence import *

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 500, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

pygame.mixer.music.load("assets/menu_music.wav")

state = "menu"
game = Game(WIDTH, HEIGHT)

leaderboard = load_leaderboard()
settings = load_settings()

player_name = ""
frame_count = 0

running = True
while running:
    screen.fill((40, 40, 40))
    frame_count += 1

    # MENU MUSIC
    if state == "menu":
        if settings.get("sound", True):
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.stop()
    else:
        pygame.mixer.music.stop()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if state == "menu":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN and player_name:
                    pygame.mixer.music.stop()
                    game.reset()
                    game.apply_settings(settings)
                    state = "game"

                elif event.key == pygame.K_BACKSPACE:
                    player_name = player_name[:-1]

                elif event.key == pygame.K_l:
                    leaderboard = load_leaderboard()
                    state = "leaderboard"

                elif event.key == pygame.K_s:
                    state = "settings"

                else:
                    if len(player_name) < 10:
                        player_name += event.unicode

        elif state == "game":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    game.player.x -= 10
                elif event.key == pygame.K_RIGHT:
                    game.player.x += 10

        elif state == "game_over":
            if event.type == pygame.KEYDOWN:
                save_score(player_name, int(game.distance))
                player_name = ""
                state = "menu"

        elif state == "win":
            if event.type == pygame.KEYDOWN:
                save_score(player_name, int(game.distance))
                player_name = ""
                state = "menu"

        elif state == "leaderboard":
            if event.type == pygame.KEYDOWN:
                state = "menu"

        elif state == "settings":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_settings(settings)
                    state = "menu"

    # GAME STATE
    if state == "menu":
        main_menu(screen, player_name, True, frame_count)

    elif state == "game":
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            game.player.x -= 5
        if keys[pygame.K_RIGHT]:
            game.player.x += 5

        # keep inside screen
        game.player.x = max(0, game.player.x)
        game.player.x = min(WIDTH - game.player.width, game.player.x)

        game.update()
        game.draw(screen)

        draw_text(screen, f"{int(game.distance)}/{game.finish_distance}", 10, 10)

        if game.check_collision():
            game.stop_engine()
            state = "game_over"

        if game.finished:
            game.stop_engine()
            state = "win"

    elif state == "game_over":
        game_over(screen, int(game.distance))

    elif state == "win":
        win_screen(screen, int(game.distance))

    elif state == "leaderboard":
        leaderboard_screen(screen, leaderboard)

    elif state == "settings":
        settings_screen(screen, settings)

    pygame.display.update()
    clock.tick(60)

pygame.quit()