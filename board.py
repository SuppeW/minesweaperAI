import random as rand
import pygame




rows, cols = input("Enter X and Y size of board: ").split(' ')
boardsize = int(rows)*int(cols)
bombAmount= input("Your board has " + str(boardsize) + " cells, how many bombs do you want? ")

rows, cols, bombAmount = int(rows), int(cols), int(bombAmount)

celldim = 20
margin = 1

winwidth, winheight = rows*celldim, cols*celldim
win = pygame.display.set_mode((winwidth, winheight))
pygame.display.set_caption("Grid Example")
win.fill((255,255,255))

x, y = 1, 1
celldim = 20
margin = 1
rectWidth, rectHeight = celldim-margin, celldim-margin
color = (200,200,200)
grey = (200,200,200)
ratio = int(winwidth/rectHeight)
cellnr = 0, 0
keys = pygame.key.get_pressed()



def playboard(y,x):
    bombs = []
    for i in range(x):
        bombs.append([])
        for j in range(y):
            bombs[i].append(0)

    for i in range(bombAmount):
        randx = int(rand.randint(0,x-1))
        randy = int(rand.randint(0,y-1))
        while True:
            if bombs[randx][randy] == 9:
                randx, randy = rand.randint(0,x-1), rand.randint(0,y-1)
            else:
                bombs[randx][randy] = 9
                break
    print("")
    print("THE RANDOMIZED BOMBGRID:")
    print("")
    print(bombs)
    totrow = len(bombs)
    totcol = len(bombs[0])

    for c in range(0,totcol):
        for r in range(0,totrow):
            if bombs[c][r] == 9:
                continue
            #Øverst til venstre
            elif c == 0 and r == 0:
                for y in range(0,2):
                    for x in range(0,2):
                        if bombs[c+y][r+x] == 9:
                            bombs[c][r] += 1
            #Øverst til høyre
            elif c == 0 and r == totrow-1:
                for y in range(0,2):
                    for x in range(-1,1):
                        if bombs[c+y][r+x] == 9:
                            bombs[c][r] += 1
            #nederst til høyre
            elif c == totcol-1 and r == totrow-1:
                for y in range(-1,1):
                    for x in range(-1,1):
                        if bombs[c+y][r+x] == 9:
                            bombs[c][r] += 1
            #øverst til venstre
            elif c == totcol-1 and r == 0:
                for y in range(-1,1):
                    for x in range(0,2):
                        if bombs[c+y][r+x] == 9:
                            bombs[c][r] += 1
            #venstre kant
            elif c  == 0:
                for y in range(0,2):
                    for x in range(-1,2):
                        if bombs[c+y][r+x] == 9:
                            bombs[c][r] += 1
            #høyre kant
            elif c  == totcol-1:
                for y in range(-1,1):
                    for x in range(-1,2):
                        if bombs[c+y][r+x] == 9:
                            bombs[c][r] += 1
            #øverste kant
            elif r  == 0:
                for y in range(-1,2):
                    for x in range(0,2):
                        if bombs[c+y][r+x] == 9:
                            bombs[c][r] += 1
            #nederste kant
            elif r  == totrow-1:
                for y in range(-1,2):
                    for x in range(-1,1):
                        if bombs[c+y][r+x] == 9:
                            bombs[c][r] += 1
            else:
                for y in range(-1,2):
                    for x in range(-1,2):
                        if bombs[c+y][r+x] == 9:
                            bombs[c][r] += 1

    print("")
    print("THE PLAYBOARD WITH COUNTED NEIGHBORS:")
    print("")
    print(bombs)
    return bombs

curboard = playboard(cols, rows)


pygame.init()
pygame.font.init()

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
            x, y = x-(x%(winheight/(cols/celldim)))+1, y-(y%(winwidth/(rows/celldim)))+1

            print(x,y)

            pygame.draw.rect(win, grey, (x, y, rectWidth, rectHeight))
            cellnr = int(x/celldim), int(y/celldim)


            c, r = cellnr
            print(c, r)
            num = str(curboard[r][c])

            pygame.draw.rect(win, (100,100,100), (x, y, rectWidth, rectHeight))

            font = pygame.font.SysFont(None, 30)
            text = font.render(num, True, (255,255,255))
            win.blit(text,(x+4, y))


            pygame.display.update()




pygame.quit()
