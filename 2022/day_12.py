import string
import sys
from queue import Queue
from typing import Tuple, Dict, List

Point = Tuple[int, int]


def get_neighbours(point: Point, puzzle_input: Dict[Point, str]) -> List[Point]:
    def get_char_index(p: Point) -> int:
        char = puzzle_input[p]
        if char == "S":
            char = "a"
        elif char == "E":
            char = "z"
        return string.ascii_lowercase.index(char)

    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    char_index = get_char_index(point)
    possibilities = list()
    for v in vectors:
        neighbour = (point[0] + v[0], point[1] + v[1])
        try:
            if get_char_index(neighbour) - char_index <= 1:
                possibilities.append(neighbour)
        except KeyError:
            continue
    return possibilities


def get_path_len(start_point: Point, end_point: Point, puzzle_input: Dict[Point, str]) -> int:
    frontier = Queue()
    frontier.put(start_point)
    came_from = dict()
    came_from[start_point] = None

    while not frontier.empty():
        current = frontier.get()
        for next_point in get_neighbours(current, puzzle_input):
            if next_point not in came_from:
                frontier.put(next_point)
                came_from[next_point] = current

    current = end_point
    path = list()
    while current != start_point:
        path.append(current)
        current = came_from[current]
    return len(path)


def main():
    puzzle_input = dict()
    with open("day12_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.strip()):
                puzzle_input[(i, j)] = char
                if char == "S":
                    start_point = (i, j)
                elif char == "E":
                    end_point = (i, j)

    print(f"Part 1: {get_path_len(start_point, end_point, puzzle_input)}")

    min_hike = sys.maxsize
    for point, char in puzzle_input.items():
        if char in ["a", "S"]:
            try:
                min_hike = min(min_hike, get_path_len(point, end_point, puzzle_input))
            except KeyError:  # There might not be a route from that start point
                continue
    print(f"Part 2: {min_hike}")


if __name__ == "__main__":
    main()
