import numpy as np

def part2(data):
    grid_size = max(max(data, key=lambda x: x[0])[0],max(data, key=lambda x: x[1])[1])
    grid = create_grid(data, grid_size)
    [get_distance(x,y,data,grid) for y in range(grid_size) for x in range(grid_size)]
    return np.count_nonzero(np.array(grid).reshape((grid_size**2))==2)

def create_grid(data, n):
    return [[1 if (x,y) in data else 0 for x in range(n)] for y in range(n)]

def get_distance(x,y, data, grid):
    grid[y][x] = 2 if sum([abs(x1-x)+abs(y1-y) for (x1, y1) in data]) < 10000 else 0

if __name__ == "__main__":
    data = [tuple(map(int, line.strip().split(","))) for line in open("input.txt", "r")]
    print(f"part 2 answer: {part2(data)}")
