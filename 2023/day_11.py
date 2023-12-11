import itertools
import sys
from typing import Dict, List, Tuple

UniMap = Dict[Tuple[int, int], str]


def expand_universe(universe_map: UniMap, empty_rows: List[int], empty_cols: List[int], offset: int) -> UniMap:
    expanded_universe = dict()
    for coord in universe_map.keys():
        row = coord[0]
        col = coord[1]
        for i, value in enumerate(empty_rows):
            if row < value:
                row += (offset - 1) * i
                break
        for j, value in enumerate(empty_cols):
            if col < value:
                col += (offset - 1) * j
                break
        expanded_universe[(row, col)] = "#"

    return expanded_universe


def get_distances(universe_map: UniMap) -> List[int]:
    distances = list()
    for x, y in itertools.combinations(universe_map.keys(), 2):
        distances.append(abs(x[0] - y[0]) + abs(x[1] - y[1]))
    return distances


def main():
    universe_map = dict()
    empty_rows = list()
    with open("day_11_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            if "#" not in line:
                empty_rows.append(i)
                continue
            for j, char in enumerate(line.strip()):
                if char == "#":
                    universe_map[(i, j)] = "#"

    empty_cols = [i for i in range(j) if i not in set([point[1] for point in universe_map.keys()])] + [sys.maxsize]
    empty_rows = empty_rows + [sys.maxsize]

    print(f"Part 1: {sum(get_distances(expand_universe(universe_map, empty_rows, empty_cols, offset=2)))}")
    print(f"Part 2: {sum(get_distances(expand_universe(universe_map, empty_rows, empty_cols, offset=1000000)))}")


if __name__ == "__main__":
    main()
