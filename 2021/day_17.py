from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int

    def __add__(self, c: Coordinates) -> Coordinates:
        self.x += c.x
        self.y += c.y
        return self


def main():
    with open("day_17_input.txt") as f:
        (x_min, x_max, y_min, y_max) = (int(i) for i in re.findall(r"-?\d+", f.read().strip()))

    # Brute force approach
    # We are going to scan all potential points since we need them for part 2, and retrieve the max height for part 1
    x_range = max(abs(x_min), abs(x_max))
    x_step = x_max // abs(x_max)
    y_range = max(abs(y_min), abs(y_max))
    shots = dict()
    for vel_x in range(0, x_range + 1, x_step):
        for vel_y in range(-y_range, y_range + 1):
            pos = Coordinates(0, 0)
            vel = Coordinates(vel_x, vel_y)
            max_height = 0
            while pos.x <= x_max and pos.y >= y_min:
                pos += vel
                vel.x -= 1 if vel.x > 0 else -1 if vel.x < 0 else 0
                vel.y -= 1
                max_height = max(max_height, pos.y)
                if x_min <= pos.x <= x_max and y_min <= pos.y <= y_max:
                    shots[(vel_x, vel_y)] = max_height
                    break
    print(f"Part 1: {max(shots.values())}")
    print(f"Part 2: {len(shots)}")


if __name__ == "__main__":
    main()
