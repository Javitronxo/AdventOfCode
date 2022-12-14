from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Point:
    x: int
    y: int

    def __hash__(self) -> int:
        return hash(f"{self.x},{self.y}")

    def points_in_between(self, other: Point) -> List[Point]:
        points = [self, other]
        if self.x == other.x:
            if self.y < other.y:
                for y in range(self.y + 1, other.y):
                    points.append(Point(self.x, y))
            else:
                for y in range(other.y + 1, self.y):
                    points.append(Point(self.x, y))
        elif self.x < other.x:
            for x in range(self.x + 1, other.x):
                points.append(Point(x, self.y))
        else:
            for x in range(other.x + 1, self.x):
                points.append(Point(x, self.y))
        return points


def drop_sand(cave_map: Dict[Point, str], floor: int = None) -> bool:
    sand_grain = Point(500, 0)
    if sand_grain in cave_map:
        return False
    lowest_y = floor if floor else max(point.y for point in cave_map.keys())
    while sand_grain.y < lowest_y:
        next_down = Point(sand_grain.x, sand_grain.y + 1)
        next_left = Point(sand_grain.x - 1, sand_grain.y + 1)
        next_right = Point(sand_grain.x + 1, sand_grain.y + 1)
        if floor and sand_grain.y + 1 == lowest_y:
            cave_map[next_down] = "#"
            cave_map[next_left] = "#"
            cave_map[next_right] = "#"
        if next_down in cave_map and next_left in cave_map and next_right in cave_map:
            cave_map[sand_grain] = "o"
            return True
        if next_down not in cave_map:
            sand_grain = next_down
        elif next_left not in cave_map:
            sand_grain = next_left
        else:
            sand_grain = next_right
    return False


def main():
    cave_map = dict()
    with open("day14_input.txt") as f:
        for line in f.readlines():
            points = [Point(int(part[0]), int(part[1])) for part in [chunk.split(",") for chunk in line.split(" -> ")]]
            for i in range(1, len(points)):
                for point in points[i - 1].points_in_between(points[i]):
                    cave_map[point] = "#"
    cave_map_copy = deepcopy(cave_map)

    rounds = 0
    while drop_sand(cave_map):
        rounds += 1
    print(f"Part 1: {rounds}")

    rounds = 0
    floor = max(point.y for point in cave_map_copy.keys()) + 2
    while drop_sand(cave_map_copy, floor):
        rounds += 1
    print(f"Part 2: {rounds}")


if __name__ == "__main__":
    main()
