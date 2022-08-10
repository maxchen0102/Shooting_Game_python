  
  
from pakage import *
import setting

class Explosoin(pygame.sprite.Sprite):
    # the center is mean the center  when the collision happend 
    def __init__(self,center,size,expl_anim): # need to parallel to player, so we add x and y 
        pygame.sprite.Sprite.__init__(self)
        self.expl_anim=expl_anim
        self.size=size 
        self.image=self.expl_anim[self.size][0] 
        
        self.rect= self.image.get_rect() # chatch the center of image 
        self.rect.center= center  
        self.frame=0
        
        # we nee d to use this way to slow the FPS or the explosion image will change to fast 
        self.last_update =pygame.time.get_ticks()
        self.frame_rate =50  # every 50 secs we will change 

    def update(self):
        now =pygame.time.get_ticks() # right now time
        if now -self.last_update>self.frame_rate: # if past our thredhold 
            self.last_update=now  # time update to now 
            self.frame+=1  # add image index 
            if self.frame==len(self.expl_anim[self.size]): # consume all image 
                self.kill()    
            else:
                self.image=self.expl_anim[self.size][self.frame] # change to next image 
                center=self.rect.center  # reset the new center 
                self.rect=self.image.get_rect()
                self.rect.center=center 
