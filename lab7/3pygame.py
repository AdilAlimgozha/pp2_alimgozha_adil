import pygame

def movement():
    global y
    global x
    if pressed[pygame.K_UP] and y > r:
        y -= step
    if pressed[pygame.K_DOWN] and y < h - r:
        y += step
    if pressed[pygame.K_LEFT] and x > r:
        x -= step
    if pressed[pygame.K_RIGHT] and x < w - r:
        x += step

pygame.init()
w, h = 400, 300
screen = pygame.display.set_mode((w, h))
done = False
x, y, step, r = w/2, h/2, 20, 25
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), r)

    pressed = pygame.key.get_pressed()
    movement()

    pygame.display.flip()
    clock.tick(60)
#done