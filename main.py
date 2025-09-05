# Simple Snake Game in Python 3 for Beginners
import pygame
import time
import random
import json
import os
import config  # import config file

def load_highscores(): 
    """Load highscores from file or return empty list."""
    if os.path.exists(config.HIGHSCORE_FILE):
        with open(config.HIGHSCORE_FILE, "r") as f:
            return json.load(f)
    return []


def save_highscores(scores):
    """Save highscores to file."""
    with open(config.HIGHSCORE_FILE, "w") as f:
        json.dump(scores, f)
    

def add_score(new_score, name):
    """Add a new score and keep only top 5."""
    scores = load_highscores()
    scores.append({"name": name, "score": new_score})
    # Sort descending by score
    scores = sorted(scores, key=lambda x: x["score"], reverse=True)
    # Keep only top 5
    scores = scores[:config.MAX_SCORES]
    save_highscores(scores)
    return


def check_highscore(score):
    """Check if score qualifies for top 5."""
    scores = load_highscores()
    if len(scores) < config.MAX_SCORES:
        return True
    return score > scores[-1]["score"]


def draw_highscores(dis, font):
    """Draw highscores on screen."""
    scores = load_highscores()
    y = 100
    dis.blit(font.render("High scores:", True, (255, 255, 0)), (50, y))
    y += 50
    for i, entry in enumerate(scores, start=1):
        text = f"{i}. {entry['name']} - {entry['score']}"
        dis.blit(font.render(text, True, (255, 255, 255)), (50, y))
        y += 40
    dis.blit(font.render("Press C to continue", True, (255, 255, 0)), (50, y))
    return


class TextInputBox:  # class to create text input box
    def __init__(self, x, y, w, h, font, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = text
        self.font = font
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.done = False  # True when player presses Enter

    def handle_event(self, event):  # function to handle events
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state if clicked inside box
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive

        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.done = True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < 12:  # limit name length
                        self.text += event.unicode
                self.txt_surface = self.font.render(self.text, True, (255, 255, 255))

    def update(self): 
        # Resize box if text is too long
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, dis):
        # Blit the text
        dis.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect
        pygame.draw.rect(dis, self.color, self.rect, 2)

####


def Your_score(score): # function to display score
    value = score_font.render("Your Score: " + str(score), True, config.SCORECOLORE)  # render the score
    dis.blit(value, [0, 0]) # display the score on screen
 

def our_snake(snake_list): # function to display snake
    for x in snake_list:
        pygame.draw.rect(dis, config.SNAKECOLOR, [x[0], x[1], config.SNAKE_BLOCK, config.SNAKE_BLOCK]) # draw rectangle for snake


def moving_rods_handel(list_of_moving_rods):
    if len(list_of_moving_rods) <= config.NO_OF_MOVING_RODS :
        add_moving_rod(list_of_moving_rods)
    for mv_rod in list_of_moving_rods:
        if mv_rod[0] == "DOWN" :
            mv_rod[2] += config.SNAKE_BLOCK  # move the moving rod down (Add 10 to y position)
            pygame.draw.rect(dis, config.OBSTACLECOLOR, [mv_rod[1],mv_rod[2],50,config.SNAKE_BLOCK]) 
        elif mv_rod[0] == "UP":
            mv_rod[2] -= config.SNAKE_BLOCK  # move the moving rod up (Subtract 10 to y position)
            pygame.draw.rect(dis, config.OBSTACLECOLOR, [mv_rod[1],mv_rod[2],50,config.SNAKE_BLOCK]) 
        elif mv_rod[0] == "LEFT":
            mv_rod[1] += config.SNAKE_BLOCK  # move the moving rod up (Subtract 10 to y position)
            pygame.draw.rect(dis, config.OBSTACLECOLOR, [mv_rod[1],mv_rod[2],config.SNAKE_BLOCK,50]) 
        elif mv_rod[0] == "RIGHT":
            pygame.draw.rect(dis, config.OBSTACLECOLOR, [mv_rod[1],mv_rod[2],config.SNAKE_BLOCK,50]) 
            mv_rod[1] -= config.SNAKE_BLOCK  # move the moving rod up (Subtract 10 to y position)
    
        if mv_rod[2] > config.DIS_HEIGHT or mv_rod[2] < 0 :  # if moving rod hits the wall (up or down)
            list_of_moving_rods.remove(mv_rod)  # remove the moving rod from the list (list_of_moving_rods) (remove mv_rod)
        if mv_rod[1] > config.DIS_WIDTH or mv_rod[1] < 0 :  # if moving rod hits the wall (left or right)
            list_of_moving_rods.remove(mv_rod)  # remove the moving rod from the list (list_of_moving_rods) (remove mv_rod)
    return 


def add_moving_rod(list_of_moving_rods):
    if len(list_of_moving_rods) >= config.NO_OF_MOVING_RODS :
        return
    choose = random.randint(0, 3)
    if choose == 0 :
        list_of_moving_rods.append(["DOWN", random.randint(0, config.DIS_WIDTH - 50), 0])
    elif choose == 1 :
        list_of_moving_rods.append(["UP", random.randint(0, config.DIS_WIDTH - 50), config.DIS_HEIGHT])
    elif choose == 2 :
        list_of_moving_rods.append(["RIGHT", config.DIS_WIDTH - 50, random.randint(0, config.DIS_HEIGHT - 10)])
    elif choose == 3 :
        list_of_moving_rods.append(["LEFT", 0, random.randint(0, config.DIS_HEIGHT - 10)])
    return


