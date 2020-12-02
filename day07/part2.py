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
    work_num = 5
    task_load = 60
    q = [(s, ord(s)-64 + task_load) for s in starts]
    workers = [None for _ in range(work_num)]
    DONE = set()
    glob_path = []
    timer = 0
    while q or any(workers):
        #print("TIME: ", timer)
        #print("que at start: ", q)
        print(workers, timer)
        for i, w in enumerate(workers):
            if not w:
                if not q:
                    continue
                workers[i] = q.pop(0)
            current, load = workers[i]
            if load == 1:
                print("Done: ", workers[i], " time: ", timer)
                DONE.add(current)
                for child in D[current]:
                    if not all(x in DONE for x in DD[child]):
                        continue
                    q.append((child, ord(child)-64 + task_load))
                if q:
                    workers[i] = q.pop(0)
                else:
                    workers[i] = None
            else:
                workers[i] = (current, load-1)



        timer += 1
    print(timer)

def read_file(filename):
    pass


print("part 1 answer: ", part1())
