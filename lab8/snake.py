import os
from select import select
import pygame
import random

BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
BLOCK_SIZE = 20
FINISH = False


class Point:        #Point in x, y coordinates
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Wall:
    def __init__(self, lev):
        self.body = []
        with open("lab8/levels/level{}.txt".format(lev), "r") as f:
            for y in range(0, HEIGHT//BLOCK_SIZE + 1):
                for x in range(0, WIDTH//BLOCK_SIZE + 1):
                    if f.read(1) == '#':
                        self.body.append(Point(x, y))

    def draw(self):
        for point in self.body:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, (226,135,67), rect)

class Food:
    def __init__(self):     #giving point to food
        self.location = Point(random.randint(0, WIDTH/BLOCK_SIZE - 1), random.randint(0, HEIGHT/BLOCK_SIZE - 1))

    def draw(self, snake, wall):     #drawing food
        for point in snake.body[1:]:
            while point.x == self.location.x and point.y == self.location.y:
                self.location = Point(random.randint(0, WIDTH/BLOCK_SIZE - 1), random.randint(0, HEIGHT/BLOCK_SIZE - 1))
        for point in wall.body:
            while point.x == self.location.x and point.y == self.location.y:
                self.location = Point(random.randint(0, WIDTH/BLOCK_SIZE - 1), random.randint(0, HEIGHT/BLOCK_SIZE - 1))
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, (0, 255, 0), rect)

class Snake:
    def __init__(self):     #giving start point to snake
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):      #movement
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        for i in range(len(self.body) - 1, 1, -1):      #game over if snake collides with itself
            if (self.body[0].x == self.body[i].x and self.body[0].y == self.body[i].y):
                game_over = True
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                    SCREEN.fill((255, 0, 0))
                    stop_font = pygame.font.SysFont("Verdana", 60)
                    text = stop_font.render("""GAME OVER""", True, (BLACK))
                    SCREEN.blit(text, (10, 100))
                    pygame.display.update()
                    CLOCK.tick(5)

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):     #draw snake
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
        pygame.draw.rect(SCREEN, (255, 0, 0), rect)

        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE - 1, BLOCK_SIZE - 1)
            pygame.draw.rect(SCREEN, (0, 255, 0), rect)

    def check_collision(self, food):    #eating food
        if self.body[0].x == food.location.x and self.body[0].y == food.location.y:
            self.body.append(Point(food.location.x, food.location.y))
            food.location.x = random.randint(0, WIDTH/BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT/BLOCK_SIZE - 1)

    def check_border_collision(self):       #game over if snake collides with borders
        global game_over
        game_over = False
        if self.body[0].x < 0 or self.body[0].x > 19 or self.body[0].y < 0 or self.body[0].y > 19:
            game_over = True
            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                SCREEN.fill((255, 0, 0))
                stop_font = pygame.font.SysFont("Verdana", 60)
                text = stop_font.render("""GAME OVER""", True, (BLACK))
                SCREEN.blit(text, (10, 100))
                pygame.display.update()
                CLOCK.tick(5)
    def check_wall_collision(self, wall):
        game_over = False
        for point in wall.body:
            if self.body[0].x == point.x and self.body[0].y == point.y:
                game_over = True
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                    SCREEN.fill((255, 0, 0))
                    stop_font = pygame.font.SysFont("Verdana", 60)
                    text = stop_font.render("""GAME OVER""", True, (BLACK))
                    SCREEN.blit(text, (10, 100))
                    pygame.display.update()
                    CLOCK.tick(5)


class Score():
    def __init__(self, snake):      #score == lenth of snake
        self.score = len(snake.body) - 1
        self.lev = 1

    def counter(self, food, snake):     #score++ if length of snake++
        score_font = pygame.font.SysFont("Verdana", 20)
        text = score_font.render("SCORE " + str(len(snake.body) - 1) + " aim: " + str (4 * self.lev), True, (255, 255, 255))
        SCREEN.blit(text, (0,0))

    def level_counter(self):     #level++ if (length of snake - 1)++
        level_font = pygame.font.SysFont("Verdana", 20)
        text = level_font.render("level " + str(self.lev), True, (255, 255, 255))
        SCREEN.blit(text, (20, 20))

class Stopping():
    def pause(self):        #press "p" to pause/unpause
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
            SCREEN.fill((255, 255, 255))
            pause_font = pygame.font.SysFont("Verdana", 60)
            text = pause_font.render("PAUSE", True, (BLACK))
            SCREEN.blit(text, (100, 100))
            pygame.display.update()
            CLOCK.tick(5)

def main():

    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    d = {"w" : True, "a" : True, "s" : True, "d" : True}    #accessible directories

    snake = Snake()
    score = Score(snake)
    wall = Wall(score.lev)
    food = Food()
    stop = Stopping()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and d["d"] == True:      #move by buttons "wasd"
                    d = {"w" : True, "a" : False, "s" : True, "d" : True}   #if "d" cannot press "a"
                    snake.dx = 1
                    snake.dy = 0
                elif event.key == pygame.K_a and d["a"] == True:
                    d = {"w" : True, "a" : True, "s" : True, "d" : False}   #if "a" cannot press "d"
                    snake.dx = -1
                    snake.dy = 0
                elif event.key == pygame.K_w and d["w"] == True:
                    d = {"w" : True, "a" : True, "s" : False, "d" : True}   #if "w" cannot press "s"
                    snake.dx = 0
                    snake.dy = -1
                elif event.key == pygame.K_s and d["s"] == True:
                    d = {"w" : False, "a" : True, "s" : True, "d" : True}   #if "s" cannot press "w"
                    snake.dx = 0
                    snake.dy = 1
                if event.key == pygame.K_p:
                    stop.pause()
        
        snake.move()
        SCREEN.fill(BLACK)


        if 4 * score.lev < len(snake.body):
            if os.path.exists("lab8/levels/level{}.txt".format(score.lev)):
                score.lev += 1
                if os.path.exists("lab8/levels/level{}.txt".format(score.lev)) == False:
                    FINISH = True
                    while FINISH:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                        SCREEN.fill((0, 255, 255))
                        pause_font = pygame.font.SysFont("Verdana", 60)
                        text = pause_font.render("VICTORY", True, (255, 0, 0))
                        SCREEN.blit(text, (90, 100))
                        pygame.display.update()
                        CLOCK.tick(5)

                wall = Wall(score.lev)
                snake = Snake()
            
        wall.draw()
        drawGrid()

        snake.draw()
        food.draw(snake, wall)
        snake.check_collision(food)
        snake.check_border_collision()
        snake.check_wall_collision(wall)
        score.counter(food, snake)
        score.level_counter()
        x = score.lev

        pygame.display.update()
        CLOCK.tick(5 * x)

def drawGrid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        for y in range(0, HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, LINE_COLOR, rect, 1)

main()
#done