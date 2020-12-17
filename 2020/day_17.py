from collections import defaultdict
from itertools import product
from typing import Any, List, Tuple

Point = Tuple[int, int, int]
HyperPoint = Tuple[int, int, int, int]
SparseMap = List[Any[Point, HyperPoint]]


def boot_machine(sparse_map: SparseMap, n_cycles: int) -> SparseMap:
    for _ in range(n_cycles):
        active_neighbours = defaultdict(int)
        # Update number of active neighbours around each active cube
        for p in sparse_map:
            for p0 in product((-1, 0, 1), repeat=len(p)):
                if p0 == tuple(0 for _ in range(len(p))):
                    continue
                active_neighbours[tuple(i + i0 for i, i0 in zip(p, p0))] += 1
        # Generate next map with active cubes
        next_map = list()
        for cube in active_neighbours:
            if cube not in sparse_map and active_neighbours[cube] == 3:
                next_map.append(cube)
            elif cube in sparse_map and active_neighbours[cube] in [2, 3]:
                next_map.append(cube)
        sparse_map = next_map
    return sparse_map


def main():
    with open("day_17_input.txt") as f:
        input_lines = f.read().splitlines()
    n_cycles = 6

    # Sparse map with only active points
    input_map = [
        (x, y, 0)
        for y, line in enumerate(input_lines)
        for x, cube in enumerate(line)
        if cube == "#"
    ]
    print(f"Part 1: {len(boot_machine(input_map, n_cycles))}")

    input_map = [
        (x, y, 0, 0)
        for y, line in enumerate(input_lines)
        for x, cube in enumerate(line)
        if cube == "#"
    ]
    print(f"Part 2: {len(boot_machine(input_map, n_cycles))}")


if __name__ == "__main__":
    main()
