def main():
    with open("day_3_input.txt") as f:
        puzzle_input = int(f.read())

    steps = 0
    max_number = 1
    while max_number < puzzle_input:
        steps += 1
        max_number += steps * 8

    last_square_side = (steps * 8) // 4
    half_side = last_square_side // 2
    surplus = max_number - puzzle_input
    while surplus > last_square_side:
        surplus -= last_square_side

    answer = abs((last_square_side - surplus) - half_side) + half_side
    print(f"Part 1: {answer}")

    value = 1
    address = (0, 0)
    memory_map = {address: value}
    moves = {
        "right": (1, 0),
        "left": (-1, 0),
        "up": (0, 1),
        "down": (0, -1),
    }
    goes = "right"
    directions = [
        (-1, 1),
        (0, 1),
        (1, 1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]

    while value < puzzle_input:
        value = 0
        address = (address[0] + moves[goes][0], address[1] + moves[goes][1])
        adjacent_addresses = [(address[0] + x, address[1] + y) for x, y in directions]
        for adjacent in adjacent_addresses:
            try:
                value += memory_map[adjacent]
            except KeyError:
                pass

        if goes == "right" and address[0] > max(memory_map.keys(), key=lambda x: x[0])[0]:
            goes = "up"
        elif goes == "up" and address[1] > max(memory_map.keys(), key=lambda x: x[1])[1]:
            goes = "left"
        elif goes == "left" and address[0] < min(memory_map.keys(), key=lambda x: x[0])[0]:
            goes = "down"
        elif goes == "down" and address[1] < min(memory_map.keys(), key=lambda x: x[1])[1]:
            goes = "right"

        memory_map[address] = value

    print(f"Part 2: {value}")


if __name__ == "__main__":
    main()
