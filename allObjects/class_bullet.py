from pakage import *
import setting
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y): # need to parallel to player, so we add x and y 
        
        bullet_img=pygame.image.load(os.path.join("img","bullet.png")).convert()
        
        pygame.sprite.Sprite.__init__(self)
        # self.image=pygame.Surface((10,20)) # setting size 
        # self.image.fill(YELLOW) # setting color 
        self.image= bullet_img
        self.image.set_colorkey(setting.BLACK)
        self.rect= self.image.get_rect() # setting   position 
        self.rect.centerx= x   
        self.rect.bottom=y 
        self.speedy=-10  


    def update(self):
      self.rect.y += self.speedy
      if self.rect.bottom<0 :
          self.kill()
