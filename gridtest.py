import pygame

pygame.init()

winwidth, winheight = 401, 401
win = pygame.display.set_mode((winwidth, winheight))
pygame.display.set_caption("Grid")
run = True

x, y = 1, 1
margin = 1
rectWidth, rectHeight = 19, 19
color = (200,200,200)


win.fill((255,255,255))
for c in range(0,20):
    x=1
    for r in range(0,20):
        pygame.draw.rect(win, color, (x, y, rectWidth, rectHeight))
        x = (x+rectWidth+margin)
    y = (y+rectHeight+margin)

pygame.display.update()

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


pygame.quit()
