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
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,200)
bright_blue= (0,0,255)

#creates setup clock
clock = pygame.time.Clock()

#create sprite
carImg = pygame.image.load('racecar.png')

#function to display car at the right location
def car(x,y):
    gameDisplay.blit(carImg, (x,y))
#count doged obsticles
def things_doged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render('Doged ' + str(count), True, black)
    gameDisplay.blit(text, (0,0))

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

    game_intro()

def text_objects(text, font):
    Textsurface = font.render(text, True, black)
    return Textsurface, Textsurface.get_rect()

#create intro
def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        Textsurface, Textrect = text_objects("A Bit Racey", largeText)
        Textrect.center = (display_width/2 , display_height/2)
        gameDisplay.blit(Textsurface, Textrect)
        
        mouse = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        if 250 > mouse[0] > 150 and 500 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_green,(150,450,100,50))
            pygame.draw.rect(gameDisplay, red,(550,450,100,50))
            if press[0] == 1:
                game_loop()
        elif 650 > mouse[0] > 550 and 500 > mouse[1] > 450:
            pygame.draw.rect(gameDisplay, bright_red,(550,450,100,50))
            pygame.draw.rect(gameDisplay, green,(150,450,100,50))
            if press[0] == 1:
                pygame.quit()
        else:
            pygame.draw.rect(gameDisplay, green,(150,450,100,50))
            pygame.draw.rect(gameDisplay, red,(550,450,100,50))

        largeText = pygame.font.Font('freesansbold.ttf', 20)
        Textsurface, Textrect = text_objects("Start", largeText)
        Textrect.center = (200 , 475)
        gameDisplay.blit(Textsurface, Textrect)

        largeText = pygame.font.Font('freesansbold.ttf', 20)
        Textsurface, Textrect = text_objects("Quit", largeText)
        Textrect.center = (600 , 475)
        gameDisplay.blit(Textsurface, Textrect)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    gameexit = False
    doged = 0
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
            doged += 1
            thing_speed += .3

        car(x,y)
        things_doged(doged)

        #check for losses
        if y < thing_starty + thing_height:
            if x > thing_startx and x < thing_startx + thing_width:
                crash()
        if x < 0 or x > display_width:
            crash()
        
        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()