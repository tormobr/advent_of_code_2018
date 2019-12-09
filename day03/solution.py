import nltk

def part1(data):
    vals = {}
    for line in data:
        for i in range(line[3]):
            for j in range(line[4]):
                if (line[1]+i, line[2]+j) not in vals.keys():
                    vals[(line[1]+i, line[2]+j)] = 1
                else: 
                    vals[(line[1]+i, line[2]+j)] += 1
    res = 0
    for v in vals.values():
        if v > 1:
            res += 1
    return vals

def part2(data):
    vals = part1(data)
    for line in data:
        overlap = False
        for i in range(line[3]):
            for j in range(line[4]):
                if vals[(line[1]+i, line[2]+j)] > 1:
                    overlap = True
        if not overlap:
            return line[0]


def parse_line(line):
    nr = int(line[1:line.find("@")])
    left = int(line[line.find("@")+1:line.find(",")])
    top = int(line[line.find(",")+1:line.find(":")])
    width = int(line[line.find(":")+1:line.find("x")])
    height = int(line[line.find("x")+1:])
    return (nr, left, top, width, height)

if __name__ == "__main__":
    lines = [parse_line(line.strip()) for line in open("input.txt", "r")]
    print(lines[0])
    print(part2(lines))
