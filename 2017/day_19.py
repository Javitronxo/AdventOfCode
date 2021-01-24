from typing import List, Tuple


def get(tube_map: List[List[str]], point: Tuple[int, int]) -> str:
    if any(size < 0 for size in point):
        return " "
    try:
        return tube_map[point[0]][point[1]]
    except IndexError:
        return " "


def main():
    tube_map = list()
    with open("day_19_input.txt") as f:
        for line in f.read().splitlines():
            tube_map.append(list(line[1:]))

    current = (0, len(tube_map[0]) - 1)
    square = tube_map[current[0]][current[1]]
    direction = "down"
    directions = {"down": (1, 0), "up": (-1, 0), "right": (0, 1), "left": (0, -1)}
    answer = str()
    steps = 0

    while all(side >= 0 for side in current) and square != " ":
        current = (current[0] + directions[direction][0], current[1] + directions[direction][1])
        square = tube_map[current[0]][current[1]]
        steps += 1
        if square.isalpha():
            answer += square
        elif square == "+":
            if direction in ["down", "up"]:
                direction = "left" if get(tube_map, (current[0], current[1] - 1)) != " " else "right"
            else:
                direction = "up" if get(tube_map, (current[0] - 1, current[1])) != " " else "down"

    print(f"Part 1: {answer}")
    print(f"Part 2: {steps}")


if __name__ == "__main__":
    main()
