#importanje pygame biblioteke
from random import random
import pygame
import random
pygame.init()


fps=60


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

#setup za prozor u kojem će igra bit
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

x=400
y=700

enemy_x=random.randrange(0,SCREEN_WIDTH-50,1)
enemy_y=0

force=0
enemy_speed=fps/15

player=pygame.image.load('plane.png')
enemy=pygame.image.load('enemy.png')

clock = pygame.time.Clock()
#pokreći dok ne kažemo quit
running=True
while running:

  #jesmo li stisnili quit?
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN :
      if event.key == pygame.K_LEFT:
        force=-(fps/10)
      if event.key == pygame.K_RIGHT:
        force=fps/10

  #provjeravamo je li igrac na rubu ekrana, ako je zaustavljamo ga (force ne može bit 0 jer se onda nikad neće pomaknut)
  if x<0:
    x=0.1
  if x>SCREEN_WIDTH-50:
    x=SCREEN_WIDTH-50.1

  

  screen.fill((255,255,255)) #ekran bijele boje
  screen.blit(player,[x,y])
  screen.blit(enemy,[enemy_x,enemy_y])
  x+=force
  enemy_y+=enemy_speed
  
  if y+25 < enemy_y:
    enemy_x=random.randrange(0,SCREEN_WIDTH-50,1)
    enemy_y=0
  
  
  pygame.display.update()
  clock.tick(fps)

pygame.quit()





