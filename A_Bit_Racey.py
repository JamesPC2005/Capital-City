import pygame
import time
import random
pygame.init()

#setup window
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit Racey')

#setup colors
black = (0,0,0)
white = (255,255,255)

#creates setup clock
clock = pygame.time.Clock()

#create sprite
carImg = pygame.image.load('racecar.png')

# function to display car at the right location
def car(x,y):
    gameDisplay.blit(carImg, (x,y))

#draw obsticles
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#crash, message_display and text_objects are a set of functions used to display text when you crash
def crash():
    message_display("You Crashed")

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    Textsurface, Textrect = text_objects(text, largeText)
    Textrect.center = (display_width/2 , display_height/2)
    gameDisplay.blit(Textsurface, Textrect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

def text_objects(text, font):
    Textsurface = font.render(text, True, black)
    return Textsurface, Textsurface.get_rect()


def game_loop():
    gameexit = False
    x = display_width * .45
    y = display_height * .8
    x_change = 0

    thing_startx = random.randrange(0, display_width - 100)
    thing_starty = -600
    thing_speed = 7
    thing_width = 100
    thing_height = 100

    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

        #check if a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        x += x_change
        gameDisplay.fill(white)
        #things(thingx, thingy, thingw, thingh, color):
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed

        #when the obsticle moves off screen, make a new one
        if thing_starty > display_height:
            thing_startx = random.randrange(0, display_width - 100)
            thing_starty = 0 - thing_height

        car(x,y)

        #check for losses
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width:
                crash()
        if x < 0 or x > display_width:
            crash()
        
        pygame.display.update()
        clock.tick(60)

game_loop()