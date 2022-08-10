## The file contains all function in the game. 
#-----------------------------------------------

from tkinter import font
from pakage import *
import setting 
import pygame


def draw_text(surf,text,size,x,y,font_name):
    font=pygame.font.Font(font_name,size)# create word object 
    text_surface=font.render(text,True,setting.WHITE) # render the object 
    text_rect =text_surface.get_rect()
    text_rect.centerx=x  
    text_rect.top=y 
    surf.blit(text_surface,text_rect) # build text on what and where



def new_rock(rock_imgs,all_sprites,rocks):
    r=ROCK(rock_imgs)
    all_sprites.add(r) # if we collision we will create new rock to you 
    rocks.add(r)

# create hp line bar 

def draw_health(surf,hp,x,y):
    if hp <0 :
        hp=0 
    BAR_LENGTH=100 # the length of hp line 
    BAR_HEIGHT=10
    fill=(hp/100)*BAR_LENGTH
    outline_rect=pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT) # the outline setting 
    fill_rect=pygame.Rect(x,y,fill,BAR_HEIGHT) # the inline setting 
    pygame.draw.rect(surf,setting.GREEN,fill_rect) #draw the inline 
    pygame.draw.rect(surf,setting.WHITE,outline_rect,2)
    
    
def draw_lives(surf,lives,img,x,y):
    for i in range(lives):
        img_rect=img.get_rect() # get the image original position 
        img_rect.x=x+30*i  # setting the image position we want 
        img_rect.y=y 
        surf.blit(img, img_rect)
        


def draw_init(screen,clock,font_name,background_img):
    screen.blit(background_img,(0,0))
    draw_text(screen,"捍衛戰士",64, setting.WIDTH/2 , setting.HEIGHT/4,font_name)
    draw_text(screen,"A D 移動戰機 空白鍵發射飛彈",22, setting.WIDTH/2,setting.HEIGHT/2,font_name)
    draw_text(screen,"按任意鍵開始遊戲",18, setting.WIDTH/2,setting.HEIGHT*3/4,font_name)
    
    pygame.display.update()
    watting =True 
    while watting : 
        clock.tick(setting.FPS) # 每秒此loop跑幾次= loop 60  次 =遊戲畫面更新率
        #取得輸入
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                return False 
            elif event.type==pygame.KEYUP:
                watting=False
                return True 
                
    
    
    