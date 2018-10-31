import random as rand


rows, cols = input("Enter X and Y size of board: ").split(' ')
boardsize = int(rows)*int(cols)
bombAmount= input("Your board has " + str(boardsize) + " cells, how many bombs do you want? ")

rows, cols, bombAmount = int(rows), int(cols), int(bombAmount)

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

playboard(cols, rows)


print("1. Resize the terminal windowcmd so that the square breackets line up.")
print("2. You will now see the first randomized bombgrid. The number 9 represent a bomb")
print("3. And also the playgrid, including a number for neighboring bombs.")
input("4. Press Enter to exit!")
