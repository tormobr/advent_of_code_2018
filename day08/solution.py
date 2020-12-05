import sys
nums = []
sys.setrecursionlimit(100000)

def part_1():
    global nums
    nums = [int(x) for x in open("input.txt").read().split()]
    nodes = []
    rec(0, nodes)
    hax = []
    for n in nodes:
        hax += (n[2])
    print(nodes)
    print(sum(hax))
def rec(index, nodes):
    print("index: ", index, " value: ", nums[index])
    children = nums[index]
    meta_entries = nums[index+1]
    if children == 0:
        meta = nums[index+2: index+2 + meta_entries]
        nodes.append((children, meta_entries, meta))
        return meta_entries + 2
    dst = 2
    for _ in range(children):
        dst += rec(index + dst, nodes)
    meta = nums[index + dst: index+dst+meta_entries]
    nodes.append((children, meta_entries, meta))
    return dst + meta_entries

if __name__ == "__main__":
    print("res: ", part_1())
