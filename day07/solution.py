from collections import defaultdict

def part1(relations, rev):
    SEEN = []
    Q = []
    for k in sorted(relations.keys()):
        if k not in rev.keys():
            Q.append(k)
    BFS(k, relations.copy(), rev.copy(), SEEN, Q)
    return "".join(SEEN)

def BFS(start, relations, rev, SEEN, Q):
    Q.append(start)
    while Q:
        ready = True
        Q.sort() 
        current = Q.pop(0)
        for item in rev[current]:
            if item not in SEEN:
                ready = False
        
        if current in SEEN or not ready:
            continue 

        SEEN.append(current) 
        for item in sorted(relations[current]):
            Q.append(item)
    return SEEN

def read_file(filename):
    relations = defaultdict(list)
    rev = defaultdict(list)
    with open(filename) as fd:
        for line in fd:
            line = line.split()
            a,b = line[1], line[-3]
            relations[a].append(b)
            rev[b].append(a)
    
    return relations, rev



data = read_file("input2.txt")
print("part 1 answer: ", part1(*data))
