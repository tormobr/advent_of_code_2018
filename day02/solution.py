

def part1(data):
    doubles = 0
    tripples = 0
    
    for line in data:
        letters = [c for c in line]
        for c in letters:
            if letters.count(c) == 2:
                doubles += 1
                break
        for c in letters:
            if letters.count(c) == 3:
                tripples += 1
                break

    return doubles * tripples

def part2(data):
    for line in data:
        for line2 in data:
            if line != line2:
                ret = differ_by_one(line, line2)
                print(ret)
                if ret[0] == True:
                    print(line)
                    return line[0:ret[1]] + line[ret[1]+1:]


def differ_by_one(a, b):
    letters_a = [c for c in a]
    letters_b = [c for c in b]
    index = -1
    found = False
    for i in range(len(letters_a)):
        if letters_a[i] != letters_b[i]:
            if not found:
                found = True
                index = i
            else:
                return (False, -1)
    return (True, index)

if __name__=="__main__":
    data = [line.strip() for line in open("input.txt", "r")]
    print(part2(data))
