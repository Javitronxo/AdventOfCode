VECTORS = [(1, 1), (-1, 1), (1, -1), (-1, -1), (0, -1), (0, 1), (1, 0), (-1, 0)]
EMPTY_SPOT = "."
GEAR_SPOT = "*"


def get_adjacent_numbers(engine_map, coord):
    adjacent_numbers = dict()  # Map of coordinates and values
    for vector in VECTORS:
        new_coord = (coord[0] + vector[0], coord[1] + vector[1])
        if not engine_map[new_coord].isdigit():
            continue

        # We have a digit, get whole number and coordinates
        coordinates_list = [new_coord]
        digit = f"{engine_map[new_coord]}"
        try:
            left = 1
            while (engine_map[(new_coord[0], new_coord[1] + left)]).isdigit():
                digit = f"{digit}{engine_map[(new_coord[0], new_coord[1] + left)]}"
                coordinates_list.append((new_coord[0], new_coord[1] + left))
                left += 1
        except KeyError:
            pass
        try:
            right = 1
            while engine_map[(new_coord[0], new_coord[1] - right)].isdigit():
                digit = f"{engine_map[(new_coord[0], new_coord[1] - right)]}{digit}"
                coordinates_list.append((new_coord[0], new_coord[1] - right))
                right += 1
        except KeyError:
            pass
        coordinates_list.sort()
        adjacent_numbers[tuple(coordinates_list)] = int(digit)

    return adjacent_numbers


def main():
    engine_map = dict()
    with open("day_3_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.strip()):
                engine_map[(i, j)] = char

    part_numbers = dict()
    gear_products = list()
    for coord, value in engine_map.items():
        is_part = value != EMPTY_SPOT and not value.isdigit()
        if not is_part:
            continue

        adjacent_numbers = get_adjacent_numbers(engine_map, coord)
        # Get all adjacent numbers for part 1
        for coordinates, number in adjacent_numbers.items():
            part_numbers[coordinates] = number
        # Get all gears for part 2
        if value == GEAR_SPOT and len(adjacent_numbers.keys()) == 2:
            values = list(adjacent_numbers.values())
            gear_products.append(values[0] * values[1])

    print(f"Part 1: {sum(part_numbers.values())}")
    print(f"Part 2: {sum(gear_products)}")


if __name__ == "__main__":
    main()
