

from pakage import *
import setting

class ROCK(pygame.sprite.Sprite):
    def __init__(self,rock_imgs):
        pygame.sprite.Sprite.__init__(self)
        
        self.rock_imgs=rock_imgs
        self.image_ori=random.choice(self.rock_imgs)
        # self.image=pygame.Surface((30,40)) # setting size 
        # self.image.fill(RED) # setting color 
        self.image_ori.set_colorkey(setting.BLACK)
        self.image=self.image_ori.copy()
        
         
        self.rect= self.image.get_rect() # setting   position 
        self.radius=int(self.rect.width*0.85/2)
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.x=random.randrange(0,setting.WIDTH-self.rect.width) # rock itself width 
        self.rect.y=random.randrange(-180,-100) #where is out of window
        self.speedy= random.randrange(2,10)
        self.speedx= random.randrange(-3,3) # so rock cna go right or left 
        self.radius=self.rect.width/2
        self.total_degree=0
        self.rot_degree  =random.randrange(-3,3)
   
    def update(self):# update all the element in the function 
        self.rotate()
        self.rect.y += self.speedy
        self.rect.x+=self.speedx
         
        if self.rect.top>setting.HEIGHT or self.rect.left>setting.WIDTH or self.rect.right<0:
                self.rect.x=random.randrange(0,setting.WIDTH-self.rect.width) # rock itself width 
                self.rect.y=random.randrange(-100,-40) #where is out of window
                self.speedy= random.randrange(2,10)
                self.speedx= random.randrange(-3,3) # so rock cna go right or left 
        
    def rotate(self):
        self.total_degree+=self.rot_degree # make sure the image wouldn't rotate over 360 degree 
        self.total_degree = self.total_degree%360 
        
        self.image=pygame.transform.rotate(self.image_ori, self.total_degree)
        
        center=self.rect.center # save the original image center to virable(stored the trajectory line )
        self.rect=self.image.get_rect() # reposition the object, if we don't do that, the object will be vibration
        self.rect.center=center   # set the center be same as originale center(follow the trajectory line )
         
        

