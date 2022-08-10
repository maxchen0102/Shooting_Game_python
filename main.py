# This is main excute program, we have to run this file 

from asyncio import shield
from module import draw_init
from pakage import *
from setting import HEIGHT, WIDTH # import all file in this 


# setting the player object 

# Game 初始化
# 遊戲視窗
pygame.init()
pygame.mixer.init() # initialize sound module 

screen=pygame.display.set_mode((setting.WIDTH,setting.HEIGHT))
pygame.display.set_caption("第一個遊戲")

clock= pygame.time.Clock()

# loading picture 
background_img=pygame.image.load(os.path.join("img","background.jpg")).convert()
## using transform to tranform proper background image to the game screen 
background_img=pygame.transform.scale(background_img,(WIDTH*2,HEIGHT))

player_img=pygame.image.load(os.path.join("img","player.png")).convert()
#rock_img=pygame.image.load(os.path.join("img","rock.png")).convert()
bullet_img=pygame.image.load(os.path.join("img","bullet.png")).convert()

player_mini_img=pygame.transform.scale(player_img,(25,19))
player_mini_img.set_colorkey(setting.BLACK)

rock_imgs =[]
for i in range(7):
    rock_imgs.append(pygame.image.load(os.path.join("img",f"rock{i}.png")).convert())


#loading the explode image 
expl_anim={}
expl_anim['lg']=[]
expl_anim['sm']=[]
expl_anim['player']=[]
for i in range(9): 
    expl_img=pygame.image.load(os.path.join("img",f"expl{i}.png")).convert()
    expl_img.set_colorkey(setting.BLACK ) 
    expl_anim['lg'].append(pygame.transform.scale(expl_img,(75,75)))
    expl_anim['sm'].append(pygame.transform.scale(expl_img,(30 ,30)))
    # player explosion loading 
    player_expl_img=pygame.image.load(os.path.join("img",f"player_expl{i}.png")).convert()
    player_expl_img.set_colorkey(setting.BLACK ) 
    expl_anim['player'].append(player_expl_img)
    

power_imgs={}
power_imgs['shield']=pygame.image.load(os.path.join("img","shield.png")).convert()
power_imgs['gun']=pygame.image.load(os.path.join("img","gun.png")).convert()


#loading the music 
shoot_sound=pygame.mixer.Sound(os.path.join("sound","shoot.wav"))
die_sound=pygame.mixer.Sound(os.path.join("sound","rumble.ogg"))

shield_sound=pygame.mixer.Sound(os.path.join("sound","pow0.wav"))
gun_sound=pygame.mixer.Sound(os.path.join("sound","pow1.wav"))


# following code can allow us random chose sound 
expls_sounds=[
    pygame.mixer.Sound(os.path.join("sound","expl0.wav")),
    pygame.mixer.Sound(os.path.join("sound","expl1.wav"))
]


    




# import background music 
pygame.mixer.music.load(os.path.join("sound","background.ogg"))
pygame.mixer.music.set_volume(0.4)


font_name= os.path.join("font.ttf")







pygame.mixer.music.play(-1)

#遊戲迴圈 

show_init=True
all_sprites =pygame.sprite.Group()# update group,(all object in the group will update follow the FPS rate )
rocks =pygame.sprite.Group()
bullets =pygame.sprite.Group()
powers= pygame.sprite.Group()
player=Player(all_sprites,bullets,shoot_sound)
all_sprites.add(player)

# create a new class object 
for i in range(8):
    module.new_rock(rock_imgs,all_sprites,rocks)
score=0  
        

running=True 
while running:
    clock.tick(setting.FPS) # 每秒此loop跑幾次= loop 60  次 =遊戲畫面更新率
       #取得輸入
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            
        elif event.type==pygame.KEYDOWN:
            
            if event.key==pygame.K_SPACE:
                player.shoot() # the function is in class player 
        #update the game screen 
    all_sprites.update()  # 每秒會更新60次畫面 
    



    
    
    # when the rocks and bullets collision 
    hits= pygame.sprite.groupcollide(rocks,bullets,TRUE,TRUE) # this funciton is using to detect collision 
    for hit in hits:
        random.choice(expls_sounds).play()
        score+= hit.radius  
        expl=Explosoin(hit.rect.center,'lg',expl_anim)
        all_sprites.add(expl)
        
        # determine when the power will show up 
        if random.random()>setting.POWER_RATE :
            pow =Power(hit.rect.center,power_imgs)
            all_sprites.add(pow) # add to this to show up main screen 
            powers.add(pow)
             
         
        module.new_rock(rock_imgs,all_sprites,rocks)
        
    
    # we should give player and rock radius atrribute 
    # detect whether the rock and player collide 
    
    hits=pygame.sprite.spritecollide(player,rocks,True,pygame.sprite.collide_circle) # the function is use circle detection
    for hit in hits :
        module.new_rock(rock_imgs,all_sprites,rocks)
        player.health-=hit.radius 
        expl=Explosoin(hit.rect.center,'sm',expl_anim) 
        all_sprites.add(expl) # add to animation  
        if player.health<=0 :
            
            death_expl=Explosoin(player.rect.center,'player',expl_anim) # create new explosion animation 
            all_sprites.add(death_expl)
            
            die_sound.play()# play the die sound 
            player.lives-=1 
            player.health=100
            player.hide() 
            print("YOU DIE....")
     
    if player.lives==0 and not (death_expl.alive()):
        running=False
        print("Game over ....")
    
    
    # determine the collision of power and player 
    hits=pygame.sprite.spritecollide(player,powers,True)
    for hit in hits : 
        if hit.type=='shield':
            shield_sound.play() # play the music when player eat the shield 
            player.health+=20
            if player.health>=100:
                player.health=100 
                
        elif hit.type=='gun':
            gun_sound.play()
            player.gunup()
    
    #畫面更新顯示 
    screen.fill(setting.BLACK)
    screen.blit(background_img,(0,0)) # fill the screen the background 
    all_sprites.draw(screen) # draw the object group in our screen 
    
    module.draw_text(screen,str(score),18,setting.WIDTH/2,10,font_name)
    module.draw_health(screen,player.health,5,15)
    module.draw_lives(screen,player.lives,player_mini_img,WIDTH-100,15)
    pygame.display.update()