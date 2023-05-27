from pygame import*
from balls import*

class ship(sprite.Sprite):
  bullets = sprite.Group()


  def __init__(self, image_path,x,y):
    sprite.Sprite.__init__(self)
    self.image=image.load("zolika.jpg")
    self.image = transform.scale(self.image, (30,30))

    self.rect = self.image.get_rect() 
        
    self.start_x = x
    self.start_y = y
    self.rect.x = x
    self.rect.y = y 
  
  def shoot(self):
    self.bullets.add(balls(self.rect.x,self.rect.y))

  def update(self,screen):
    keys = key.get_pressed()
    if keys[K_LEFT] and self.rect.x > 0:
      self.rect.x -= 5
    if keys[K_RIGHT] and self.rect.x < 740:
      self.rect.x += 5
    if keys[K_SPACE]:
      self.shoot()
    self.bullets.update()
    self.bullets.draw(screen)
    for bullet in self.bullets:
      if bullet.getY() < 0:
        bullet.kill()
    
