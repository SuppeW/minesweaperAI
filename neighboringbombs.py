import random as rand

bombs =[
[0,9,0,0,9],
[0,0,9,0,0],
[9,0,0,0,9],
[0,9,0,0,0],
[0,9,0,0,9]
]

bombnnumbers = []

totrows = 5
totcols = 5

neighborcount = 0


#filling an empty grid with 0s.
for x in range(0, totrows):
    bombnnumbers.append([])
    for y in range(0, totcols):
        bombnnumbers[x].append(0)


#Looping trough the bombgrid..
for rows in range(0, totrows-1):
    for cols in range(0, totcols-1):

        #Telling no to check itself, and settin number in new grid to 9.
        if bombs[rows][cols] == 9:
            continue

        #The following 4 loops is checking the corners to see if there is any live neighbors.
        #Top left corner
        elif rows and cols == 0:
            for x in range(0,1):
                for y in range(0,1):
                    if bombs[rows+x][cols+y] == 9:
                        neighborcount += 1
        #Bottom right corner
        elif rows == totrows-1 and cols == totcols-1:
            for x in range(-1,0):
                for y in range(-1,0):
                    if bombs[rows+x][cols+y] == 9:
                        neighborcount += 1

        #Bottom Left corner
        elif rows == totrows-1 and cols == 0:
            for x in range(-1,0):
                for y in range(0,1):
                    if bombs[rows+x][cols+y] == 9:
                        neighborcount += 1

        #Top right corner
        elif rows == 0 and cols == totcols-1:
            for x in range(0,1):
                for y in range(-1,0):
                    if bombs[rows+x][cols+y] == 9:
                        neighborcount += 1

        #The following 4 loops is checking the edges to look for neighboring bombs.
        #Left edge
        elif rows == 0:
            for x in range(0,1):
                for y in range(-1,1):
                    if bombs[rows+x][cols+y] == 9:
                        neighborcount += 1

        #Right edge
        elif rows == totrows-1:
            for x in range(-1,0):
                for y in range(-1,1):
                    if bombs[rows+x][cols+y] == 9:
                        neighborcount += 1

        #Top edge
        elif cols == 0:
            for x in range(-1,1):
                for y in range(0,1):
                    if bombs[rows+x][cols+y] == 9:
                        neighborcount += 1

        #Bottom edge
        elif cols == totcols-1:
            for x in range(-1,1):
                for y in range(-1,0):
                    if bombs[rows+x][cols+y] == 9:
                        neighborcount += 1

        #Every other cell
        else:
            for x in range(-1,1):
                for y in range(-1,1):
                    if bombs[rows+x][cols+y] == 9:
                        neighborcount += 1



        #inputting new data into new grid.
        bombnnumbers[rows][cols] = neighborcount

print(bombnnumbers)
