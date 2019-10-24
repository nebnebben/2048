import random
import sys
import os
Grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#Grid = [[0]*4 for _ in range(5)]


def start(Grid):
    spawn = False
    while spawn == False:
        rnum1 = random.randrange(0, 4)
        rnum2 = random.randrange(0, 4)
        if Grid[rnum1][rnum2] == 0:
            Grid[rnum1][rnum2] = 1
            spawn = True
    spawn = False
    while spawn == False:
        rnum1 = random.randrange(0, 4)
        rnum2 = random.randrange(0, 4)
        if Grid[rnum1][rnum2] == 0:
            Grid[rnum1][rnum2] = 2
            spawn = True
    return Grid

def gennumber(Grid):
    spawn = False
    full = True
    for y in range(0, 4):
        for x in range(0, 4):
            if Grid[x][y] == 0:
                full = False
    if full == True:
        spawn = True
    while spawn == False:
        rnum1 = random.randrange(0, 4)
        rnum2 = random.randrange(0, 4)
        if Grid[rnum1][rnum2] == 0:
            rnum3 = random.randrange(1,3)
            Grid[rnum1][rnum2] = rnum3
            spawn = True
    return Grid

def move(Grid):
    valid = False
    while valid == False:
        mov = input("Choose a move")
        print(mov)
        if mov == "w":
            valid = True
            moveup(valid, Grid)
        elif mov == "a":
            valid = True
            moveleft(valid, Grid)
        elif mov == "s":
            valid = True
            movedown(valid, Grid)
        elif mov == "d":
            valid = True
            moveright(valid, Grid)

        else:
            print("That is not a valid move, please try again")

def moveleft(valid, Grid):
    valid = False
    stop = False
    for x in range(0,4):
        for y in range(0,4):
            stop = False
            if Grid[x][y] == 0:
                for i in range(x,4):
                    if Grid[i][y] != 0 and stop == False:
                        Grid[x][y] = Grid[i][y]
                        Grid[i][y] = 0
                        stop = True
                        valid = True
            stop = False
            if Grid[x][y] != 0:
                for i in range(x+1,4):
                    if Grid[i][y] == Grid[x][y] and stop == False and i == x + 1 and Grid[x][y] != 1 and Grid[x][y] != 2:
                        Grid[x][y] = Grid[x][y] * 2
                        Grid[i][y] = 0
                        stop = True
                        valid = True
                    elif Grid[i][y] == 1 and Grid[x][y] == 2 and stop == False and i == x + 1:
                        Grid[x][y] = 3
                        Grid[i][y] = 0
                        stop = True
                        valid = True
                    elif Grid[i][y] == 2 and Grid[x][y] == 1 and stop == False and i == x + 1:
                        Grid[x][y] = 3
                        Grid[i][y] = 0
                        stop = True
                        valid = True
                    if Grid[i][y] != 0:
                        stop = True
    return(valid, Grid)



def moveright(valid, Grid):
    valid = False
    stop = False
    for x in range(3,-1,-1):
        for y in range(0,4):
            stop = False
            if Grid[x][y] == 0:
                for i in range(x,-1,-1):
                    if Grid[i][y] != 0 and stop == False:
                        Grid[x][y] = Grid[i][y]
                        Grid[i][y] = 0
                        stop = True
                        valid = True
            stop = False
            if Grid[x][y] != 0:
                for i in range(x-1,-1,-1):
                    if Grid[i][y] == Grid[x][y] and stop == False and i == x - 1 and Grid[x][y] != 1 and Grid[x][y] != 2:
                        Grid[x][y] = Grid[x][y] * 2
                        Grid[i][y] = 0
                        stop = True
                        valid = True
                    elif Grid[i][y] == 1 and Grid[x][y] == 2 and stop == False and i == x - 1:
                        Grid[x][y] = 3
                        Grid[i][y] = 0
                        stop = True
                        valid = True
                    elif Grid[i][y] == 2 and Grid[x][y] == 1 and stop == False and i == x - 1:
                        Grid[x][y] = 3
                        Grid[i][y] = 0
                        stop = True
                        valid = True
                    if Grid[i][y] != 0:
                        stop = True
    return(valid, Grid)


def moveup(valid, Grid):
    valid = False
    stop = False
    for x in range(0,4):
        for y in range(0,4):
            stop = False
            if Grid[x][y] == 0:
                for i in range(y,4):
                    if Grid[x][i] != 0 and stop == False:
                        Grid[x][y] = Grid[x][i]
                        Grid[x][i] = 0
                        stop = True
                        valid = True
            stop = False
            if Grid[x][y] != 0:
                for i in range(y+1,4):
                    if Grid[x][i] == Grid[x][y] and stop == False and i == y + 1 and Grid[x][y] != 1 and Grid[x][y] != 2:
                        Grid[x][y] = Grid[x][y] * 2
                        Grid[x][i] = 0
                        stop = True
                        valid = True
                    elif Grid[x][i] == 1 and Grid[x][y] == 2 and stop == False and i == y + 1:
                        Grid[x][y] = 3
                        Grid[x][i] = 0
                        stop = True
                        valid = True
                    elif Grid[x][i] == 2 and Grid[x][y] == 1 and stop == False and i == y + 1:
                        Grid[x][y] = 3
                        Grid[x][i] = 0
                        stop = True
                        valid = True
                    if Grid[x][i] != 0:
                        stop = True
    return(valid, Grid)

def movedown(valid, Grid):
    valid = False
    stop = False
    for x in range(0, 4):
        for y in range(3,-1,-1):
            stop = False
            if Grid[x][y] == 0:
                for i in range(y, -1,-1):
                    if Grid[x][i] != 0 and stop == False:
                        Grid[x][y] = Grid[x][i]
                        Grid[x][i] = 0
                        stop = True
                        valid = True
            stop = False
            if Grid[x][y] != 0:
                for i in range(y-1,-1,-1):
                    if Grid[x][i] == Grid[x][y] and stop == False and i == y - 1 and Grid[x][y] != 1 and Grid[x][y] != 2:
                        Grid[x][y] = Grid[x][y] * 2
                        Grid[x][i] = 0
                        stop = True
                        valid = True
                    elif Grid[x][i] == 1 and Grid[x][y] == 2 and stop == False and i == y - 1:
                        Grid[x][y] = 3
                        Grid[x][i] = 0
                        stop = True
                        valid = True
                    elif Grid[x][i] == 2 and Grid[x][y] == 1 and stop == False and i == y - 1:
                        Grid[x][y] = 3
                        Grid[x][i] = 0
                        stop = True
                        valid = True
                    if Grid[x][i] != 0:
                        stop = True
    return (valid, Grid)


def play(Grid):
    Lost = False
    while Lost == False:
        print("test")



start(Grid)

Grid = gennumber(Grid)
for y in range(0,4):
    for x in range(0,4):
        print(Grid[x][y], end=' ')
        if x == 3:
            print("")
a=1
while a==1:
    move(Grid)

    Grid = gennumber(Grid)
    for y in range(0,4):
        for x in range(0,4):
            print(Grid[x][y],end=' ')
            if x == 3:
                print("")
