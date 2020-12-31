from typing import List, Tuple
from queue import Queue

Point = Tuple[int, int]


def get_neighbours(point: Point, magic_number: int) -> List[Point]:
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    possibilities = list()
    for vector in directions:
        new_point = (point[0] + vector[0], point[1] + vector[1])
        if all(coord >= 0 for coord in new_point):
            x, y = new_point
            n_ones = bin((x * x + 3 * x + 2 * x * y + y + y * y) + magic_number).count("1")
            if n_ones % 2 == 0:
                possibilities.append(new_point)
    return possibilities


def main():
    with open("day_13_input.txt") as f:
        puzzle_input = int(f.read())

    origin = (1, 1)
    destination = (31, 39)

    # From: https://www.redblobgames.com/pathfinding/a-star/introduction.html
    frontier = Queue()
    frontier.put(origin)
    came_from = dict()
    came_from[origin] = None

    while not frontier.empty():
        current = frontier.get()
        for next_point in get_neighbours(current, puzzle_input):
            if next_point not in came_from:
                frontier.put(next_point)
                came_from[next_point] = current

    current = destination
    path = list()
    while current != origin:
        path.append(current)
        current = came_from[current]
    print(f"Part 1: {len(path)}")

    locations = 0
    for point in came_from:
        current = point
        for _ in range(50 + 1):
            if current == origin:
                locations += 1
                break
            current = came_from[current]
    print(f"Part 2: {locations}")


if __name__ == "__main__":
    main()
