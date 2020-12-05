from collections import defaultdict
import sys
nums = []
sys.setrecursionlimit(100000)

def part_2():
    global nums
    nums = [int(x) for x in open("input.txt").read().split()]
    nodes = defaultdict(list)
    dst, score = rec(0, nodes)
    print(nodes)
    return score

def rec(index, nodes):
    print("index: ", index, " value: ", nums[index])
    children = nums[index]
    meta_entries = nums[index+1]
    if children == 0:
        meta = nums[index+2: index+2 + meta_entries]
        nodes[index].append(sum(meta))
        return meta_entries + 2, sum(meta)

    dst = 2
    child_scores = []
    for _ in range(children):
        d, score = rec(index + dst, nodes)
        dst += d

        child_scores.append(score)

    meta = nums[index + dst: index+dst+meta_entries]
    
    score = 0
    nodes[index] = (child_scores)
    for m in meta:
        if m > children or m == 0:
            continue
        score += child_scores[m-1]
    print(score, index)

     


    return dst + meta_entries, score

if __name__ == "__main__":
    print("res 2 :: ", part_2())
