def get_rolls_to_lift(floor_map: dict[tuple[int, int], str]) -> list[tuple[int, int]]:
    vectors = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
    rolls_to_remove = []
    for coord in floor_map.keys():
        rolls = 0
        for vector in vectors:
            new_coord = (coord[0] + vector[0], coord[1] + vector[1])
            if new_coord in floor_map:
                rolls += 1
        if rolls < 4:
            rolls_to_remove.append(coord)
    return rolls_to_remove


def remove_rolls(floor_map: dict[tuple[int, int], str], rolls: list[tuple[int, int]]):
    for roll in rolls:
        floor_map.pop(roll)


def main():
    floor_map = {}
    with open("day_4_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.strip()):
                if char == "@":
                    floor_map[(i, j)] = char

    print(f"Part 1: {len(get_rolls_to_lift(floor_map))}")

    part_2 = 0
    while True:
        rolls = get_rolls_to_lift(floor_map)
        if len(rolls) == 0:
            break
        remove_rolls(floor_map, rolls)
        part_2 += len(rolls)
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
