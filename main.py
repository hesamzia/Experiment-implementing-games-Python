import pygame
import time

pygame.init()

# colors definition
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis_width = 800 # TODO (add to config file)width of display window
dis_height  = 600 # height of display window

# set display window of game
dis=pygame.display.set_mode((dis_width,dis_height))

# set title of game window
pygame.display.set_caption('Snake Game')


game_over=False # game over flag

x1 = dis_width/2  # initial position of snake on x axis
y1 = dis_height/2
 
x1_change = 0      # initial change in position
y1_change = 0

clock = pygame.time.Clock() # to control speed of snake

snake_speed=30 # TODO (add to config file) speed of snake

font_style = pygame.font.SysFont(None, 50) #  font style and size


def message(msg,color): # function to display message on screen
    mesg = font_style.render(msg, True, color) # render the message
    mesg_rect = mesg.get_rect(center=(dis_width/2, dis_height/2)) # get rectangle of message
    dis.blit(mesg, mesg_rect) # display the message on screen
 
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

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
        
    x1 += x1_change             # update position of snake
    y1 += y1_change
    dis.fill(white)          # fill display with white color
    pygame.draw.rect(dis, black, [x1, y1, 10, 10]) # draw snake
    
    pygame.display.update()   # update display

    clock.tick(snake_speed)        # control speed of snake
    
message("You lost",red)
pygame.display.update() # display message on screen for 2 seconds and then quit game 
time.sleep(2) 
pygame.quit()
quit()

