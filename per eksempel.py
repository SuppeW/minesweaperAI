import pygame, random

pygame.init()
win = pygame.display.set_mode((400,400))

randnum1 = int(random.randint(0,255))
randnum2 = int(random.randint(0,255))
randnum3 = int(random.randint(0,255))

randposx = int(random.randint(0,350))
randposy = int(random.randint(0,350))
               



run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    win.fill((255,255,255))
    pygame.draw.rect(win, (randnum1, randnum2, randnum3),(randposx, randposy, 50, 50))
    pygame.display.update()

pygame.quit()
            
