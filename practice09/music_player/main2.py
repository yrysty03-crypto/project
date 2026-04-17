import pygame
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 500, 350
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 28)

player = MusicPlayer("music")

volume = 0.5
player.set_volume(volume)

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((30, 30, 30))

    # STATUS
    if player.is_playing:
        status = "Playing"
    elif player.is_paused:
        status = "Paused"
    else:
        status = "Stopped"

    status_text = font.render(f"Status: {status}", True, (255, 255, 0))
    screen.blit(status_text, (20, 20))

    # TRACK
    track_text = font.render(f"Track: {player.get_current_track()}", True, (255, 255, 255))
    screen.blit(track_text, (20, 60))

    # TIME
    progress = player.get_position()
    time_text = font.render(f"Time: {progress}s", True, (200, 200, 200))
    screen.blit(time_text, (20, 90))

    # PROGRESS BAR
    bar_x, bar_y = 20, 120
    bar_width, bar_height = 400, 10

    total_length = 180
    ratio = min(progress / total_length, 1)

    pygame.draw.rect(screen, (70, 70, 70), (bar_x, bar_y, bar_width, bar_height))
    pygame.draw.rect(screen, (0, 200, 0), (bar_x, bar_y, bar_width * ratio, bar_height))

    # VOLUME
    vol_text = font.render(f"Volume: {int(volume * 100)}%", True, (180, 180, 180))
    screen.blit(vol_text, (20, 150))

    # CONTROLS
    controls = [
        "P - Play / Resume",
        "S - Pause",
        "SPACE - Pause/Resume",
        "N - Next",
        "B - Previous",
        "UP/DOWN - Volume",
        "Q - Quit"
    ]

    for i, text in enumerate(controls):
        label = font.render(text, True, (180, 180, 180))
        screen.blit(label, (20, 190 + i * 22))

    pygame.display.flip()

    # AUTO NEXT TRACK
    if not pygame.mixer.music.get_busy() and player.is_playing:
        player.next_track()

    # EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_p:
                player.play()

            elif event.key == pygame.K_s:
                player.stop()

            elif event.key == pygame.K_SPACE:
                if player.is_playing:
                    player.pause()
                elif player.is_paused:
                    player.resume()

            elif event.key == pygame.K_n:
                player.next_track()

            elif event.key == pygame.K_b:
                player.previous_track()

            elif event.key == pygame.K_UP:
                volume = min(1.0, volume + 0.1)
                player.set_volume(volume)

            elif event.key == pygame.K_DOWN:
                volume = max(0.0, volume - 0.1)
                player.set_volume(volume)

            elif event.key == pygame.K_q:
                running = False

    clock.tick(30)

pygame.quit()