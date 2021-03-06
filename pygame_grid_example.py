import pygame, random


list1 = [
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19],
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    ]



pygame.init()
pygame.font.init()

winwidth, winheight = 400, 400
win = pygame.display.set_mode((winwidth, winheight))

pygame.display.set_caption("Grid Example")


x, y = 1, 1
celldim = 20
margin = 1
rectWidth, rectHeight = celldim-margin, celldim-margin
color = (200,200,200)
red = (255,0,0)
ratio = int(winwidth/rectHeight)
cellnr = 0, 0

keys = pygame.key.get_pressed()


win.fill((255,255,255))


for c in range(0,ratio):
    x=1
    for r in range(0,ratio):
        pygame.draw.rect(win, color, (x, y, rectWidth, rectHeight))
        x = (x+rectWidth+margin)
    y = (y+rectHeight+margin)

pygame.display.update()

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            print(mousepos)
            x, y = mousepos
            x, y = x-(x%(winheight/celldim))+1, y-(y%(winwidth/celldim))+1
            print(x,y)
            pygame.draw.rect(win, (0,0,0), (x, y, rectWidth, rectHeight))
            cellnr = int(x/celldim), int(y/celldim)
            print(cellnr)

            c, r = cellnr
            
            num = str(list1[r][c])
            font = pygame.font.SysFont(None,30)
            text = font.render(num, True, (255,255,255))

            
            win.blit(text,(x+4,y))
            pygame.display.update()



pygame.quit()
