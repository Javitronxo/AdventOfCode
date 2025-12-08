from functools import cache
from queue import Queue

Point = tuple[int, int]


def solve_part_1(manifold: dict[Point, str], start_point: Point, max_row: int) -> int:
    beams = Queue()
    beams.put(start_point)
    reached = set()
    reached.add(start_point)
    result = 0
    while not beams.empty():
        current = beams.get()
        next_point = (current[0] + 1, current[1])
        if next_point[0] >= max_row:
            break
        elif next_point in reached:
            continue
        elif manifold[next_point] == "^":
            beams.put((next_point[0], next_point[1] + 1))
            beams.put((next_point[0], next_point[1] - 1))
            result += 1
        else:
            beams.put(next_point)
        reached.add(next_point)
    return result


def solve_part_2(manifold: dict[Point, str], start_point: Point, max_row: int) -> int:
    @cache
    def dfs(p: Point):
        if p[0] == max_row:
            return 1
        if manifold[(p[0], p[1])] == "^":
            return dfs((p[0] + 1, p[1] - 1)) + dfs((p[0] + 1, p[1] + 1))
        return dfs((p[0] + 1, p[1]))

    return dfs(start_point)


def main():
    manifold = {}
    with open("day_7_input.txt", "r") as f:
        lines = f.readlines()
        for row, line in enumerate(lines):
            for col, char in enumerate(line.strip()):
                manifold[(row, col)] = char
                if char == "S":
                    start_point = (row, col)
        max_row = row

    print(f"Part 1: {solve_part_1(manifold, start_point, max_row)}")
    print(f"Part 2: {solve_part_2(manifold, start_point, max_row)}")


if __name__ == "__main__":
    main()
