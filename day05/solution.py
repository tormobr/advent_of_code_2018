

def part1(data):
    result = data
    current_length = len(data)
    i = 0
    while True:
        if abs(ord(result[i]) - ord(result[i+1])) == 32:
            result = result[:i] + result[i+2:]
            current_length -= 2
            i -= 2
        i += 1
        if i == len(result)-1:
            break
    return len(result)-1

def part2(data):
    distinct = set([c.lower() for c in data.strip()])
    results = []
    data = [c for c in data.strip()]
    for d in distinct:
        result = list(filter(lambda x: x != d and x != d.upper(), data))
        i = 0
        while True:
            if abs(ord(result[i]) - ord(result[i+1])) == 32:
                result = result[:i] + result[i+2:]
                i -= 2
            i += 1
            if i == len(result)-1:
                break
        results.append((d, len(result)))
    
    return min(results, key=lambda x: x[1])
if __name__ =="__main__":
    data = open("input.txt", "r").read()
    print(part1(data))
    print(part2(data))
