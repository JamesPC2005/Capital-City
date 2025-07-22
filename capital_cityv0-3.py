import pygame
import time
import random
pygame.init()

# Setup window
display_width = 1600
display_height = 1000
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Capital City')

# Setup colors
black = (0, 0, 0)
grey = (50, 50, 50)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (0, 255, 0)
blue = (0, 0, 200)
bright_blue = (0, 0, 255)

# Clock setup
clock = pygame.time.Clock()

# Unused sprite example
# sprite = pygame.image.load('name of file')

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    Textsurface, Textrect = text_objects(text, largeText)
    Textrect.center = (display_width / 2, display_height / 2)
    gameDisplay.blit(Textsurface, Textrect)

    pygame.display.update()
    time.sleep(2)
    game_intro()

def text_objects(text, font):
    Textsurface = font.render(text, True, black)
    return Textsurface, Textsurface.get_rect()

# --- Intro Menu ---
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
        Textrect.center = (display_width / 2, display_height / 4)
        gameDisplay.blit(Textsurface, Textrect)
        
        mouse = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        # Start button
        if display_width / 2 + 50 > mouse[0] > display_width / 2 - 50 and display_height / 4 + display_height / 12 + 50 > mouse[1] > display_height / 4 + display_height / 12:
            pygame.draw.rect(gameDisplay, bright_green, (display_width / 2 - 50, display_height / 4 + display_height / 12, 100, 50))
            pygame.draw.rect(gameDisplay, red, (display_width / 2 - 50, display_height / 4 + 2 * display_height / 12, 100, 50))
            if press[0] == 1:
                game_loop(None, 0)
        # Quit button
        elif display_width / 2 + 50 > mouse[0] > display_width / 2 - 50 and display_height / 4 + 2 * display_height / 12 + 50 > mouse[1] > display_height / 4 + (2 * display_height) / 12:
            pygame.draw.rect(gameDisplay, bright_red, (display_width / 2 - 50, display_height / 4 + 2 * display_height / 12, 100, 50))
            pygame.draw.rect(gameDisplay, green, (display_width / 2 - 50, display_height / 4 + display_height / 12, 100, 50))
            if press[0] == 1:
                pygame.quit()
        else:
            pygame.draw.rect(gameDisplay, green, (display_width / 2 - 50, display_height / 4 + display_height / 12, 100, 50))
            pygame.draw.rect(gameDisplay, red, (display_width / 2 - 50, display_height / 4 + 2 * display_height / 12, 100, 50))

        # Button labels
        smallText = pygame.font.Font('freesansbold.ttf', 20)
        Textsurface, Textrect = text_objects("Start", smallText)
        Textrect.center = (display_width / 2, display_height / 4 + display_height / 12 + 25)
        gameDisplay.blit(Textsurface, Textrect)

        Textsurface, Textrect = text_objects("Quit", smallText)
        Textrect.center = (display_width / 2, display_height / 4 + (2 * display_height) / 12 + 25)
        gameDisplay.blit(Textsurface, Textrect)

        pygame.display.update()
        clock.tick(15)

# --- In Game Shop ---

def store(Board, money):
    board = Board #pass input board into a new varable
    store = True
    while store:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        Textsurface, Textrect = text_objects("Store", largeText)
        Textrect.center = (display_width / 8, display_height / 12)
        gameDisplay.blit(Textsurface, Textrect)
        
        mouse = pygame.mouse.get_pos()
        press = pygame.mouse.get_pressed()

        pygame.display.update()
        clock.tick(15)



# --- Board Logic ---

def board_initialize():
    grid = [["empty" for i in range(8)] for j in range(6)]
    return grid

def draw_board(board):
    startx = display_width / 5  # Reserve space for UI
    starty = 0
    cell_width = ((display_width * 4) / 5) / len(board[0])
    cell_height = ((display_height * 3) / 4) / len(board)

    # Draw grid background and borders
    for row in range(len(board)):
        for col in range(len(board[0])):
            x = startx + (col * cell_width)
            y = starty + (row * cell_height)
            pygame.draw.rect(gameDisplay, white, (x, y, cell_width, cell_height))
            pygame.draw.rect(gameDisplay, black, (x, y, cell_width, cell_height), 1)

    draw_cells(board, startx, starty, cell_width, cell_height)

def draw_cells(board, startx, starty, cell_width, cell_height):
    for row in range(len(board)):
        for col in range(len(board[0])):
            tile = board[row][col]
            x = startx + (col * cell_width)
            y = starty + (row * cell_height)

            if tile == "filled":
                pygame.draw.rect(gameDisplay, blue, (x + 3, y + 3, cell_width - 6, cell_height - 6))

# --- Main Game Loop ---

def game_loop(Board, Money):
    gameexit = False
    if Board == None:
        board = board_initialize()
    money = Money

    while not gameexit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #begin to calculate what grid we are over
                mouse_x, mouse_y = pygame.mouse.get_pos()
                startx = display_width / 5
                starty = 0
                cell_width = ((display_width * 4) / 5) / len(board[0])
                cell_height = ((display_height * 3) / 4) / len(board)
                grid_x = int((mouse_x - startx) // cell_width)
                grid_y = int((mouse_y - starty) // cell_height)
                #done with grid location calculation

                if 0 <= grid_x < len(board[0]) and 0 <= grid_y < len(board): #placeholder function, for now it just swaps grid values between "empty" and "filled"
                    current = board[grid_y][grid_x]
                    if current == "empty":
                        board[grid_y][grid_x] = "filled"
                    else:
                        board[grid_y][grid_x] = "empty"


            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE: #reserved space for ending the turn
                    print('space pressed')

                if event.key == pygame.K_TAB: #start the store
                    store(board, money)

                if event.key == pygame.K_ESCAPE: #reserved space for in game options menu
                    print('esc key pressed')

        gameDisplay.fill(grey)
        draw_board(board)
        pygame.display.update()
        clock.tick(60)

# --- Start the game ---
game_intro()
game_loop()
