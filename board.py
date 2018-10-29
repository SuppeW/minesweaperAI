import random as rand


rows, cols = input("Enter X and Y size of board: ").split(' ')
boardsize = int(rows)*int(cols)
bombAmount= input("Your board has " + str(boardsize) + " cells, how many bombs do you want? ")

rows, cols, bombAmount = int(rows), int(cols), int(bombAmount)








def randbombs(x,y):
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
                break
    return bombs[x][y]



playercellx, playercelly = input("Pick a cell you want to open by giving an x and y value: ").split(' ')
playercellx, playercelly = int(playercellx), int(playercelly)
if randbombs(playercellx, playercelly) == 1:
    print("you chose a cell containing a bomb...")
else:
    print("Your cell did not have bomb in it!")
