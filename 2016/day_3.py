import re
from typing import List


def is_possible_triangle(sides: List[int]) -> bool:
    larger_side = max(sides)
    sides.remove(larger_side)
    return sum(sides) > larger_side


def main():
    triangle_candidates = list()
    with open('day_3_input.txt') as f_in:
        for line in f_in.readlines():
            candidate = re.search(r'(\d+)\s+(\d+)\s+(\d+)', line).groups()
            triangle_candidates.append([int(i) for i in candidate])

    possible_triangles = 0
    for candidate in triangle_candidates:
        if is_possible_triangle(candidate.copy()):
            possible_triangles += 1
    print(f"Part 1: We have {possible_triangles} possible triangles")

    possible_triangles = 0
    sides = list()
    for j in range(len(triangle_candidates[0])):
        for i in range(len(triangle_candidates)):
            sides.append(triangle_candidates[i][j])
            if len(sides) == 3:
                if is_possible_triangle(sides):
                    possible_triangles += 1
                sides = list()
    print(f"Part 2: We have {possible_triangles} possible triangles")


if __name__ == '__main__':
    main()
