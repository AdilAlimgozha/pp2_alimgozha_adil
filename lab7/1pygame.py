import pygame
import datetime
import os

pygame.init()
screen = pygame.display.set_mode((1000, 700))
done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    x = datetime.datetime.now()
    s = x.second
    m = x.minute
        
    screen.fill((0, 0, 0))
    image = pygame.image.load('lab7/images/mickeyclock.jpeg')
    seconds = pygame.image.load('lab7/images/seconds2.png')
    minutes = pygame.image.load('lab7/images/minutes2.png')

    image = pygame.transform.scale(image, (1000, 700))
    seconds = pygame.transform.scale(seconds, (180, 180))
    minutes = pygame.transform.scale(minutes, (150, 150))

    screen.blit(image, (0, 0))

    w, h = seconds.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
    box_rotate = [p.rotate(-s*6 + 134) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    origin = ((495, 350)[0] + min_box[0], (495, 350)[1] - max_box[1])
    rotated_image = pygame.transform.rotate(seconds, -s*6 + 134)
    screen.blit(rotated_image, origin)

    w1, h1 = minutes.get_size()
    box = [pygame.math.Vector2(p) for p in [(0, 0), (w1, 0), (w1, -h1), (0, -h1)]]
    box_rotate = [p.rotate(-m*6 + 134) for p in box]
    min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
    max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])
    origin = ((500, 350)[0] + min_box[0], (500, 350)[1] - max_box[1])
    rotated_image1 = pygame.transform.rotate(minutes, -m*6 + 134)
    screen.blit(rotated_image1, origin)


    pygame.display.flip()
    clock.tick(60)
    #done