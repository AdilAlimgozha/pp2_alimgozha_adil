import os
from select import select
import pygame
import random
from configparser import ConfigParser
import psycopg2

BLACK = (0, 0, 0)
LINE_COLOR = (50, 50, 50)
HEIGHT = 400
WIDTH = 400
BLOCK_SIZE = 20
FINISH = False
game_over = False


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

class SuperFood:
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
        pygame.draw.rect(SCREEN, (0, 255, 255), rect)

class Enter_user():
    def __init__(self):
        self.username = input("Enter username: ")
        self.user = self.username

    def enter(self):
        entering = True
        while entering:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        entering = False
            SCREEN.fill((255, 255, 255))
            enter_font = pygame.font.SysFont("Verdana", 20)
            text = enter_font.render("Username: " + self.username, True, (BLACK))
            SCREEN.blit(text, (20, 100))
            pygame.display.update()
            CLOCK.tick(5)

class Snake:
    def __init__(self):     #giving start point to snake
        self.body = [Point(10, 11)]
        self.dx = 0
        self.dy = 0

    def move(self, enter_user, score):
        for i in range(len(self.body) - 1, 0, -1):      #movement
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy

        for i in range(len(self.body) - 1, 1, -1):      #game over if snake collides with itself
            if (self.body[0].x == self.body[i].x and self.body[0].y == self.body[i].y):
                global game_over
                game_over = True
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            def config(filename='lab10/db/database.ini', section='postgresql'):
                                parser = ConfigParser()
                                parser.read(filename)
                                db = {}
                                if parser.has_section(section):
                                    params = parser.items(section)
                                    for param in params:
                                        db[param[0]] = param[1]
                                else:
                                    raise Exception('Section {0} not found in the {1} file'.format(section, filename))
                                return db

                            try:
                                params = config()
                                conn = psycopg2.connect(**params)
                                cursor = conn.cursor()

                                sql = '''CREATE TABLE SCORE (username TEXT, level INT, score INT);'''

                                cursor.execute(sql)

                                sql1 = """INSERT INTO SCORE (username, level, score) VALUES ('""" + enter_user.user + """',""" + str(score.lev) + """,""" + str(len(self.body) - 1) + """);"""

                                cursor.execute(sql1)

                                sql2 = """
                                select * from SCORE;
                                """
                                cursor.execute(sql2)

                                for i in cursor.fetchall():
                                    print(i)
  
                                conn.commit()
                                conn.close()
                            except(Exception, psycopg2.DatabaseError) as error:
                                print(error)
                            finally:
                                if conn is not None:
                                    conn.close()
                                    print("connection closed")
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

    def check_collision(self, food, timer, probability):    #eating food
        if self.body[0].x == food.location.x and self.body[0].y == food.location.y:
            timer.counter = 10
            self.body.append(Point(food.location.x, food.location.y))
            food.location.x = random.randint(0, WIDTH/BLOCK_SIZE - 1)
            food.location.y = random.randint(0, HEIGHT/BLOCK_SIZE - 1)
            probability.p = random.randint(1, 4)


    def check_collision_superFood(self, superFood, timer, probability):     #eating superFood
        if self.body[0].x == superFood.location.x and self.body[0].y == superFood.location.y:
            timer.counter = 10
            prob_len = random.randint(2, 3)
            if prob_len == 2:
                self.body.append(Point(superFood.location.x, superFood.location.y))
                self.body.append(Point(superFood.location.x, superFood.location.y))
            elif prob_len == 3:
                self.body.append(Point(superFood.location.x, superFood.location.y))
                self.body.append(Point(superFood.location.x, superFood.location.y))
                self.body.append(Point(superFood.location.x, superFood.location.y))
            superFood.location.x = random.randint(0, WIDTH/BLOCK_SIZE - 1)
            superFood.location.y = random.randint(0, HEIGHT/BLOCK_SIZE - 1)
            probability.p = random.randint(1, 4)


    def check_border_collision(self, enter_user, score):       #game over if snake collides with borders
        if self.body[0].x < 0 or self.body[0].x > 19 or self.body[0].y < 0 or self.body[0].y > 19:
            global game_over
            game_over = True
            while game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        def config(filename='lab10/db/database.ini', section='postgresql'):
                            parser = ConfigParser()
                            parser.read(filename)
                            db = {}
                            if parser.has_section(section):
                                params = parser.items(section)
                                for param in params:
                                    db[param[0]] = param[1]
                            else:
                                raise Exception('Section {0} not found in the {1} file'.format(section, filename))
                            return db

                        try:
                            params = config()
                            conn = psycopg2.connect(**params)
                            cursor = conn.cursor()

                            sql = '''CREATE TABLE SCORE (username TEXT, level INT, score INT);'''

                            cursor.execute(sql)

                            sql1 = """INSERT INTO SCORE (username, level, score) VALUES ('""" + enter_user.user + """',""" + str(score.lev) + """,""" + str(len(self.body) - 1) + """);"""

                            cursor.execute(sql1)

                            sql2 = """
                            select * from SCORE;
                            """
                            cursor.execute(sql2)

                            for i in cursor.fetchall():
                                print(i)
  
                            conn.commit()
                            conn.close()
                        except(Exception, psycopg2.DatabaseError) as error:
                            print(error)
                        finally:
                            if conn is not None:
                                conn.close()
                                print("connection closed")
                        pygame.quit()
                SCREEN.fill((255, 0, 0))
                stop_font = pygame.font.SysFont("Verdana", 60)
                text = stop_font.render("""GAME OVER""", True, (BLACK))
                SCREEN.blit(text, (10, 100))
                pygame.display.update()
                CLOCK.tick(5)
    def check_wall_collision(self, wall, enter_user, score):       #wall collision
        for point in wall.body:
            if self.body[0].x == point.x and self.body[0].y == point.y:
                global game_over
                game_over = True
                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            def config(filename='lab10/db/database.ini', section='postgresql'):
                                parser = ConfigParser()
                                parser.read(filename)
                                db = {}
                                if parser.has_section(section):
                                    params = parser.items(section)
                                    for param in params:
                                        db[param[0]] = param[1]
                                else:
                                    raise Exception('Section {0} not found in the {1} file'.format(section, filename))
                                return db

                            try:
                                params = config()
                                conn = psycopg2.connect(**params)
                                cursor = conn.cursor()

                                sql = '''CREATE TABLE SCORE (username TEXT, level INT, score INT);'''

                                cursor.execute(sql)

                                sql1 = """INSERT INTO SCORE (username, level, score) VALUES ('""" + enter_user.user + """',""" + str(score.lev) + """,""" + str(len(self.body) - 1) + """);"""

                                cursor.execute(sql1)

                                sql2 = """
                                select * from SCORE;
                                """
                                cursor.execute(sql2)

                                for i in cursor.fetchall():
                                    print(i)
  
                                conn.commit()
                                conn.close()
                            except(Exception, psycopg2.DatabaseError) as error:
                                print(error)
                            finally:
                                if conn is not None:
                                    conn.close()
                                    print("connection closed")
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

    def counter(self, snake):     #score++ if length of snake++
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

