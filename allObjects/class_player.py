

from allObjects.class_bullet import Bullet
# from allObjects import class_bullet
from pakage import *
import setting



class Player(pygame.sprite.Sprite):
    def __init__(self,all_sprites,bullets,shoot_sound): #類別要使用的實際參數 直接當變數引入就好
        self.shoot_sound=shoot_sound
        self.bullets=bullets
        self.all_sprites=all_sprites
        
        player_img=pygame.image.load(os.path.join("img","player.png")).convert()
        
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(player_img,(50,38))
        self.image.set_colorkey(setting.BLACK) #把圖片的黑色部分變成透明（去背）
        self.radius=20
        self.rect= self.image.get_rect() # setting   position 
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius) # this code sohuld below the "setting position code"
   
        self.rect.centerx=setting.WIDTH/2  # setting the initial position 
        self.rect.bottom=setting.HEIGHT-10
        self.speedx=8 
        self.health=100
        self.lives=3 # the life of the plane 
        self.hidden= False
        self.hide_time=0  
        
        self.gun=1  # the bullet that the player have  
        self.gun_time= 0  # record the time that you eat the power of gun 

    def update(self):   
        now=pygame.time.get_ticks() 
        if self.gun >1 and now - self.gun_time>5000: 
            self.gun-=1  
            self.gun_time=now 
        
        if self.hidden and now - self.hide_time>1000:
            self.hidden=False 
            self.rect.centerx=setting.WIDTH/2  # return the the original position 
            self.rect.bottom=setting.HEIGHT-10
       
                    
        
        key_pressd =pygame.key.get_pressed() # get all keyboard boolen which is array  
        if key_pressd[pygame.K_d]:
            self.rect.x += self.speedx
        
        if key_pressd[pygame.K_a]:
            self.rect.x -= self.speedx
        
        if self.rect.right>setting.WIDTH:
            self.rect.right = setting.WIDTH 
        if self.rect.left <0:
            self.rect.left=0 

    
    def shoot(self):
        if not(self.hidden):
            if self.gun==1 :   
                bullet=Bullet(self.rect.centerx,self.rect.top)
                self.all_sprites.add(bullet) # this all_sprties group will show on screen 
                self.bullets.add(bullet)
                self.shoot_sound.play() # the sound will play when the function be called 
            
            elif self.gun >=2 : 
                bullet1=Bullet(self.rect.left,self.rect.centery)
                bullet2=Bullet(self.rect.right,self.rect.centery)
                
                self.all_sprites.add(bullet1) # this all_sprties group will show on screen 
                self.all_sprites.add(bullet2) # this all_sprties group will show on screen 
                self.bullets.add(bullet1)
                
                self.bullets.add(bullet2)
                self.shoot_sound.play() 
    def hide(self):
        self.hidden=True
        self.hide_time=pygame.time.get_ticks() #get time 
        self.rect.center=(setting.WIDTH/2,setting.HEIGHT+500) #== 讓你看不見就是消失
        
    def gunup(self):
        self.gun+=1
        self.gun_time= pygame.time.get_ticks()
    