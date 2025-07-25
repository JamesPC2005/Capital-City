#drawing objects and shapes in python
import pygame

pygame.init

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
gameDisplay.fill(black)

#change the colors of individual pixels
pixAr = pygame.PixelArray(gameDisplay)
pixAr[10][20] = green

#draw a line
pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)
#rectangle
pygame.draw.rect(gameDisplay, red, (400,400,50,25))
#circle
pygame.draw.circle(gameDisplay, white, (150,150), 75)
#polygons
pygame.draw.polygon(gameDisplay, green, ((25,75),(76,125),(250,375),(400,25)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            quit()
    pygame.display.update()
