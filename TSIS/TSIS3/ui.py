import pygame

def get_font(size=30):
    return pygame.font.SysFont("Arial", size)

def draw_text(screen, text, x, y, size=30):
    font = get_font(size)
    screen.blit(font.render(text, True, (255,255,255)), (x, y))

def draw_center(screen, text, y, size=30, color=(255,255,255)):
    font = get_font(size)
    render = font.render(text, True, color)
    rect = render.get_rect(center=(screen.get_width()//2, y))
    screen.blit(render, rect)

def draw_input_box(screen, text, active, frame_count):
    box = pygame.Rect(120, 280, 260, 50)
    pygame.draw.rect(screen, (255,255,255), box, 2)

    cursor = "|" if (frame_count//30)%2==0 else ""
    txt = get_font(30).render(text+cursor, True, (255,255,255))
    screen.blit(txt, (box.x+10, box.y+10))

def main_menu(screen, name, active, frame):
    draw_center(screen,"RACER GAME",180,40)
    draw_center(screen,"Enter your name:",240)
    draw_input_box(screen,name,True,frame)
    draw_center(screen,"ENTER - Start",360,20)
    draw_center(screen,"L - Leaderboard",400,20)
    draw_center(screen,"S - Settings",430,20)

def game_over(screen, score):
    draw_center(screen,"GAME OVER",250,40,(255,0,0))
    draw_center(screen,f"Score: {score}",300)
    draw_center(screen,"Press any key",350,20)

def win_screen(screen, score):
    draw_center(screen,"YOU WIN!",250,40,(0,255,0))
    draw_center(screen,f"Distance: {score}",300)
    draw_center(screen,"Press any key",350,20)

def leaderboard_screen(screen,data):
    draw_center(screen,"LEADERBOARD",120,40)
    y=200
    for e in data:
        draw_center(screen,f"{e['name']} - {e['score']}",y)
        y+=30
    draw_center(screen,"Press any key",650,20)

def settings_screen(screen,s):
    draw_center(screen,"SETTINGS",150,40)
    draw_center(screen,f"Sound(S): {s.get('sound',True)}",250)
    draw_center(screen,"ESC to return",400,20)