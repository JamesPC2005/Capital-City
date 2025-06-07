import pygame

# initalize pygame
pygame.init


# create a window
# make the window size varable in the future
gameDisplay = pygame.display.set_mode((800,600))

#set title of window
pygame.display.set_caption('A bit Racey')

#creates gameclock
clock = pygame.time.Clock()

#create main game loop
crash = False

while not crash:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: crash = True
        #the print statement shows all events
        print(event)
# update the screen
    pygame.display.update()
#set refresh rate
    clock.tick(60)

pygame.quit()
quit()