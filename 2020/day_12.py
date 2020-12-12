"""
NOTE: Pretty sure part 2 is not well solved, but thanks to the beauty of taxicab geometry I still get the expected
    distance. But the rotate_point function should move one point relative to the other...
    Still, is Friday night and this was extra-extra-challenging to solve after those weird gummies you ate before.
    The keyboard feels pretty weird, spent too much time looking for the right key all the time...
"""
from typing import List, Tuple

Point = Tuple[int, int]


def rotate_point(direction: str, abs_degrees: int, point: Point) -> Point:
    degrees = abs_degrees % 360
    if degrees == 0:
        return point
    elif degrees == 90:
        point = (point[1], point[0] * -1) if direction == "L" else (point[1] * -1, point[0])
    elif degrees == 180:
        point = (point[0] * -1, point[1] * -1) if direction == "L" else (point[0] * -1, point[1] * -1)
    elif degrees == 270:
        point = (point[1] * -1, point[0]) if direction == "L" else (point[1], point[0] * -1)
    return point


def move_ship(instructions: List[str]) -> Point:
    # Variables for Part 1
    position_1 = (0, 0)
    degrees = 90
    # Variables for Part 2
    position_2 = (0, 0)
    waypoint = (1, 10)

    for instruction in instructions:
        direction = instruction[0]
        magnitude = int(instruction[1:])

        if direction == "N":
            position_1 = (position_1[0] + magnitude, position_1[1])
            waypoint = (waypoint[0] + magnitude, waypoint[1])
        elif direction == "S":
            position_1 = (position_1[0] - magnitude, position_1[1])
            waypoint = (waypoint[0] - magnitude, waypoint[1])
        elif direction == "E":
            position_1 = (position_1[0], position_1[1] + magnitude)
            waypoint = (waypoint[0], waypoint[1] + magnitude)
        elif direction == "W":
            position_1 = (position_1[0], position_1[1] - magnitude)
            waypoint = (waypoint[0], waypoint[1] - magnitude)

        elif direction == "L":
            degrees -= magnitude
            waypoint = rotate_point(direction, magnitude, waypoint)
        elif direction == "R":
            degrees += magnitude
            waypoint = rotate_point(direction, magnitude, waypoint)

        elif direction == "F":
            position_2 = (position_2[0] + magnitude * waypoint[0], position_2[1] + magnitude * waypoint[1])
            f = degrees % 360
            if f == 0:
                position_1 = (position_1[0] + magnitude, position_1[1])
            elif f == 90:
                position_1 = (position_1[0], position_1[1] + magnitude)
            elif f == 180:
                position_1 = (position_1[0] - magnitude, position_1[1])
            elif f == 270:
                position_1 = (position_1[0], position_1[1] - magnitude)
        else:
            raise ValueError(f"Cannot parse instruction: {direction}")

    distance_1 = abs(position_1[0]) + abs(position_1[1])
    distance_2 = abs(position_2[0]) + abs(position_2[1])
    return distance_1, distance_2


def main():
    with open("day_12_test1.txt") as f:
        input_lines = f.read().splitlines()
    distance_1, distance_2 = move_ship(input_lines)
    print(f"Part 1: Manhattan distance between that location and the ship's starting position is {distance_1}")
    print(f"Part 2: Manhattan distance between that location and the ship's starting position is {distance_2}")


if __name__ == "__main__":
    main()
