import time
import nltk
from nltk import FreqDist
import numpy as np
from collections import defaultdict

def part2(data):
    grid_size = get_max(data)
    grid = create_grid(data, grid_size)
    for y in range(grid_size):
        for x in range(grid_size):
            get_distance(x,y,data, grid)
    fd = FreqDist(np.array(grid).reshape((grid_size**2)))
    return fd[2]

def create_grid(data, n):
    grid = []
    index = 0 
    for y in range(n):
        line = []
        for x in range(n):
            if (x, y) in data:
                line.append(1)
                index += 1
            else:
                line.append(0)
        grid.append(line)
    return grid
    

def get_distance(x,y, data, grid):
    grid[y][x] = 2 if sum([abs(x1-x)+abs(y1-y) for (x1, y1) in data]) < 10000 else 0

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
    print(f"part 2 answer: {part2(data)}")
