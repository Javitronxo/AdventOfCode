import re
from copy import deepcopy


def main():
    grid = set()
    fold_instructions = list()
    with open("day_13_input.txt") as f:
        get_points = True
        for line in f.readlines():
            if not len(line.strip()):
                get_points = False
                continue
            elif get_points:
                grid.add(tuple(int(x) for x in line.split(",")))
            else:
                axis, n = re.findall(r"fold along (\w)=(\d+)", line)[0]
                fold_instructions.append((axis, int(n)))

    for i, instruction in enumerate(fold_instructions):
        axis, n = instruction
        folded_grid = set()
        for point in grid:
            if axis == "x" and point[0] > n:
                folded_grid.add((2 * n - point[0], point[1]))
            elif axis == "y" and point[1] > n:
                folded_grid.add((point[0], 2 * n - point[1]))
            else:
                folded_grid.add(point)
        if i == 0:
            print(f"Part 1: {len(folded_grid)}")
        grid = deepcopy(folded_grid)

    x_points = [point[0] for point in grid]
    y_points = [point[1] for point in grid]
    min_x, max_x = min(x_points), max(x_points)
    min_y, max_y = min(y_points), max(y_points)
    paper = [[" " for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for point in grid:
        paper[point[1] - min_y][point[0] - min_x] = "#"
    print(f"Part 2:")
    for row in paper:
        print("".join(row))


if __name__ == "__main__":
    main()
