from collections import defaultdict
from copy import deepcopy


def main():
    original_fish_map = defaultdict(int)
    with open("day_6_input.txt") as f:
        for time in [int(x) for x in f.read().split(",")]:
            original_fish_map[time] += 1

    part_iterations = {1: 80, 2: 256}
    for part, iterations in part_iterations.items():
        fish_map = deepcopy(original_fish_map)
        for _ in range(iterations):
            new_fish_map = defaultdict(int)
            for time, fish in fish_map.items():
                if time == 0:
                    new_fish_map[6] += fish
                    new_fish_map[8] += fish
                else:
                    new_fish_map[time - 1] += fish
            fish_map = deepcopy(new_fish_map)
        print(f"Part {part}: {sum(value for value in fish_map.values())}")


if __name__ == "__main__":
    main()
