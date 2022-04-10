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

        if pressed[pygame.K_q]:     #eraser q 
            if isMouseDown:
                pygame.draw.line(screen, (255, 255, 255), (prevX, prevY), (currentX, currentY), 20)

        prevX = currentX
        prevY = currentY
        
        pygame.display.flip()
        clock.tick(60)

def calculateRect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))
    
def centerCirc(x1, y1, x2, y2):
    return abs(x1 - x2) / 2 + min(x1, x2), abs(y1 - y2) / 2 + min(y1, y2)

def radiusCirc(x1, y1, x2, y2):
    return sqrt((abs(x1 - x2) / 2) ** 2 + (abs(y1 - y2) / 2) ** 2)

main()