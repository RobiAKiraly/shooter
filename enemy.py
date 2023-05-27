from pygame import *

class Enemy(sprite.Sprite):
    def __init__(self, image_path,x,y):
        sprite.Sprite.__init__(self)
        self.image=image.load("zolika.jpg")
        self.image = transform.scale(self.image, (30,30))

        self.rect = self.image.get_rect() 
        
        self.start_x = x
        self.start_y = y
        self.rect.x = x
        self.rect.y = y 
