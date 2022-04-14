import pygame
from math import sqrt

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    baseLayer = pygame.Surface((640, 480))
    clock = pygame.time.Clock()
    
    prevX = 0
    prevY = 0

    prevX1 = -1
    prevY1 = -1
    currentX1 = -1
    currentY1 = -1

    color = (0, 0, 0)

    
    screen.fill((255, 255, 255))

    isMouseDown = False

    while True:
        
        pressed = pygame.key.get_pressed()

        currentX = prevX
        currentY = prevY
        
        for event in pygame.event.get():        #pen
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: 
                    isMouseDown = True

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1: 
                    isMouseDown = False

            if event.type == pygame.MOUSEMOTION:
                currentX = event.pos[0]
                currentY = event.pos[1]


            if event.type == pygame.MOUSEBUTTONDOWN:        #rectangle
                if event.button == 1: 
                    isMouseDown = True
                    currentX1 = event.pos[0]
                    currentY1 = event.pos[1]    
                    prevX1 =  event.pos[0]
                    prevY1 =  event.pos[1]

            if event.type == pygame.MOUSEBUTTONUP:
                isMouseDown = False
                baseLayer.blit(screen, (0, 0))


            if event.type == pygame.MOUSEMOTION:
                if isMouseDown:
                    currentX1 =  event.pos[0]
                    currentY1 =  event.pos[1]
            
            if event.type == pygame.KEYDOWN:        #color 1, 2, 3, 4
                if event.key == pygame.K_2:
                    color = (255, 0, 0)
                elif event.key == pygame.K_3:
                    color = (0, 255, 0)
                elif event.key == pygame.K_4:
                    color = (0, 0, 255)
                elif event.key == pygame.K_1:
                    color = (0, 0, 0)
        
        if isMouseDown and pressed[pygame.K_w] == False and pressed[pygame.K_q] == False:     #pen
            pygame.draw.line(screen, color, (prevX, prevY), (currentX, currentY))

        if pressed[pygame.K_w]:     #rectangle w
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRect(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.rect(screen, color, pygame.Rect(r), 1)

        if pressed[pygame.K_e]:     #circle e
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))

                r = calculateRect(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(r), 1)

                c = centerCirc(prevX1, prevY1, currentX1, currentY1)
                s = radiusCirc(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.circle(screen, color, c, s, 1)

        if pressed[pygame.K_r]:     #square r
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateSqrt(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.rect(screen, color, pygame.Rect(r), 1)

        if pressed[pygame.K_t]:     #triangle t
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRtriangle(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color, r, 1)

        if pressed[pygame.K_y]:     #equilateral triangle y
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                r = equilateraltriangle(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color, r, 1)

        if pressed[pygame.K_u]:     #rhombus u
            if isMouseDown and prevX1 != -1 and prevY1 != -1 and currentX1 != -1 and currentY1 != -1:
                screen.blit(baseLayer, (0, 0))
                r = calculateRomb(prevX1, prevY1, currentX1, currentY1)
                pygame.draw.polygon(screen, color, r, 1)


        if pressed[pygame.K_q]:     #eraser q 
            if isMouseDown:
                pygame.draw.line(screen, (255, 255, 255), (prevX, prevY), (currentX, currentY), 20)

        prevX = currentX
        prevY = currentY
        
        pygame.display.flip()
        clock.tick(60)

def calculateRect(x1, y1, x2, y2):      #rect
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
    
def centerCirc(x1, y1, x2, y2):         #center of circle
    return abs(x1 - x2) / 2 + min(x1, x2), abs(y1 - y2) / 2 + min(y1, y2)

def radiusCirc(x1, y1, x2, y2):         #radius of circle
    return sqrt((abs(x1 - x2) / 2) ** 2 + (abs(y1 - y2) / 2) ** 2)

def calculateSqrt(x1, y1, x2, y2):      #square
    return min(x1, x2), min(y1, y2), abs(x1 - x2), abs(x1 - x2)

def calculateRtriangle(x1, y1, x2, y2):     #right triangle
    return [(min(x1, x2), min(y1, y2)), (min(x1, x2), abs(y1 - y2) + min(y1, y2)), (abs(x1 - x2) + min(x1, x2), abs(y1 - y2) + min(y1, y2))]

def equilateraltriangle(x1, y1, x2, y2):    #equilateral triangle
    side = min(abs(x2-x1), abs(y2-y1))
    height = round(side * 0.866)
    x = 1
    y = 1

    if (x2 > x1):
        x = -1
    if (y2 > y1):
        y = -1
    pnt1 = (x2 + round(side/2)*x, y2)
    pnt2 = (x2, y2 + height*y)
    pnt3 = (x2 + side*x, y2 + height*y)
    return (pnt1, pnt2, pnt3)

def calculateRomb(x1, y1, x2, y2):      #rhombus
    dx, dy = x2-x1,y2-y1
    return (x1,y1+dy),(x1+dx,y1),(x1,y1-dy),(x1-dx,y1)

main()