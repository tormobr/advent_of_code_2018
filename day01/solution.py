
def part1(data):
    return sum(data)

def part2(data):
    seen = {0}
    current = 0
    index = 0
    while True:
        current += data[index]
        if current in seen:
            break
        seen.add(current)
        index = (index+1)%len(data)
    return current

if __name__=="__main__":
    lines = [x.strip() for x in open("input.txt", "r")]
    data = [int(l) for l in lines]
    print(part2(data))
