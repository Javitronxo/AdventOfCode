from copy import deepcopy
from typing import List

floor_map = List[List[str]]


def apply_rules(input_map: floor_map, part: int) -> floor_map:
    max_occupied = 4 if part == 1 else 5
    new_map = deepcopy(input_map)
    vectors = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]

    for i, row in enumerate(input_map):
        for j, seat in enumerate(row):
            if seat == ".":
                new_map[i][j] = seat

            occupied_seats = 0
            if part == 1:
                for vector in vectors:
                    if (
                        0 <= (i + vector[0]) < len(input_map)
                        and 0 <= (j + vector[1]) < len(row)
                        and input_map[i + vector[0]][j + vector[1]] == "#"
                    ):
                        occupied_seats += 1
            elif part == 2:
                for vector in vectors:
                    scale = 1
                    while True:
                        if 0 <= (i + vector[0] * scale) < len(input_map) and 0 <= (j + vector[1] * scale) < len(row):
                            seat_seen = input_map[i + vector[0] * scale][j + vector[1] * scale]
                            if seat_seen == "#":
                                occupied_seats += 1
                                break
                            elif seat_seen == "L":
                                break
                            elif seat_seen == ".":
                                scale += 1
                        else:
                            break

            if seat == "L" and not occupied_seats:
                new_map[i][j] = "#"
            elif seat == "#" and occupied_seats >= max_occupied:
                new_map[i][j] = "L"

    return new_map


def main():
    input_map_original = list()
    with open("day_11_input.txt") as f:
        for line in f.read().splitlines():
            input_map_original.append([char for char in line])

    for i in [1, 2]:
        input_map = deepcopy(input_map_original)
        while True:
            new_map = apply_rules(input_map, part=i)
            occupied_seats = sum(row.count("#") for row in new_map)
            if new_map == input_map:
                break
            else:
                input_map = new_map
        print(f"Part {i}: We have {occupied_seats} occupied seats")


if __name__ == "__main__":
    main()
