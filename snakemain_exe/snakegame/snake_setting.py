import pygame
import random
class snake_set():
    def __init__(self):
        self.screen_width=500
        self.screen_height=500
        self.bg_color=(250,213,165)
class snake_body():
    def __init__(self):
        self.width=40
        self.height=40
        length=40
        head=pygame.image.load("snakegame/snake_head.png").convert_alpha()
        head_right=pygame.image.load("snakegame/snake_head_right.png").convert_alpha()
        head_left=pygame.image.load("snakegame/snake_head_left.png").convert_alpha()
        head_up=pygame.image.load("snakegame/snake_head_up.png").convert_alpha()
        self.rest_body=pygame.image.load("snakegame/square.jpg").convert_alpha()
        self.head=pygame.transform.scale(head,(self.width,self.height))
        self.head_right=pygame.transform.scale(head_right,(self.width,self.height))
        self.head_left=pygame.transform.scale(head_left,(self.width,self.height))
        self.head_up=pygame.transform.scale(head_up,(self.width,self.height))
        self.rest_body=pygame.transform.scale(self.rest_body,(self.width,self.height))
        


        self.x=0
        self.y=0
        self.x_velocity=10
        self.y_velocity=0
        self.length=40
    def draw(self,screen,snake_list,head):
        length=len(snake_list)
        for i in range(length):
            if i==length-1:
                screen.blit(head,snake_list[i])
            else:
                screen.blit(self.rest_body,snake_list[i])
                #pygame.draw.rect(screen,(47,72,62),(snake_list[i][0],snake_list[i][1],40,40))
            
class snake_food():
    def __init__(self,width,height):
        self.apple_width=width-5
        self.apple_height=height-5
        #images
        food_apple=pygame.image.load("snakegame/apple.png").convert_alpha()
        food_apple=pygame.transform.scale(food_apple,(self.apple_width,self.apple_height))
        self.image=food_apple
    def create_food(self,screen_width,screen_height):

        self.x=random.randint(0,screen_width-self.apple_width)
        self.y=random.randint(0,screen_height-self.apple_height)
        
    def show_food(self,screen):
        screen.blit(self.image,(self.x,self.y))
        




