import time as time
import random, pygame

pygame.init()

bombs =[
[0,9,0,0,9],
[0,9,9,0,0],
[9,9,0,9,9],
[0,0,0,9,0],
[0,9,0,0,9]
]

neighborcount = 0
totcol = 5
totrow = 5

#print(bombs[row][col])


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

print(bombs)

curnum = str(bombs[0][0])
font = pygame.font.SysFont('comicsansms', 72)
text = font.render(curnum,True,(0,128,0))

win = pygame.display.set_mode((400, 400))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((255,255,255))
    win.blit(text,(0,0))

    pygame.display.update()


pygame.quit()
