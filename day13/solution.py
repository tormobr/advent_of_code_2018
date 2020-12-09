import os
import sys
import time
from collections import defaultdict, deque
import numpy as np

dirs = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}
symbols = {
    (0, 1): ">",
    (0, -1): "<",
    (-1, 0): "^",
    (1, 0): "v"
}

slopes = {
    ">\\": (1, 0),
    ">/": (-1, 0),
    "<\\": (-1, 0),
    "</": (1, 0),
    "^\\": (0, -1),
    "^/": (0, 1),
    "v\\": (0, 1),
    "v/": (0, -1),
}

directions = [(0,1), (1, 0), (0, -1), (-1, 0)]


def solve():
    grid = np.array([[c for c in line.strip("\n")] for line in open("input.txt")])
    
    players = []
    for y, line in enumerate(grid):
        for x, elem in enumerate(line):
            if elem in dirs.keys():
                players.append(((y, x), dirs[elem], elem, "-", 0))

    print("players: ", players)
  
    turn = ["L", "S", "R"]
    ticks = 10**7
    for j in range(ticks):
        print(j)
        crash = False
        crash_index = []
        if j > 100000:
            os.system("clear")
            for line in grid:
                print("".join(line))
            print(j)
            time.sleep(1)
        if len(players) == 1:
            for line in grid:
                print("".join(line))
            return players
        for i, ((y, x), (dy, dx), symb, prev_symb, turns) in enumerate(players):
            current = grid[y][x]
            new_y = y + dy
            new_x = x + dx
            new_dir = (dy, dx)
            nex = grid[new_y][new_x]
            new_turns = turns

            if nex == "+":
                turn_key = turn[turns % 3]
                if turn_key == "R":
                    new_dir = directions[(directions.index((dy,dx)) + 1) % 4]
                if turn_key == "L":
                    new_dir = directions[(directions.index((dy,dx)) - 1) % 4]
                new_turns += 1
            elif current+nex in slopes.keys():
                new_dir = slopes[current+nex]

            players[i] = ((new_y, new_x), new_dir, symb, nex, new_turns)
            grid[y][x] = prev_symb
            #grid[new_y][new_x] =  symbols[new_dir]
            #print(y, x, dy, dx)
            #print(nex)
        pop_index = []
        for i, ((y, x), (dy, dx), symb, prev_symb, turns) in enumerate(players):
            for i2, ((y2, x2), (dy2, dx2), symb2, prev_symb2, turns2) in enumerate(players):
                if (x, y) == (x2, y2) and i != i2:
                    pop_index.append(i)
                    pop_index.append(i2)
                    break
            else:
                grid[y][x] =  symbols[(dy, dx)]
                players[i] = ((y, x), (dy, dx), symbols[(dy ,dx)], prev_symb, turns)
        
        new_players = []
        for index, p in enumerate(players):
            if index not in pop_index:
                new_players.append(p)
        players = new_players

if __name__ == "__main__":
    print(solve())
