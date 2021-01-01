import re
from copy import deepcopy
from dataclasses import dataclass
from typing import List


@dataclass
class Disc:
    number: int
    n_positions: int
    initial_time: int
    position: int


def solve_game(discs: List[Disc]) -> int:
    time = 0
    while any(((disc.position + disc.number) % disc.n_positions) != 0 for disc in discs):
        for disc in discs:
            disc.position = (disc.position + 1) % disc.n_positions
        time += 1
    return time


def main():
    discs = list()
    line_pattern = r"Disc #(\d+) has (\d+) positions; at time=(\d+), it is at position (\d+)."
    with open("day_15_input.txt") as f:
        for line in f.readlines():
            disc_info = re.search(line_pattern, line).groups()
            discs.append(Disc(int(disc_info[0]), int(disc_info[1]), int(disc_info[2]), int(disc_info[3])))

    print(f"Part 1: {solve_game(deepcopy(discs))}")

    discs.append(Disc(number=(len(discs) + 1), n_positions=11, initial_time=0, position=0))
    print(f"Part 2: {solve_game(discs)}")


if __name__ == "__main__":
    main()
