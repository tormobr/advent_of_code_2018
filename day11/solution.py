import numba
import numpy as np


grid = []
for y in range(1, 301):
    tmp = []
    for x in range(1,301):
        ID = x + 10
        pl = ID * y
        pl += 1955
        pl *= ID
        if pl < 100:
            pl = 0
        else:
            pl = int(str(pl)[-3])
        pl -= 5
        tmp.append(pl)
    grid.append(tmp)

winn = 0
winn_x_y = None
for y in range(len(grid)):
    for x in range(len(grid[0])):
        total = grid[y][x]
        for dx, dy in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1), (-1,1),(1,-1)]:
            try:
                total += grid[y+dy][x+dx]
            except IndexError:
                continue
        if total > winn:
            winn_x_y = (x-1, y-1)
            winn = total
print(winn)
print(winn_x_y)



grid = np.array(grid)
@numba.njit()
def hax():
    winn = 0
    winn_x_y = None
    score = 0
    H = len(grid)
    W = len(grid[0])
    for y in range(H):
        print(y)
        for x in range(W):
            for k in range(1, 300 - max(x, y)):
                sub_arr = grid[y:y+k, x:x+k]
                total = np.sum(sub_arr)
                if total > score:
                    winn_x_y = (x+1, y+1)
                    score = total
                    winn = k
    print("index: ", winn_x_y)
    print("size: ", winn)
    print("score: ", score)
hax()
#print(winn)
#print(winn_x_y)



