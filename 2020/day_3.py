from typing import List


def get_num_trees(input_map: List[str], slope: List[int]) -> int:
    num_trees = 0
    position = [slope[0], slope[1]]
    while position[0] < len(input_map):
        if input_map[position[0]][position[1]] == "#":
            num_trees += 1
        position = [(position[0] + slope[0]), ((position[1] + slope[1]) % len(input_map[0]))]
    return num_trees


def main():
    with open("day_3_input.txt") as f:
        input_map = list()
        for line in f.readlines():
            input_map.append(line.strip())

    print(f"Part 1: There were {get_num_trees(input_map, [1, 3])} trees")

    slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    total_trees = 1
    for slope in slopes:
        total_trees *= get_num_trees(input_map, slope)
    print(f"Part 2: There were {total_trees} trees")


if __name__ == "__main__":
    main()
