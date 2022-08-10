  
  
from pakage import *
import setting

class Power(pygame.sprite.Sprite):
    # the center is mean the center  when the collision happend 
    def __init__(self,center,power_imgs ): # need to parallel to player, so we add x and y 
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['shield','gun'])
        self.image=power_imgs[self.type]
        self.image.set_colorkey(setting.BLACK)

        # get the image original position and change th position 
        
        self.rect=self.image.get_rect()
        self.rect.center =center 
        self.speedy = 3
        
        
    def  update(self):
        self.rect.y += self.speedy 
        if self.rect.y> setting.HEIGHT :
            self.kill()
        
                 