import pygame, sys
from pygame.locals import *
import random, time
 
#Initialzing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0
 
#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
background = pygame.image.load("lab8/images_racer/AnimatedStreet.png")
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#create enemy
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab8/images_racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)  
 
      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
 
#create player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab8/images_racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top > 0:
            if pressed_keys[K_w]:
                self.rect.move_ip(0, -7)
        if self.rect.bottom < SCREEN_HEIGHT:
            if pressed_keys[K_s]:
                self.rect.move_ip(0, 7)
        if self.rect.left > 0:
              if pressed_keys[K_a]:
                  self.rect.move_ip(-7, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_d]:
                  self.rect.move_ip(7, 0)

#create cion
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab8/images_racer/coin.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(0, SCREEN_WIDTH - 80), random.randint(SCREEN_HEIGHT / 3, SCREEN_HEIGHT - 80))
    def draw(self):
        DISPLAYSURF.blit(self.image, self.rect.center)
          
#Setting up Sprites    
P1 = Player()
C1 = Coin()   
E1 = Enemy()
 
#Creating Sprites Groups
player = pygame.sprite.Group()
player.add(P1)

coins = pygame.sprite.Group()
coins.add(C1)

enemies = pygame.sprite.Group()
enemies.add(E1)

move_sprites = pygame.sprite.Group()
move_sprites.add(P1)
move_sprites.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

pygame.mixer.Sound('lab8/sounds_racer/background.wav').play(-1)

#Game Loop
while True:
       
    #Cycles through all events occurring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("score: " + str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coins = font_small.render("coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(coins, (SCREEN_WIDTH - 100, 10)) 
 
    # draw coin
    C1.draw()

    #Moves and Re-draws car Sprites
    for entity in move_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # coins++ if collision
    if pygame.sprite.spritecollideany(C1, player):
        COINS += 1
        pygame.mixer.Sound('lab8/sounds_racer/coin.wav').play()
        C1 = Coin()

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('lab8/sounds_racer/crash.wav').play()
        time.sleep(0.5)
                    
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
           
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()     
    
    pygame.display.update()
    FramePerSec.tick(FPS)