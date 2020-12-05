import time
from matplotlib import pyplot as plt
import os
import numpy as np
import re
WHITE_SQUARE = "\u25a0"

# Draw matrix in terminal
def draw_matrix(m, mapping={1: WHITE_SQUARE + " ", 0:"  "}):
    s = "" 
    for row in m:
        s += "\t"
        for item in row:
            if item not in mapping.keys():
                item = 0
            s += mapping[item]
        s += "\n"
    print(s)
    return s

def get_size(items):
    max_y = max(items, key=lambda x: x[0][1])
    min_y = min(items, key=lambda x: x[0][1])
    return max_y[0][1] - min_y[0][1]


lines = [line.strip() for line in open("input.txt")]
items = []
for l in lines:
    m = re.findall(r"<[\d|,|\s+|\-]*>", l)
    pos = tuple([int(s.strip()) for s in m[0][1:-1].split(",")])
    speed = tuple([int(s.strip()) for s in m[1][1:-1].split(",")])
    items.append((pos, speed))

seconds = 100000
sizes = []
for i in range(10946):
    for index, ((x, y), (speed_x, speed_y)) in enumerate(items):
        new_x = x + speed_x
        new_y = y + speed_y
        items[index] = ((new_x, new_y), (speed_x, speed_y))
    sizes.append(get_size(items))

print(get_size(items))
grid = np.zeros((300, 300))
for item in items:
    #print(item)
    for index, ((x, y), (speed_x, speed_y)) in enumerate(items):
        grid[y][x] = 1

draw_matrix(grid)
        
    

    


