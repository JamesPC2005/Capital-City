import pygame
import time
import random
pygame.init()

#setup window
display_width = 1600
display_height = 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Capital City')

#setup colors
black = (0,0,0)
grey = (50,50,50)
white = (255,255,255)
red = (200,0,0)
bright_red = (255,0,0)
green = (0,200,0)
bright_green = (0,255,0)
blue = (0,0,200)
bright_blue= (0,0,255)

#creates setup clock
clock = pygame.time.Clock()

#create sprite, unused
#sprite = pygame.image.load('name of file')


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
        Textsurface, Textrect = text_objects("Capital City", largeText)
        Textrect.center = (display_width/2 , display_height/4)
        gameDisplay.blit(Textsurface, Textrect)
        
        mouse = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()
        if display_width / 2 + 50 > mouse[0] > display_width / 2 - 50 and display_height / 4 + display_height / 12 + 50 > mouse[1] > display_height / 4 + display_height / 12:
            pygame.draw.rect(gameDisplay, bright_green,(display_width / 2 - 50 , display_height / 4 + display_height / 12 , 100 , 50))
            pygame.draw.rect(gameDisplay, red,(display_width / 2 - 50 , display_height / 4 + 2 * display_height / 12 , 100 , 50))
            if press[0] == 1:
                game_loop()


        elif display_width / 2 + 50 > mouse[0] > display_width / 2 - 50 and display_height / 4 + 2 * display_height / 12 + 50 > mouse[1] > display_height / 4 + (2 * display_height) / 12:
            pygame.draw.rect(gameDisplay, bright_red,(display_width / 2 - 50 , display_height / 4 + 2 * display_height / 12 , 100 , 50))
            pygame.draw.rect(gameDisplay, green,(display_width / 2 - 50 , display_height / 4 + display_height / 12 , 100 , 50))
            if press[0] == 1:
                pygame.quit()


        else:
            pygame.draw.rect(gameDisplay, green,(display_width / 2 - 50 , display_height / 4 + display_height / 12 , 100 , 50))
            pygame.draw.rect(gameDisplay, red,(display_width / 2 - 50 , display_height / 4 + 2 * display_height / 12 , 100 , 50))

        largeText = pygame.font.Font('freesansbold.ttf', 20)
        Textsurface, Textrect = text_objects("Start", largeText)
        Textrect.center = (display_width / 2  , display_height / 4 + display_height / 12 + 25 )
        gameDisplay.blit(Textsurface, Textrect)

        largeText = pygame.font.Font('freesansbold.ttf', 20)
        Textsurface, Textrect = text_objects("Quit", largeText)
        Textrect.center = (display_width / 2 , display_height / 4 + (2 * display_height) / 12 + 25)
        gameDisplay.blit(Textsurface, Textrect)

        pygame.display.update()
        clock.tick(15)


def board_initialize():
    grid = [[None for i in range(8)] for j in range(6)]
    return grid


def draw_board(board):

    startx = display_width / 5 #save space for ui
    starty = 0 #save space for ui

    cell_width = ((display_width * 4) / 5) / len(board[0])   # columns
    cell_height = ((display_height * 3) / 4) / len(board)    # rows

    for row in range(len(board)):
        for col in range(len(board[0])):
            x = startx + (col * cell_width)
            y = starty + (row * cell_height)
            pygame.draw.rect(gameDisplay, white, (x, y, cell_width, cell_height))
            pygame.draw.rect(gameDisplay, black, (x, y, cell_width, cell_height), 1) # the 1 at the end adds a border

    draw_cells()

def draw_cells():
    #use this space later to draw the images of objects in the board spaces based on the stored values in board
    '''
    for row in len(board):
        #
        #
        for col in len(board[0]):
            #
            #
    '''



def game_loop():
    gameexit = False
    board = board_initialize()

    

    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                quit()

        #check if a key is pressed
        #    if event.type == pygame.KEYDOWN:
        #        if event.key == pygame.K_LEFT:
        #            x_change = -5
        #        if event.key == pygame.K_RIGHT:
        #            x_change = 5
        #    if event.type == pygame.KEYUP:
        #        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
        #            x_change = 0

        gameDisplay.fill(grey)
        draw_board(board)
        
        pygame.display.update()
        clock.tick(60)

game_intro()
#game_loop()