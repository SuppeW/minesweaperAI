import pygame, random

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

list1 = [
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6],
    [1,2,3,4,5,6]]
    




screen.fill((255,255,255))
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,(0,255,0),(0,0,140,140))
            mousepos = pygame.mouse.get_pos()
            x,y = mousepos
            x,y = int(x-(x%(400/20))+1), int(y-(y%(400/20))+1)
            print(mousepos)
            print(x,y)
            cellnr = int(x/20), int(y/20)
            print(cellnr)
            r, c = cellnr
            print(r,c)
            num = str(list1[c][r])
            font = pygame.font.SysFont(None, 20)
            text = font.render(num, True, (0, 0, 0))
            screen.fill((255, 255, 255))
            screen.blit(text,(x,y))
            pygame.display.update()    

pygame.quit()
