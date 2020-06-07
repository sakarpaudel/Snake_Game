#SARCASTIC SNAKE SAKARU
import pygame,os
import time
import random
print("Hello World! I miss you")
pygame.init()
pygame.mixer.init()
os.getcwd()
#Color Configuration
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
grey= (192,192,192)

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, "images")

file_dir = os.path.split(os.path.abspath(__file__))[0]
music_path = os.path.join(file_dir, "musics")

dis_width = 800
dis_height = 600
border_color= red
border_width=20
#configure snake size 
snake_block = 20
snake_speed = 5
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake')

#Text and font manage
font_style = pygame.font.SysFont('freesansbold.ttf',25)
score_font = pygame.font.SysFont("comicsansms", 35)
menu_font = pygame.font.SysFont("comicsansms", 30)
#image transform
ratImg = pygame.image.load(os.path.join(main_dir, 'rat.png'))
ratImg =  pygame.transform.scale(ratImg, (snake_block, snake_block))

snakeImg = pygame.image.load(os.path.join(main_dir, 'snake.png'))
snakeImg =  pygame.transform.scale(snakeImg, (snake_block, snake_block))

menuImg = pygame.image.load(os.path.join(main_dir, 'main_menu.jpg'))
menuImg =  pygame.transform.scale(menuImg, (dis_width, dis_height))

pauseImg = pygame.image.load(os.path.join(main_dir, 'pause_menu.jpg'))
pauseImg =  pygame.transform.scale(pauseImg,(dis_width, dis_height))

rulesImg = pygame.image.load(os.path.join(main_dir, 'game_rules.jpg'))
rulesImg =  pygame.transform.scale(rulesImg,(dis_width, dis_height))

aboutImg = pygame.image.load(os.path.join(main_dir, 'about_snake.jpg'))
aboutImg =  pygame.transform.scale(aboutImg,(dis_width, dis_height))

overImg = pygame.image.load(os.path.join(main_dir, 'game_over.jpg'))
overImg =  pygame.transform.scale(overImg,(dis_width, dis_height))
#Sound Configuration
crash_sound=  pygame.mixer.Sound(os.path.join(file_dir, "crash.wav"))
gulp_sound=  pygame.mixer.Sound(os.path.join(file_dir, "gulp.wav"))
explode_sound=  pygame.mixer.Sound(os.path.join(file_dir, "explode.wav"))
confirm_sound=  pygame.mixer.Sound(os.path.join(file_dir, "confirm.wav"))

