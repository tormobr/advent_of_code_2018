from collections import deque

def part_1():
    marbles = deque([0])
    current_index = 1
    respawn_index = 1
    players = 459
    player_scores = [0]*players
    last_marble = 72103*100
    for i in range(1, last_marble + 1):
        current_player = (i % players)
        if i % 23 == 0:
            marbles.rotate(7)
            player_scores[current_player] += marbles.pop() + i
            marbles.rotate(-1)
            continue

        marbles.rotate(-1)
        marbles.append(i)
        #print(f"{current_player}:::{marbles}")

    print(sorted(player_scores))

    


if __name__ == "__main__":
    print(part_1())
