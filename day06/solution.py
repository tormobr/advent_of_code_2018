import time
import nltk
from nltk import FreqDist
import numpy as np
from collections import defaultdict

def part1(data):
    distances = defaultdict(list)
    grid_size = get_max(data)
    grid = create_grid(data, grid_size)
    #pretty_print(grid)
    for y in range(grid_size):
        for x in range(grid_size):
            get_distance(x,y,data, distances, grid)
            print("new iteration")
    pretty_print(grid)
    fd = FreqDist(np.array(grid).reshape((grid_size**2)))
    for s,c in fd.most_common():
        if not infinite(s, None, grid):
            print("res: ", c)
    return data

def create_grid(data, n):
    grid = []
    index = 0 
    for y in range(n):
        line = []
        for x in range(n):
            if (x, y) in data:
                line.append(chr(97 + index))
                index += 1
            else:
                line.append(".")
        grid.append(line)
    return grid
    

def get_distance(x,y, data, ditances, grid):
    minn = 100000
    min_x = 0
    min_y = 0
    res = []
    for (x1, y1) in data:
        neww = (abs(x1-x) + abs(y1-y))
        res.append(neww)
        if neww < minn:
            minn = neww
            min_x, min_y = x1, y1

    if res.count(minn) > 1:
        grid[y][x] = "."
        return
    grid[y][x] = grid[min_y][min_x]

def pretty_print(grid):
    res = ""
    for line in grid:
        for c in line:
            res += str(c)
        res += "\n"
    print(res)

def get_max(data):
    max_x = max(data, key=lambda x: x[0])[0]
    max_y = max(data, key=lambda x: x[1])[1]
    return max(max_x, max_y) +1

def infinite(s, res, grid):
    top = [grid[0][i] for i in range(len(grid[0]))]
    bottom = [grid[-1][i] for i in range(len(grid[0]))]
    left = [grid[i][0] for i in range(len(grid))]
    right = [grid[i][-1] for i in range(len(grid))]
    if s not in top+bottom+left+right:
        return False
    return True

if __name__ == "__main__":
    data = [tuple(map(int, line.strip().split(","))) for line in open("input.txt", "r")]
    print(part1(data))
