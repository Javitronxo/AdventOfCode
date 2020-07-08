import itertools
from copy import deepcopy
from typing import List

Grid = List[List[str]]


def update_grid(grid: Grid, second_part: bool = False) -> Grid:
    next_grid = deepcopy(grid)
    grid_range = range(len(grid))
    for i, j in itertools.product(grid_range, repeat=2):
        if second_part and (i, j) in [(0, 0), (0, len(grid) - 1), (len(grid) - 1, 0), (len(grid) - 1, len(grid) - 1)]:
            continue
        neighbors = list()
        for i_0, j_0 in itertools.product(range(-1, 2), repeat=2):
            if (i_0 == j_0 == 0) or (i + i_0) < 0 or (i + i_0) >= len(grid) or (j + j_0) < 0 or (j + j_0) >= len(grid):
                continue
            neighbors.append(grid[i + i_0][j + j_0])
        if grid[i][j] == '#' and neighbors.count('#') not in [2, 3]:
            next_grid[i][j] = '.'
        elif grid[i][j] == '.' and neighbors.count('#') == 3:
            next_grid[i][j] = '#'
    return next_grid


def main():
    grid = list()
    with open('day_18_input.txt') as f_in:
        for line in f_in.readlines():
            grid.append(list(line.strip()))

    n_steps = 100
    second_grid = deepcopy(grid)
    second_grid[0][0] = second_grid[0][len(grid) - 1] = second_grid[len(grid) - 1][0] = \
        second_grid[len(grid) - 1][len(grid) - 1] = '#'
    for _ in range(n_steps):
        grid = update_grid(grid)
        second_grid = update_grid(second_grid, second_part=True)

    n_lights = 0
    n_lights_second = 0
    for i in range(len(grid)):
        n_lights += grid[i].count('#')
        n_lights_second += second_grid[i].count('#')

    print(f"Part 1: After {n_steps} steps there are {n_lights} on.")
    print(f"Part 2: After {n_steps} steps there are {n_lights_second} on.")


if __name__ == '__main__':
    main()
