import numpy as np

def part1(data):
    dist = {}
    max_x = max(data, key=lambda x: x[0])
    max_y = max(data, key=lambda x: x[1])
    a = np.zeros((max_x[0]+1, max_y[1]+1))
    for c in data:
        a[c[0],c[1]] = 1
    
    for c in data:
        dist[c] = {}
        for i, row in enumerate(a):
            for j, elem in enumerate(row):
                if (i,j) not in dist[c].keys():
                    dist[c][(i,j)] = abs(c[0] -j) + abs(c[1] - i)             

if __name__ == "__main__":
    data = [list(map(int, line.strip().split(","))) for line in open("input.txt", "r")]
    print(part1(data))
