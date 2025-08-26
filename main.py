import pygame
pygame.init()

# colors definition
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# set display window of game
dis=pygame.display.set_mode((800,600))

# set title of game window
pygame.display.set_caption('Snake Game')


game_over=False # game over flag

x1 = 300 # initial position of snake
y1 = 300
 
x1_change = 0      # initial change in position
y1_change = 0

clock = pygame.time.Clock() # to control speed of snake
 
while not game_over: # main loop of game
    for event in pygame.event.get(): # event handling loop
       if event.type==pygame.QUIT:
            game_over=True
    if event.type == pygame.KEYDOWN: # if key is pressed
        if event.key == pygame.K_LEFT: # if left arrow key is pressed
            x1_change = -10
            y1_change = 0
        elif event.key == pygame.K_RIGHT: # if right arrow key is pressed
            x1_change = 10
            y1_change = 0
        elif event.key == pygame.K_UP: # if up arrow key is pressed
            y1_change = -10
            x1_change = 0
        elif event.key == pygame.K_DOWN:  # if down arrow key is pressed
            y1_change = 10
            x1_change = 0            
    x1 += x1_change             # update position of snake
    y1 += y1_change
    dis.fill(white)          # fill display with white color
    pygame.draw.rect(dis, black, [x1, y1, 10, 10]) # draw snake
    
    clock.tick(30)        # control speed of snake

    pygame.display.update()   # update display
pygame.quit()
quit()

