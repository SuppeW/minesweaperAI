import random as rand

rows = 10
cols = 10
bombAmount = 20
changedCells = []


def randomlist():
    bombcount = 0
    bombs = []
    for i in range(rows):
        bombs.append([])
        for j in range(cols):
            bombs[i].append(0)

    for i in range(bombAmount):
        randx = int(rand.randint(0,rows-1))
        randy = int(rand.randint(0,cols-1))
        while True:
            if bombs[randx][randy] == 1:
                randx, randy = rand.randint(0,rows-1), rand.randint(0,cols-1)
            else:
                bombs[randx][randy] = 1
                bombcount +=1
                print(bombcount)
                break
    return bombs

print(randomlist())
