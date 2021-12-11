from typing import Dict, List, Tuple

Point = Tuple[int, int]


def update_point(sea_map: Dict[Point, int], point: Point, flashes: List[Point], flashed: List[Point]):
    sea_map[point] += 1
    if sea_map[point] > 9:
        sea_map[point] = 0
        flashes.append(point)
        flashed.append(point)


def main():
    sea_map = dict()
    with open("day_11_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.strip()):
                sea_map[(i, j)] = int(char)

    steps, num_flashes, steps_part_one = 0, 0, 100
    directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
    while True:
        flashes, flashed = list(), list()
        for point in sea_map.keys():
            update_point(sea_map, point, flashes, flashed)
        while flashes:
            point = flashes.pop()
            for direction in directions:
                neighbor = (point[0] + direction[0], point[1] + direction[1])
                if neighbor in flashed or neighbor not in sea_map:
                    continue
                update_point(sea_map, neighbor, flashes, flashed)
        num_flashes += len(flashed)
        steps += 1
        if steps == steps_part_one:
            print(f"Part 1: {num_flashes}")
        if len(flashed) == len(sea_map):
            print(f"Part 2: {steps}")
            break


if __name__ == "__main__":
    main()