def hit_moving_rod(list_of_moving_rods, snake_List, snake_Head):
    for mv_rod in list_of_moving_rods:
        if mv_rod[0] == "DOWN" or mv_rod[0] == "UP":
            if snake_Head[1] in range(mv_rod[2] - 10, mv_rod[2] + 10) and snake_Head[0] in range(mv_rod[1], mv_rod[1] + 50):  # if snake's head hits moving rod
                return True
            for x in snake_List[:-1]:
                if x[1] == mv_rod[2] and x[0] in range(mv_rod[1], mv_rod[1] + 50):  # if snake's body hits moving rod
                    return True
        else :
            if snake_Head[0] in range(mv_rod[1] - 10, mv_rod[1] + 10) and snake_Head[1] in range(mv_rod[2], mv_rod[2] + 50):  # if snake's head hits moving rod
                return True
            for x in snake_List[:-1]:
                if x[0] == mv_rod[1] and x[1] in range(mv_rod[2], mv_rod[2] + 50):  # if snake's body hits moving rod
                    return True

    return False


def message(msg,color): # function to display message on screen
    mesg = font_style.render(msg, True, color) # render the message
    mesg_rect = mesg.get_rect(center=(config.DIS_WIDTH/2, config.DIS_HEIGHT/2)) # get rectangle of message
    dis.blit(mesg, mesg_rect) # display the message on screen
 


def gameLoop(): # main function of game
    list_of_moving_rods = []

    # for input box
    waiting_for_name = True
    wating_for_highscore = True

    game_over=False # game over flag
    game_close=False # game close flag

    x1 = config.DIS_WIDTH/2  # initial position of snake on x axis
    y1 = config.DIS_HEIGHT/2
    
    x1_change = 0      # initial change in position
    y1_change = 0

    snake_List = [] # list to store position of snake
    Length_of_snake = 1

    foodx = round(random.randrange(0, config.DIS_WIDTH - config.SNAKE_BLOCK) / 10.0) * 10.0 # initial position of food on x axis
    foody = round(random.randrange(0, config.DIS_HEIGHT - config.SNAKE_BLOCK) / 10.0) * 10.0
    while not game_over: # main loop of game

        while game_close == True: # if game is over
            if check_highscore(Length_of_snake - 1):
                # Normally you'd build an input box here
#                name = input("New Highscore! Enter your name: ")
                while waiting_for_name:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            waiting_for_name = False
                        input_box.handle_event(event)

                    input_box.update()

                    dis.fill((30, 30, 30))
                    msg = font.render(f"New High score! Score: {Length_of_snake - 1}", True, (255, 255, 0))
                    dis.blit(msg, (100, 100))

                    input_box.draw(dis)

                    pygame.display.flip()
                    clock.tick(30)

                    # When player presses Enter
                    if input_box.done:
                        name = input_box.text if input_box.text.strip() else "Player"
#                        print(f"Saving score: {name} - {Length_of_snake - 1}")
                        waiting_for_name = False
                        add_score(Length_of_snake - 1, name)
                while wating_for_highscore:
                    dis.fill(config.DISPLAYCOLOR)
                    draw_highscores(dis, font)
                    pygame.display.update()
                    for event in pygame.event.get():    # event handling
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_c:   # if q is pressed
                                wating_for_highscore = False
                                waiting_for_name = False
            
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

#!!!!
        for event in pygame.event.get():   # event handling
            if event.type == pygame.QUIT:  # if window is closed
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # if left arrow is pressed
                    x1_change = -config.SNAKE_BLOCK # change in position
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = config.SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -config.SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = config.SNAKE_BLOCK
                    x1_change = 0

        if x1 >= config.DIS_WIDTH or x1 < 0 or y1 >= config.DIS_HEIGHT or y1 < 0: # if snake hits the wall
            game_close = True
            
        x1 += x1_change             # update position of snake
        y1 += y1_change
        dis.fill(config.DISPLAYCOLOR) # fill display with DISPLAYCOLOR color

        pygame.draw.rect(dis, config.FOODCOLOR, [foodx, foody, config.SNAKE_BLOCK, config.SNAKE_BLOCK]) # draw food on screen
        snake_Head = [] # list to store position of snake head
        snake_Head.append(x1) # append x and y position of snake head
        snake_Head.append(y1)  
        snake_List.append(snake_Head) # append position of snake head to snake list
        if len(snake_List) > Length_of_snake: # if length of snake is greater than length of snake
            del snake_List[0] # delete the first element of snake list

        for x in snake_List[:-1]: # if snake hits itself
            if x == snake_Head:
                game_close = True


        our_snake(snake_List)        # call function to display snake 
        Your_score(Length_of_snake - 1)           # call function to display score


        # handel moving rods 
        moving_rods_handel(list_of_moving_rods)


        # if hit moving rod game will close
        if hit_moving_rod(list_of_moving_rods, snake_List, snake_Head):
            game_close = True


        pygame.display.update()

        if x1 == foodx and y1 == foody: # if snake eats the food
            foodx = round(random.randrange(0, config.DIS_WIDTH - config.SNAKE_BLOCK) / 10.0) * 10.0 # initial position of food on x axis
            foody = round(random.randrange(0, config.DIS_HEIGHT - config.SNAKE_BLOCK) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(config.SNAKE_SPEED) # set speed of game

    pygame.quit()
    quit()

pygame.init()

# set display window of game
dis = pygame.display.set_mode((config.DIS_WIDTH, config.DIS_HEIGHT))

# set title of game window
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()


font_style = pygame.font.SysFont("bahnschrift", 25) # another font style and size
score_font = pygame.font.SysFont("comicsansms", 35)
font = pygame.font.SysFont(None, 40) # highscore font

# create text input box
input_box = TextInputBox(200, 200, 200, 50, font)
#player_score = 123  # Example score

 
gameLoop() # call the main function to start the game
