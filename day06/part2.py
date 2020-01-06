import numpy as np

def part2(data):
    grid_size = get_max(data)
    grid = create_grid(data, grid_size)
    for y in range(grid_size):
        for x in range(grid_size):
            get_distance(x,y,data, grid)
    grid_1d = np.array(grid).reshape((grid_size**2))
    res = np.count_nonzero(grid_1d==2)
    return res

def create_grid(data, n):
    grid = []
    for y in range(n):
        grid.append([])
        for x in range(n):
            if (x, y) in data:
                grid[y].append(1)
            else:
                grid[y].append(0)
    return grid
    

def get_distance(x,y, data, grid):
    grid[y][x] = 2 if sum([abs(x1-x)+abs(y1-y) for (x1, y1) in data]) < 10000 else 0

def get_max(data):
    max_x = max(data, key=lambda x: x[0])[0]
    max_y = max(data, key=lambda x: x[1])[1]
    return max(max_x, max_y) +1

if __name__ == "__main__":
    data = [tuple(map(int, line.strip().split(","))) for line in open("input.txt", "r")]
    print(f"part 2 answer: {part2(data)}")