class Timer():                  #timer of disappearing food
    def __init__(self):
        self.counter = 10

    def run_counter(self, snake, score, food):
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        run_font = pygame.font.SysFont("Verdana", 20)
        text = run_font.render("timer: " + str(self.counter), True, ((255, 255, 255)))
        SCREEN.blit(text, (297, 5))
        pygame.display.flip()
        CLOCK.tick(60)

        if snake.dx == 1 or snake.dx == -1 or snake.dy == 1 or snake.dy == -1:
            self.counter = self.counter - 0.2 / score.lev
        if self.counter < 0:
            food.location = Point(random.randint(0, WIDTH/BLOCK_SIZE - 1), random.randint(0, HEIGHT/BLOCK_SIZE - 1))
            self.counter = 10

class TimerSuperFood():             #timer of disappearing superFood
    def __init__(self):
        self.counter = 10

    def run_counter(self, snake, score, superFood):
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        run_font = pygame.font.SysFont("Verdana", 20)
        text = run_font.render("timer: " + str(self.counter), True, ((255, 255, 255)))
        SCREEN.blit(text, (297, 5))
        pygame.display.flip()
        CLOCK.tick(60)

        if snake.dx == 1 or snake.dx == -1 or snake.dy == 1 or snake.dy == -1:
            self.counter = self.counter - 0.2 / score.lev
        if self.counter < 0:
            superFood.location = Point(random.randint(0, WIDTH/BLOCK_SIZE - 1), random.randint(0, HEIGHT/BLOCK_SIZE - 1))
            self.counter = 10

class Probability():        #probability of appearing superFood
    def __init__(self):
        self.p = random.randint(1, 4)

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
    stop = Stopping()
    food = Food()
    timer = Timer()
    probability = Probability()
    superFood = SuperFood()
    timerSuperFood = TimerSuperFood()
    enter_user = Enter_user()

    enter_user.username

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                def config(filename='lab10/db/database.ini', section='postgresql'):
                    parser = ConfigParser()
                    parser.read(filename)
                    db = {}
                    if parser.has_section(section):
                        params = parser.items(section)
                        for param in params:
                            db[param[0]] = param[1]
                    else:
                        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
                    return db

                try:
                    params = config()
                    conn = psycopg2.connect(**params)
                    cursor = conn.cursor()

                    sql = '''CREATE TABLE SCORE (username TEXT, level INT, score INT);'''

                    cursor.execute(sql)

                    sql1 = """INSERT INTO SCORE (username, level, score) VALUES ('""" + enter_user.user + """',""" + str(score.lev) + """,""" + str(len(snake.body) - 1) + """);"""

                    cursor.execute(sql1)

                    sql2 = """
                    select * from SCORE;
                    """
                    cursor.execute(sql2)

                    for i in cursor.fetchall():
                        print(i)
  
                    conn.commit()
                    conn.close()
                except(Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()
                        print("connection closed")
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
                if event.key == pygame.K_SPACE:
                    enter_user.enter()
        
        snake.move(enter_user, score)
        SCREEN.fill(BLACK)


        if 4 * score.lev < len(snake.body):         #levels
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
        score.counter(snake)
        score.level_counter()
        if 2 <= probability.p <= 4:         #what will appear food or superFood?
            food.draw(snake, wall)
            timer.run_counter(snake, score, food)
            snake.check_collision(food, timer, probability)

        elif probability.p == 1:            #what will appear food or superFood?
            superFood.draw(snake, wall)
            timer.run_counter(snake, score, superFood)
            snake.check_collision_superFood(superFood, timer, probability)

        

        snake.check_border_collision(enter_user, score)
        snake.check_wall_collision(wall, enter_user, score)
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
#no db when qiut from pause
#no db when quit from victory screen