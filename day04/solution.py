
def part1(data):
    guard = -1
    sleep = 0
    G = {}
    for line in data:
        if line:
            year, month, day, time, message = parse_line(line)
            time = int(time)
            message_split = message.split()
            if "Guard" in message:
                guard = message_split[1]
            elif "falls asleep" in message:
                sleep = time
            elif "wakes up" in message:
                for i in range(sleep, time):
                    if guard not in G.keys():
                        G[guard] = {}
                    if i not in G[guard].keys():
                        G[guard][i] = 0
                    G[guard][i] += 1
    return get_max2(G)
def get_max(G):
    best = (0,0)
    for k, v in G.items():
        total_mins = 0
        for key, value in v.items():
            total_mins += value
        if total_mins > best[1]:
            best = (k, total_mins)

    best2 = (0,0)
    for k, v in G[best[0]].items():
        if v > best2[1]:
            best2 = (k, v)
    return best2[0], best[0]

def get_max2(G):
    best = (0,0,0)
    for k, v in G.items():
        for key, value in v.items():
            if value > best[2]:
                best = (k,key, value)
    return best

def parse_line(line):
    message = line.split("]")[1].strip()
    print(message)
    line_split = line.split()
    date = line_split[0][1:]
    date_split = date.split("-")
    year = date_split[0]
    month = date_split[1]
    day = date_split[2]

    time = line_split[1][3:-1]
    print(int(time))
    return year, month, day, time, message

if __name__ == "__main__":
    lines = [line.strip() for line in open("input.txt", "r")]
    lines.sort()
    print(part1(lines))
