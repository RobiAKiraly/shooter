from enemy import*
from ship import*
from pygame import*
import random

init()
screen = display.set_mode((800, 600))
clock = time.Clock()

char = ship("download.jpg",300,300)


backgrounds = [
    'space1.jpg',
    'space2.jpg',
]
entitys = sprite.Group()
entitys.add(char)
selected_background = random.choice(backgrounds)
background_image = image.load(selected_background)
background_image = transform.scale(background_image, (800, 600))
screen.blit(background_image, (0, 0))
run = True

while run:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window  
    for e in event.get():
        if e.type == QUIT:
            run = False 
    
    # screen.fill((0,0,0)) #comment this and see what hapen
    # screen.blit(background_image, (0, 0))
    screen.blit(background_image, (0, 0))
    char.update(screen)

    entitys.draw(screen)
    display.flip()
    display.update()
    dt = clock.tick(60) / 1000
