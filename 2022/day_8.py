from functools import reduce


def main():
    forrest = dict()
    max_row = 0
    max_col = 0

    with open("day8_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            max_row = i
            for j, char in enumerate(line.strip()):
                forrest[(i, j)] = int(char)
                max_col = i

    visible_trees = 0
    max_scenic_score = 0
    for coord, tree in forrest.items():
        if (
            coord[0] in [0, max_row]
            or coord[1] in [0, max_col]
            or max([forrest[(i, coord[1])] for i in range(0, coord[0])]) < tree
            or max([forrest[(i, coord[1])] for i in range(coord[0] + 1, max_row + 1)]) < tree
            or max([forrest[(coord[0], j)] for j in range(0, coord[1])]) < tree
            or max([forrest[(coord[0], j)] for j in range(coord[1] + 1, max_col + 1)]) < tree
        ):
            visible_trees += 1

        tree_view = [0, 0, 0, 0]
        for i in reversed(range(0, coord[0])):
            tree_view[0] += 1
            if forrest[(i, coord[1])] >= tree:
                break
        for i in range(coord[0] + 1, max_col + 1):
            tree_view[1] += 1
            if forrest[(i, coord[1])] >= tree:
                break
        for j in reversed(range(0, coord[1])):
            tree_view[2] += 1
            if forrest[(coord[0], j)] >= tree:
                break
        for j in range(coord[1] + 1, max_col + 1):
            tree_view[3] += 1
            if forrest[(coord[0], j)] >= tree:
                break
        max_scenic_score = max(max_scenic_score, reduce(lambda x, y: x * y, tree_view))

    print(f"Part 1: {visible_trees}")
    print(f"Part 2: {max_scenic_score}")


if __name__ == "__main__":
    main()
