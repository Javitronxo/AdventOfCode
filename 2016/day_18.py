from typing import List


def populate_room(puzzle_input: str, room_length: int) -> List[List[str]]:
    safe_tile = "."
    trap_tile = "^"
    room = [list(puzzle_input)]

    for i in range(room_length - 1):
        row = list()
        for j in range(len(puzzle_input)):
            left_tile = room[i][j - 1] if j - 1 >= 0 else safe_tile
            center_tile = room[i][j]
            try:
                right_tile = room[i][j + 1]
            except IndexError:
                right_tile = safe_tile

            new_tile = safe_tile
            if (
                (left_tile == center_tile == trap_tile and right_tile == safe_tile)
                or (center_tile == right_tile == trap_tile and left_tile == safe_tile)
                or (left_tile == trap_tile and right_tile == center_tile == safe_tile)
                or (right_tile == trap_tile and left_tile == center_tile == safe_tile)
            ):
                new_tile = trap_tile
            row.append(new_tile)
        room.append(row)
    return room


def main():
    with open("day_18_input.txt") as f:
        puzzle_input = f.read().strip()

    room = populate_room(puzzle_input, 40)
    print(f"Part 1: {sum(row.count('.') for row in room)}")

    room = populate_room(puzzle_input, 400000)
    print(f"Part 2: {sum(row.count('.') for row in room)}")


if __name__ == "__main__":
    main()
