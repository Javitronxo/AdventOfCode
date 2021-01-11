from typing import Tuple

Point = Tuple[int, int]


def get_distance(point: Point) -> int:
    dx = abs(point[0])
    dy = abs(point[1])
    return dx + max(0, ((dy - dx) // 2))


def main():
    with open("day_11_input.txt") as f:
        puzzle_input = f.read().split(",")

    position = (0, 0)
    max_distance = 0
    for direction in puzzle_input:
        if direction == "n":
            position = (position[0], position[1] + 2)
        elif direction == "nw":
            position = (position[0] - 1, position[1] + 1)
        elif direction == "sw":
            position = (position[0] - 1, position[1] - 1)
        elif direction == "s":
            position = (position[0], position[1] - 2)
        elif direction == "se":
            position = (position[0] + 1, position[1] - 1)
        elif direction == "ne":
            position = (position[0] + 1, position[1] + 1)
        max_distance = max(max_distance, get_distance(position))
    print(f"Part 1: {get_distance(position)}")
    print(f"Part 2: {max_distance}")


if __name__ == "__main__":
    main()
