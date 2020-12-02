from copy import deepcopy
from collections import defaultdict

def part1():
    lines = [l.split() for l in open("input.txt")]
    D = defaultdict(list)
    DD = defaultdict(list)

    for l in lines:
        k, v = l[1], l[-3]
        D[k].append(v)
        DD[v].append(k)
    start = None
    all_values = []
    for v in D.values():
        all_values += v

    starts = []
    for key in D.keys():
        if key not in all_values:
            starts.append(key)
          
    print(starts)
    BFS(starts, D, DD)
    return "strudel"

def BFS(starts, D, DD):
    path = []
    print("starts: ", starts)
    q = starts
    SEEN = set()
    glob_path = []
    while q:
        q = sorted(q)
        current = q.pop(0)
        print(current)
        print(q)
        glob_path.append(current)
        if current in SEEN:
            continue
        SEEN.add(current)

        for child in D[current]:
            if not all(x in SEEN for x in DD[child]):
                continue
            q.append(child)
    print("".join(glob_path))

def read_file(filename):
    pass


print("part 1 answer: ", part1())
