from queue import PriorityQueue
from typing import Dict, Tuple

Point = Tuple[int, int]


def dijkstra_cost(start: Point, end: Point, cave_map: Dict[Point, int]) -> int:
    # Shamelessly stolen from: https://www.redblobgames.com/pathfinding/a-star/introduction.html
    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    frontier = PriorityQueue()
    frontier.put(start)
    came_from, cost_so_far = dict(), dict()
    came_from[start], cost_so_far[start] = None, 0
    while not frontier.empty():
        current = frontier.get()
        if current == end:
            break
        for v in vectors:
            if (new_point := (current[0] + v[0], current[1] + v[1])) not in cave_map:
                continue
            new_cost = cost_so_far[current] + cave_map[new_point]
            if new_point not in cost_so_far or new_cost < cost_so_far[new_point]:
                cost_so_far[new_point] = new_cost
                frontier.put(new_point)
                came_from[new_point] = current
    return cost_so_far[end]


def main():
    cave_map = dict()
    with open("day_15_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.strip()):
                cave_map[(i, j)] = int(char)

    start, end = (0, 0), (i, j)
    print(f"Part 1: {dijkstra_cost(start, end, cave_map)}")

    max_x = max(point[0] for point in cave_map.keys()) + 1
    max_y = max(point[1] for point in cave_map.keys()) + 1
    new_cave_map = dict()
    for i in range(5):
        for j in range(5):
            for point, value in cave_map.items():
                if (new_value := value + i + j) > 9:
                    new_value = new_value % 9
                new_cave_map[(point[0] + max_x * i, point[1] + max_y * j)] = new_value
    end = (max(point[0] for point in new_cave_map.keys()), max(point[0] for point in new_cave_map.keys()))
    print(f"Part 2: {dijkstra_cost(start, end, new_cave_map)}")


if __name__ == "__main__":
    main()
