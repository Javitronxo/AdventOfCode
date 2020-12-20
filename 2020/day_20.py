import re
from typing import List


class Tile:
    def __init__(self, number: str):
        self.number = number
        self.grid = list()
        self.adjacent = set()

    @property
    def borders(self) -> List[List[str]]:
        return [
            self.grid[0],  # 0: Up
            self.grid[-1],  # 1: Down
            [line[0] for line in self.grid],  # 2: Left
            [line[-1] for line in self.grid],  # 3: Right
        ]


def main():
    with open("day_20_input.txt") as f:
        input_lines = f.read().splitlines()

    tiles = list()
    for line in input_lines:
        if "Tile" in line:
            target_number = re.search(r"Tile (\d+):", line).group(1)
            tile = Tile(target_number)
        elif not line:
            tiles.append(tile)
        else:
            tile.grid.append(list(line))
    tiles.append(tile)

    for tile in tiles:
        for candidate in tiles:
            if candidate.number == tile.number:
                continue
            if any(
                border for border in tile.borders if border in candidate.borders or border[::-1] in candidate.borders
            ):
                tile.adjacent.add(candidate)

    answer = 1
    for tile in tiles:
        if len(tile.adjacent) == 2:
            answer *= int(tile.number)
            continue

    print(f"Part 1: {answer}")


if __name__ == "__main__":
    main()
