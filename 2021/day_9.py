import math


def main():
    sea_map = dict()
    with open("day_9_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.strip()):
                sea_map[(i, j)] = int(char)

    low_points = dict()
    vectors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for point, value in sea_map.items():
        neighbours = [
            sea_map[new_point]
            for vector in vectors
            if (new_point := (point[0] + vector[0], point[1] + vector[1])) in sea_map
        ]
        if value < min(neighbours):
            low_points[point] = value
    print(f"Part 1: {sum(i + 1 for i in low_points.values())}")

    basins = list()
    for point, value in low_points.items():
        neighbours = set([
            new_point
            for vector in vectors
            if (
                    (new_point := (point[0] + vector[0], point[1] + vector[1])) in sea_map and
                    sea_map[new_point] > value and
                    sea_map[new_point] != 9
            )
        ])
        basin = {point}.union(neighbours)
        while neighbours:
            point = neighbours.pop()
            new_neighbours = [
                new_point
                for vector in vectors
                if (
                        (new_point := (point[0] + vector[0], point[1] + vector[1])) in sea_map and
                        new_point not in basin and
                        sea_map[new_point] > value and
                        sea_map[new_point] != 9
                )
            ]
            basin = basin.union(set(new_neighbours))
            neighbours = neighbours.union(set(new_neighbours))
        basins.append(len(set(basin)))
    print(f"Part 2: {math.prod(sorted(basins, reverse=True)[:3])}")


if __name__ == "__main__":
    main()
