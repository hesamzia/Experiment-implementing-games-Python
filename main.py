# Simple Snake Game in Python 3 for Beginners
import pygame
import time
import random
import config  # import config file

pygame.init()

# colors definition
#white = (255, 255, 255) # TODO (add to config file) define colors in config file
#yellow = (255, 255, 102)
#black = (0, 0, 0)
#red = (213, 50, 80)
#green = (0, 255, 0)
#blue = (50, 153, 213)

dis_width = 600 # TODO (add to config file)width of display window
dis_height  = 400 # height of display window

# set display window of game
dis = pygame.display.set_mode((dis_width,dis_height))

# set title of game window
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block=10 # TODO (add to config file) size of snake block
snake_speed=10 # TODO (add to config file) speed of snake

font_style = pygame.font.SysFont("bahnschrift", 25) # another font style and size
score_font = pygame.font.SysFont("comicsansms", 35)
 

def Your_score(score): # function to display score
    value = score_font.render("Your Score: " + str(score), True, config.SCORECOLORE)  # render the score
    dis.blit(value, [0, 0]) # display the score on screen
 

def our_snake(snake_block, snake_list): # function to display snake
    for x in snake_list:
        pygame.draw.rect(dis, config.SNAKECOLOR, [x[0], x[1], snake_block, snake_block]) # draw rectangle for snake


def message(msg,color): # function to display message on screen
    mesg = font_style.render(msg, True, color) # render the message
    mesg_rect = mesg.get_rect(center=(dis_width/2, dis_height/2)) # get rectangle of message
    dis.blit(mesg, mesg_rect) # display the message on screen
 


def gameLoop(): # main function of game
    game_over=False # game over flag
    game_close=False # game close flag

    x1 = dis_width/2  # initial position of snake on x axis
    y1 = dis_height/2
    
    x1_change = 0      # initial change in position
    y1_change = 0

    snake_List = [] # list to store position of snake
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # initial position of food on x axis
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 

    while not game_over: # main loop of game

        while game_close == True: # if game is over
            dis.fill(config.DISPLAYCOLOR) # fill the display with DISPLAYCOLOR color
            message("You Lost! Press Q-Quit or C-Play Again", config.MESSAGECOLOR)  # display message
            Your_score(Length_of_snake - 1) # display score
            pygame.display.update()

            for event in pygame.event.get():    # event handling
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:   # if q is pressed
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # if c is pressed
                        gameLoop()

        for event in pygame.event.get():   # event handling
            if event.type == pygame.QUIT:  # if window is closed
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # if left arrow is pressed
                    x1_change = -snake_block # change in position
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: # if snake hits the wall
            game_close = True
            
        x1 += x1_change             # update position of snake
        y1 += y1_change
        dis.fill(config.DISPLAYCOLOR) # fill display with DISPLAYCOLOR color

        pygame.draw.rect(dis, config.FOODCOLOR, [foodx, foody, snake_block, snake_block]) # draw food on screen
        snake_Head = [] # list to store position of snake head
        snake_Head.append(x1) # append x and y position of snake head
        snake_Head.append(y1)  
        snake_List.append(snake_Head) # append position of snake head to snake list
        if len(snake_List) > Length_of_snake: # if length of snake is greater than length of snake
            del snake_List[0] # delete the first element of snake list

        for x in snake_List[:-1]: # if snake hits itself
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)        # call function to display snake 
        Your_score(Length_of_snake - 1)           # call function to display score

        pygame.display.update()

        if x1 == foodx and y1 == foody: # if snake eats the food
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # initial position of food on x axis
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed) # set speed of game

    pygame.quit()
    quit()

gameLoop() # call the main function to start the game
