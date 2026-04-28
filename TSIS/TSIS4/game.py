import pygame, random, time
from config import *

class Game:
    def __init__(self, settings, sounds):
        self.settings = settings
        self.sounds = sounds
        self.reset()

    def reset(self):
        self.snake = [(100,100),(80,100),(60,100)]
        self.direction = (CELL,0)
        self.score = 0
        self.level = 1
        self.speed = 10

        self.food = self.spawn()
        self.poison = self.spawn()
        self.power = None
        self.obstacles = []

        self.effect_end = 0
        self.shield = False

    def spawn(self):
        return (random.randrange(0, WIDTH, CELL),
                random.randrange(0, HEIGHT, CELL))

    def safe_obstacles(self):
        self.obstacles = []
        for _ in range(self.level + 2):
            while True:
                p = self.spawn()
                if p not in self.snake:
                    self.obstacles.append(p)
                    break

    def update(self):
        head = (self.snake[0][0]+self.direction[0],
                self.snake[0][1]+self.direction[1])

        if (head[0]<0 or head[0]>=WIDTH or
            head[1]<0 or head[1]>=HEIGHT or
            head in self.snake or
            (head in self.obstacles and not self.shield)):
            return False

        self.snake.insert(0, head)

        if head == self.food:
            self.score += 1
            if self.settings["sound"]:
                self.sounds["eat"].play()
            self.food = self.spawn()
        else:
            self.snake.pop()

        if head == self.poison:
            for _ in range(2):
                if len(self.snake)>1:
                    self.snake.pop()
            if len(self.snake)<=1:
                return False
            self.poison = self.spawn()

        if not self.power and random.random()<0.01:
            self.power = (self.spawn(), random.choice(["speed","slow","shield"]))

        if self.power and head == self.power[0]:
            if self.power[1]=="speed": self.speed=15
            if self.power[1]=="slow": self.speed=5
            if self.power[1]=="shield": self.shield=True
            self.effect_end = pygame.time.get_ticks()+5000
            self.power=None

        if self.effect_end and pygame.time.get_ticks()>self.effect_end:
            self.speed=10
            self.shield=False

        self.level = self.score//5+1

        if self.level>=3 and not self.obstacles:
            self.safe_obstacles()

        return True

    def draw(self, screen, font):
        color = tuple(self.settings["snake_color"])

        for s in self.snake:
            pygame.draw.rect(screen, color, (*s,CELL,CELL))

        pygame.draw.rect(screen, RED, (*self.food,CELL,CELL))

        x,y = self.poison
        blink = PURPLE if int(time.time()*5)%2==0 else RED
        pygame.draw.rect(screen, blink, (x,y,CELL,CELL))

        pygame.draw.circle(screen, BLACK, (x+6,y+7),2)
        pygame.draw.circle(screen, BLACK, (x+14,y+7),2)

        if self.power:
            pygame.draw.rect(screen, CYAN, (*self.power[0],CELL,CELL))

        for o in self.obstacles:
            pygame.draw.rect(screen, WHITE, (*o,CELL,CELL))

        screen.blit(font.render(f"Score: {self.score}", True, WHITE),(10,10))