def game_intro():
    intro=True
    pygame.mixer.music.load(os.path.join(file_dir, "intromusic.mp3"))
    pygame.mixer.music.play()
    while intro:
        pygame.display.update()
        dis.blit(menuImg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    gameLoop()
                if event.key == pygame.K_r:
                    rules()
                if event.key == pygame.K_a:
                    about()
def about():
    confirm_sound.play()
    while True:
        dis.blit(aboutImg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    confirm_sound.play()
                    game_intro()
                if event.key == pygame.K_SPACE:
                    gameLoop()
        pygame.display.update()
def over(length):
    while True:
        dis.blit(overImg,(0,0))
        Your_score(length - 1)
        high_score(length-1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or pygame.K_SPACE:
                    confirm_sound.play()
                    game_intro()
                if event.key == pygame.K_q:
                    quit()
        pygame.display.update()
def rules():
    confirm_sound.play()
    rules=True
    while rules:
        dis.blit(rulesImg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    confirm_sound.play()
                    game_intro()
                if event.key == pygame.K_SPACE or pygame.k_C:
                    rules= False
                    pause= False
                if event.key == pygame.K_a:
                    about()
        pygame.display.update()
                    
def pause():
    confirm_sound.play()
    pygame.mixer.music.load(os.path.join(file_dir, "intromusic.mp3"))
    pygame.mixer.music.play()
    paused= True
    while paused:
        dis.blit(pauseImg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    confirm_sound.play()
                    game_intro()
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.stop()
                    gameLoop()
                if event.key == pygame.K_c:
                    pygame.mixer.music.stop()
                    paused = False
                if event.key == pygame.K_r:
                    pygame.mixer.music.stop()
                    rules()
        pygame.display.update()
                    
 #Display The scores
def get_high_score():
    # Default high score
    high_score = 0
 
    # Try to read the high score from a file
    try:
        high_score_file = open("high_score.txt", "r")
        high_score = int(high_score_file.read())
        high_score_file.close()
        #print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")
 
    return high_score

def save_high_score(new_high_score):
    try:
        # Write the file to disk
        high_score_file = open("high_score.txt", "w")
        high_score_file.write(str(new_high_score))
        high_score_file.close()
    except IOError:
        # can't write it.
        print("Unable to save the high score.")
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [20, 10])

def high_score(score):
    highscore = get_high_score()
    #highscore=0
    if(score>highscore):
        highscore+=1
        value = score_font.render("High-Score: " + str(score), True, green)
        dis.blit(value, [20,45])
        save_high_score(score)
    else:
        value = score_font.render("High-Score: " + str(highscore), True, green)
        dis.blit(value, [20,45])
#Snake body description
def our_snake(snake_block, snake_list):
    for x in snake_list:
        dis.blit(snakeImg,([x[0], x[1]]))
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 4, dis_height / 2])
def info(msg,color):
    mesg = menu_font.render(msg, True, color)
    dis.blit(mesg, [dis_width / 4, dis_height / 2])
def border():
        #print("drawing border")
        pygame.display.update()
        dis.fill(blue)
    # top line
        pygame.draw.rect(dis, border_color, [0,0,dis_width,border_width])
    # bottom line
        pygame.draw.rect(dis, border_color, [0,dis_height-snake_block,dis_width,border_width])
    # left line
        pygame.draw.rect(dis, border_color, [0,0,border_width, dis_height])
    # right line
        pygame.draw.rect(dis, border_color, [dis_width-border_width,0,dis_width,dis_height])
 
 #Main game loop
def gameLoop():
    confirm_sound.play()
    pygame.mixer.music.load(os.path.join(file_dir, "music.mp3"))
    pygame.mixer.music.play()
    game_close = False
    game_over = False
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0

    clock = pygame.time.Clock()
 
    snake_List = []
    length = 1
    #Randomize first food generation
    foodx = round(random.randrange(border_width,dis_width-snake_block-snake_block) /snake_block) * snake_block
    foody = round(random.randrange(border_width, dis_height-snake_block-border_width) / snake_block) *snake_block
    while not game_over:
        border()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_close = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p :
                    pygame.mixer.music.stop()
                    pause()
                    pygame.mixer.music.load(os.path.join(file_dir, "music.mp3"))
                    pygame.mixer.music.play()
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                if event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
            #Going out of screen
        if x1 >= dis_width-snake_block or x1 < snake_block or y1 >= dis_height-snake_block or y1 < snake_block:
            #game_over = True
            print("went out of screen")
            pygame.mixer.music.stop()
            explode_sound.play()
            over(length)
        x1 += x1_change
        y1 += y1_change
        #food draw
        #print("Food  at",foodx,foody)
        dis.blit(ratImg,(foodx,foody))
        #Grow the snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

    #maintain length
        if len(snake_List) > length+1:
            del snake_List[0]
        #Eating own tail
        for x in snake_List[:-2]:
            if x == snake_Head:
                pygame.mixer.music.stop()
                crash_sound.play()
                print("Tail Eaten")
                over(length)
       
    #Score counting
        our_snake(snake_block, snake_List)
        Your_score(length - 1)
        high_score(length-1)
 
        pygame.display.update()
    #eating foood
        if x1 == foodx and y1 == foody:
            gulp_sound.play()
            #Food regeneration after eaten
            foodx = round(random.randrange(border_width,dis_width-snake_block-snake_block) /snake_block) * snake_block
            foody = round(random.randrange(border_width, dis_height-snake_block-border_width) / snake_block) *snake_block
            length += 1
            print("Food eaten!")
        clock.tick(length+2)
        #clock.tick(snake_speed)
    pygame.quit()
    quit()
game_intro()