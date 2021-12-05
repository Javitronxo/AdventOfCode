from collections import defaultdict
from typing import Dict, List, Tuple


class Vent:
    def __init__(self, start: Tuple[int], end: Tuple[int]):
        self.start = start
        self.end = end
        self.path = self._get_path()

    def _get_path(self) -> List[Tuple[int]]:
        vector_x = 1 if self.end[0] > self.start[0] else -1 if self.end[0] < self.start[0] else 0
        vector_y = 1 if self.end[1] > self.start[1] else -1 if self.end[1] < self.start[1] else 0
        point = self.start
        path = [point]
        while point != self.end:
            point = (point[0] + vector_x, point[1] + vector_y)
            path.append(point)
        return path

    @property
    def is_straight(self) -> bool:
        return self.start[0] == self.end[0] or self.start[1] == self.end[1]


def get_vents_map(vents: List[Vent]) -> Dict[Tuple[int], int]:
    sea_map = defaultdict(int)
    for vent in vents:
        for point in vent.path:
            sea_map[point] += 1
    return sea_map


def main():
    vents = list()
    with open("day_5_input.txt") as f:
        for line in f.readlines():
            p0, p1 = line.split(" -> ")
            vent = Vent(
                tuple(int(n) for n in p0.split(",")),
                tuple(int(n) for n in p1.split(",")),
            )
            vents.append(vent)

    straight_vents = [vent for vent in vents if vent.is_straight]
    sea_map = get_vents_map(straight_vents)
    print(f"Part 1: {sum(1 for n in sea_map.values() if n > 1)}")

    sea_map = get_vents_map(vents)
    print(f"Part 2: {sum(1 for n in sea_map.values() if n > 1)}")


if __name__ == '__main__':
    main()
