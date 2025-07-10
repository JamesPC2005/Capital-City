# READ ME

Hi there this is the beginning point of my solo-development project to create a game over the summer. I dont have much experecne in creating games so we will have to see how this goes.

## The basic idea of the game is as follows:
you are creating a city on a 2-d board game style board. you can use money to buy new properties and place them on the map, each property will help you generate more money in one way or another. at the end of each year you need to pay a certain ammount of taxes, the game ends when you fail to pay your taxes in a given year.

simple, right? well i guess we will have to see

## june 6 2025
Its my first day working on the project, ill let you know how it goes:
The first thing i did was create this readme file, and establish a github for the project.
After that I created a practace game called a bit racy following instructions from a tutorial. it turned out well but i still have much more to do.

## june 13 2025
Im back to working on the project, the tutorial is going over UI creations so lets see how i do.

I managed to get functional menu screen and start button, its going well. I think im ready to start developing Capitol City now

## july 10 2025
I ended up accidentally taking a break from the project but im back now.

Im trying to figure out how to make the board store and display values. the only way i can think of doing it is to turn every tile in the board into a buttor, but thats a pain so im going to look for something better.

after looking through a couple forums i think i found a good way to do it, im going to write a line by line explination for my future self here, im also going to try to make it look nice but i dont know if ill be able to, so please have paitence with me.  

```python

elif event.type == pygame.MOUSEBUTTONDOWN:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    #gets the mouse location
    startx = display_width / 5
    #accounts for the ui space on the right
    starty = 0
    #no need to account for y-start
    cell_width = ((display_width * 4) / 5) / len(board[0])
    #same calculation as elsewhere, should i make a global calculation/function?
    cell_height = ((display_height * 3) / 4) / len(board)
    #same as line above
    grid_x = int((mouse_x - startx) // cell_width)
    #takes how far x is from the start x and uses cell width to calculate the cell the mouse is in
    grid_y = int((mouse_y - starty) // cell_height)
    #same as above, but for y values

    if 0 <= grid_x < len(board[0]) and 0 <= grid_y < len(board):
        #this function will be remade later, currently swaps the grid between empty and full, use the cards to set a value for the mouse to carry and place that into the grid space.
        current = board[grid_y][grid_x]
        board[grid_y][grid_x] = "filled" if current == "empty" else "empty"
```
