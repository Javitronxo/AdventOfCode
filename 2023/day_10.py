from typing import List, Tuple


def find_initial_direction(maze: List[str], start: Tuple[int, int]) -> Tuple[int, int]:
    valid = {
        (1, 0): {"|", "J", "L"},
        (0, -1): {"F", "L", "-"},
        (-1, 0): {"|", "7", "F"},
        (0, 1): {"J", "7", "-"},
    }
    for (offset_row, offset_col), valid_pipes in valid.items():
        new_row, new_col = start[0] + offset_row, start[1] + offset_col
        if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and maze[new_row][new_col] in valid_pipes:
            return offset_row, offset_col


def find_loop(maze: List[str], start: Tuple[int, int]):
    mult = {"L": 1, "7": 1, "J": -1, "F": -1}
    dir_row, dir_col = find_initial_direction(maze, start)
    current = start
    loop = []
    while current != start or not loop:
        loop.append(current)
        row, col = current
        current = (row + dir_row, col + dir_col)
        pipe = maze[current[0]][current[1]]
        if pipe in {"J", "L", "F", "7"}:
            dir_row, dir_col = dir_col * mult[pipe], dir_row * mult[pipe]
    return loop


def part_two(loop: List[Tuple[int, int]]) -> int:
    """
    How to get the enclosed points:
        Shoelace formula: https://en.wikipedia.org/wiki/Shoelace_formula
        Pick's theorem: https://en.wikipedia.org/wiki/Pick%27s_theorem
    """
    x, y = zip(*loop)
    area = 0.5 * abs(sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(loop))))
    return int(area - 0.5 * len(loop) + 1)


def main():
    maze = list()
    start_point = None
    with open("day_10_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            maze.append(line.strip())
            if "S" in line:
                start_point = (i, line.index("S"))

    loop = find_loop(maze, start_point)
    print(f"Part 1: {len(loop) // 2}")
    print(f"Part 2: {part_two(loop)}")


if __name__ == "__main__":
    main()
