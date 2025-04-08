import pygame
import sys
from snake_setting import snake_set
from snake_setting import snake_body,snake_food
def welcome():
    pygame.display.set_caption('snake game')
    settings=snake_set()
    wel_screen=pygame.display.set_mode((settings.screen_width,settings.screen_height+60))
    bg_image=pygame.image.load("snakegame/main_background.png").convert_alpha()
    bg_image==pygame.transform.scale(bg_image,(settings.screen_width,settings.screen_height+60))
   
    while True:
        #wel_screen.fill((0,255,255))
        wel_screen.blit(bg_image,(0,0))
        for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        start_game()
        pygame.display.flip()
        
        


def start_game():
    pygame.display.set_caption("snake game")
    settings=snake_set()
    screen=pygame.display.set_mode((settings.screen_width,settings.screen_height+60))
    snake=snake_body()
    pygame.init()
    s_head=snake.head_right
    snake_list=[]
    snake_length=1
    clock=pygame.time.Clock()
    fps=12
    score=0
    up_key=False
    down_key=False
    right_key=False
    left_key=False
    sound_no=True
    food=snake_food(snake.width,snake.height)
    food.create_food(settings.screen_width,settings.screen_height)
    vel_increase=10
    game_over=False
    def play_sound(sound):
        pygame.mixer.init()
        pygame.mixer.music.load(sound)
        pygame.mixer.music.play()

    def print_score(score,screen,highscore):
        font=pygame.font.SysFont("gabriola",45)
        text="Score :"+str(score)+"    Highscore :"+str(highscore)
        score_img=font.render(text,True,(0,0,0))
        screen.blit(score_img,(10,settings.screen_height+4))
    def print_text(screen,text,color,dimensions,size):
        font=pygame.font.SysFont("gabriola",size)
        text_img=font.render(text,True,color)
        screen.blit(text_img,dimensions)
    with open("snakegame/highscore.txt","r") as f:
        highscore=f.read()

    while True:
        screen.fill(settings.bg_color)
        food.show_food(screen)
        snake.draw(screen,snake_list,s_head)
        
        print_score(score,screen,highscore)
        if game_over==True:
            #play_sound("snakegame/TZRM68V-game-over.mp3")

            with open("snakegame/highscore.txt","w") as f:
                f.write(str(highscore))
            write="Game Over!!!"
            print_text(screen,write,(255,36,0),(80,50),70)
            write="press enter to restart"
            print_text(screen,write,(0,0,139),(70,settings.screen_height/2),50)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        start_game()

        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                elif event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT and left_key==False:
                        s_head=snake.head_right
                        snake.x_velocity=vel_increase
                        snake.y_velocity=0
                        right_key=True
                        up_key=False
                        down_key=False
                    if event.key==pygame.K_LEFT and right_key==False:
                        snake.x_velocity=-(vel_increase)
                        snake.y_velocity=0
                        s_head=snake.head_left
                        left_key=True
                        up_key=False
                        down_key=False
                    if event.key==pygame.K_UP and down_key==False :
                        snake.x_velocity=0
                        snake.y_velocity=-(vel_increase)
                        s_head=snake.head_up
                        up_key=True
                        right_key=False
                        left_key=False
                    if event.key==pygame.K_DOWN and up_key==False :
                        snake.x_velocity=0
                        snake.y_velocity=vel_increase
                        s_head=snake.head
                        down_key=True
                        right_key=False
                        left_key=False

            snake.x=snake.x+snake.x_velocity
            snake.y=snake.y+snake.y_velocity
            if abs(snake.x-food.x)<35 and abs(snake.y-food.y)<35:
                play_sound("snakegame/eat_sound.mp3")
                score=score+10
                if score>int(highscore):
                    highscore=score
                    if sound_no==True:
                        play_sound("snakegame/high_score_sound.mp3")
                        sound_no=False
                food.create_food(settings.screen_width,settings.screen_height)
                vel_increase+=1
                snake_length=snake_length+1
            head=[snake.x,snake.y]
            snake_list.append(head)
            if len(snake_list)>snake_length:
                del snake_list[0]
            if snake.x<0 or snake.x>settings.screen_width-snake.width or snake.y<0 or snake.y>settings.screen_height-snake.height:
                #print("game over")
                game_over=True
                play_sound("snakegame\game_over_sound.mp3")
            if head in snake_list[:-1]:
                game_over=True
                play_sound("snakegame\game_over_sound.mp3")
        
        pygame.draw.line(screen,(255,0,255),(0,settings.screen_height),(settings.screen_width,settings.screen_height),width=4)
        #screen.blit(head,(snake.x,snake.y))
        #print(snake_list)
        
        
        pygame.display.flip()
        clock.tick(fps)

welcome()



 