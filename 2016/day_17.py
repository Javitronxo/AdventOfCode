from queue import Queue
from typing import Dict, Tuple

from lib.utils import get_md5_hash

Room = Tuple[int, int]


def get_neighbours(room: Room, input_str: str) -> Dict[str, Room]:
    possibilities = dict()
    steps = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    directions = {0: "U", 1: "D", 2: "L", 3: "R"}
    shorted_hash = get_md5_hash(input_str)[:4]
    for i, char in enumerate(shorted_hash):
        if char in ["b", "c", "d", "e", "f"]:
            new_room = (room[0] + steps[i][0], room[1] + steps[i][1])
            if all(0 <= coord <= 3 for coord in new_room):
                direction = directions[i]
                possibilities[direction] = new_room
    return possibilities


def main():
    with open("day_17_input.txt") as f:
        input_puzzle = f.read().strip()

    origin = (0, 3)
    destination = (3, 0)

    rooms = Queue()
    rooms.put((origin, input_puzzle))
    paths = list()

    while not rooms.empty():
        current_room, input_str = rooms.get()
        neighbours = get_neighbours(current_room, input_str)
        for direction, new_room in neighbours.items():
            new_str = input_str + direction
            if new_room == destination:
                paths.append(new_str)
            else:
                rooms.put((new_room, new_str))

    shortest_path = min(paths, key=len).replace(input_puzzle, "")
    print(f"Part 1: {shortest_path}")

    longest_path = max(paths, key=len).replace(input_puzzle, "")
    print(f"Part 2: {len(longest_path)}")


if __name__ == "__main__":
    main()
