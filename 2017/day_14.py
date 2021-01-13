from collections import deque
from queue import Queue
from typing import List, Tuple, Set

Point = Tuple[int, int]


def get_knot_hash(lengths: List[int]) -> str:
    numbers_deque = deque(range(256))
    total_rounds = 64
    current_position = 0
    skip_size = 0
    for _ in range(total_rounds):
        for length in lengths:
            numbers_list = list(numbers_deque)
            numbers_deque = deque(numbers_list[:length][::-1] + numbers_list[length:])
            rotation = (length + skip_size) % len(numbers_deque)
            current_position += length + skip_size
            numbers_deque.rotate(-rotation)
            skip_size += 1
    numbers_deque.rotate(current_position)

    knot_hash_numbers = list()
    while numbers_deque:
        xor_result = 0
        for _ in range(16):
            xor_result = xor_result ^ numbers_deque.popleft()
        knot_hash_numbers.append(xor_result)

    knot_hash = str()
    for n in knot_hash_numbers:
        knot_hash += hex(n)[2:].zfill(2)
    return knot_hash


def get_adjacent(point: Point, grid: List[str]) -> Set[Point]:
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    adjacent = set()
    for direction in directions:
        i, j = (point[0] + direction[0], point[1] + direction[1])
        if 0 <= i < len(grid) and 0 <= j < len(grid) and grid[i][j] == "1":
            adjacent.add((i, j))
    return adjacent


def get_points_in_group(current: Point, grid: List[str]) -> Set[Point]:
    queue = Queue()
    queue.put(current)
    visited = set()
    visited.add(current)
    while not queue.empty():
        point = queue.get()
        for adjacent in get_adjacent(point, grid):
            if adjacent not in visited:
                queue.put(adjacent)
                visited.add(adjacent)
    return visited


def main():
    with open("day_14_input.txt") as f:
        puzzle_input = f.read().strip()

    hashes = list()
    for i in range(128):
        lengths = list()
        for char in f"{puzzle_input}-{i}":
            lengths.append(ord(char))
        lengths.extend([17, 31, 73, 47, 23])
        dense_hash = get_knot_hash(lengths)
        hashes.append(dense_hash)

    grid = list()
    for knot_hash in hashes:
        bin_hash = str()
        for char in knot_hash:
            bin_hash += bin(int(char, 16))[2:].zfill(4)
        grid.append(bin_hash)
    print(f"Part 1: {sum(row.count('1') for row in grid)}")

    groups = list()
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == "1":
                current = (i, j)
                if all([current not in group for group in groups]):
                    visited = get_points_in_group(current, grid)
                    groups.append(visited)
    print(f"Part 2: {len(groups)}")


if __name__ == "__main__":
    main()
