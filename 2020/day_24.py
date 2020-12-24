from copy import deepcopy
from typing import List, Tuple, Set

Point = Tuple[int, int]


def parse_instruction(line: str) -> List[str]:
    """Get a list with directions for input line"""
    allowed_directions = ["e", "se", "sw", "w", "nw", "ne"]
    directions = list()
    partial_direction = str()
    for char in line:
        if (partial_direction + char) in allowed_directions:
            directions.append(partial_direction + char)
            partial_direction = str()
        elif char in allowed_directions:
            directions.append(char)
        else:
            partial_direction += char
    return directions


def get_adjacent_tiles(tile: Point, black_tiles: Set[Point]) -> Tuple[List[Point], List[Point]]:
    """Get while and black tiles adjacent to a single tile"""
    x, y = tile[0], tile[1]
    adjacent_tiles = [(x + 2, y), (x + 1, y + 1), (x - 1, y + 1), (x - 2, y), (x - 1, y - 1), (x + 1, y - 1)]
    black_adjacent = list()
    white_adjacent = list()
    for adjacent in adjacent_tiles:
        if adjacent in black_tiles:
            black_adjacent.append(adjacent)
        else:
            white_adjacent.append(adjacent)
    return black_adjacent, white_adjacent


def flip_tiles(black_tiles: Set[Point]) -> Set[Point]:
    """Flip black and while tiles according to adjacent tiles"""
    new_tiles = deepcopy(black_tiles)
    for black_tile in black_tiles:
        black_adjacent, white_adjacent = get_adjacent_tiles(black_tile, black_tiles)

        # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
        if len(black_adjacent) == 0 or len(black_adjacent) > 2:
            new_tiles.remove(black_tile)

        # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
        for white_tile in white_adjacent:
            black_adjacent, _ = get_adjacent_tiles(white_tile, black_tiles)
            if len(black_adjacent) == 2:
                new_tiles.add(white_tile)

    return new_tiles


def main():
    with open("day_24_input.txt") as f:
        input_lines = f.read().splitlines()

    black_tiles = set()  # Save only the black tiles locations
    for line in input_lines:
        x, y = 0, 0
        directions = parse_instruction(line)
        for direction in directions:
            if direction == "e":
                x += 2
            elif direction == "w":
                x -= 2
            elif direction == "se":
                y -= 1
                x += 1
            elif direction == "sw":
                y -= 1
                x -= 1
            elif direction == "ne":
                y += 1
                x += 1
            elif direction == "nw":
                y += 1
                x -= 1
        final_tile = (x, y)
        if final_tile not in black_tiles:
            black_tiles.add(final_tile)
        else:
            black_tiles.remove(final_tile)

    print(f"Part 1: {len(black_tiles)}")

    n_flips = 100
    for _ in range(n_flips):
        black_tiles = flip_tiles(black_tiles)
    print(f"Part 2: {len(black_tiles)}")


if __name__ == "__main__":
    main()
