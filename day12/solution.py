import time
from copy import deepcopy


lines = [l.strip() for l in open("input.txt")]
state = list(lines[0].split()[2])
for _ in range(4):
    state.insert(0, ".")
    state.append(".")

rules = lines[2:]
D = {}
for r in rules:
    k, v = r.split("=>")
    k = k.strip()
    v = v.strip()
    D[k] = v

def get_score(state):
    ret = 0
    for i in range(len(state)):
        if state[i] == "#":
            ret += i-shift
    return ret


iterations = 2001
shift = 4
thousand_score = 0
rate = 0
part_1 = 0
for i in range(iterations):
    new_state = deepcopy(state)
    score = get_score(new_state)
    if i == 1000:
        thousand_score = score
    elif i == 2000:
        rate = score - thousand_score
    elif i == 20:
        part_1 = score
    for x in range(2,len(state)-2):
        key = "".join(state[x-2: x+2+1])
        if key not in D.keys():
            new_state[x] = "."
        else:
            new_state[x] = D[key]
    shift_start = 4 - new_state.index("#")
    for _ in range(shift_start):
        new_state.insert(0, ".")
        shift += 1
    shift_end = 4 - new_state[::-1].index("#")
    for _ in range(shift_end):
        new_state.append(".")
    state = new_state



print("part 1: ", part_1)
print("part 2: ", (50000000000 / 1000 - 1) * rate + thousand_score)
