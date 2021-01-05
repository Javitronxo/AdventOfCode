from copy import deepcopy
from itertools import permutations
from queue import Queue
from sys import maxsize
from typing import Dict, List, Tuple

Point = Tuple[int, int]


def get_neighbours(point: Point, floor) -> List[Point]:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    possibilities = list()
    for vector in directions:
        new_point = (point[0] + vector[0], point[1] + vector[1])
        if all(coord >= 0 for coord in new_point) and floor[new_point] != "#":
            possibilities.append(new_point)
    return possibilities


def get_path_len(origin: Point, destination: Point, came_from: Dict[Point, Point]) -> int:
    current = destination
    path = list()
    while current != origin:
        path.append(current)
        current = came_from[current]
    return len(path)


def get_steps(floor: Dict[Point, str], point_locations: Dict[int, Point], origin_number: int) -> int:
    steps = 0
    origin = point_locations.pop(origin_number)
    if not point_locations:
        return steps

    came_from = get_directions(origin, floor)
    path_lengths = dict()
    for number, point in point_locations.items():
        path_len = get_path_len(origin, point, came_from)
        path_lengths[number] = path_len
    min_paths = {
        number: path_len for number, path_len in path_lengths.items() if path_len == min(path_lengths.values())
    }
    steps += min(path_lengths.values())

    new_steps = list()
    for number in min_paths.keys():
        new_steps.append(get_steps(floor, deepcopy(point_locations), number))
    steps += min(new_steps)

    return steps


def get_directions(origin: Point, floor: Dict[Point, str]) -> Dict[Point, Point]:
    frontier = Queue()
    frontier.put(origin)
    came_from = dict()
    came_from[origin] = None
    while not frontier.empty():
        current = frontier.get()
        for next_point in get_neighbours(current, floor):
            if next_point not in came_from:
                frontier.put(next_point)
                came_from[next_point] = current
    return came_from


def main():
    floor = dict()
    point_locations = dict()
    with open("day_24_input.txt") as f:
        for y, line in enumerate(f.read().splitlines()):
            for x, char in enumerate(line):
                if char.isdigit():
                    point_locations[int(char)] = (x, y)
                floor[(x, y)] = char

    print(f"Part 1: {get_steps(floor, deepcopy(point_locations), 0)}")

    # Brute force it by checking all possible paths
    all_came_from = dict()
    for i in range(len(point_locations)):
        all_came_from[i] = get_directions(point_locations[i], floor)

    min_path = maxsize
    for p in permutations(range(1, len(point_locations))):
        path = 0
        route = [0] + list(p) + [0]
        for i in range(len(route) - 1):
            came_from = all_came_from[route[i]]
            path += get_path_len(point_locations[route[i]], point_locations[route[i + 1]], came_from)
            if path > min_path:
                break
        min_path = min(path, min_path)

    print(f"Part 2: {min_path}")


if __name__ == "__main__":
    main()
