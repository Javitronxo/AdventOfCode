from math import trunc
from typing import List


class BoardingPass:
    def __init__(self, boarding_pass_raw: str):
        self.row = None
        self.column = None
        self.seat_id = None
        self._decode_raw_pass(boarding_pass_raw)

    @staticmethod
    def get_set_id(row: int, column: int) -> int:
        return row * 8 + column

    def _decode_raw_pass(self, boarding_pass_raw: str):
        max_row = Plane.NUM_ROWS - 1
        max_col = Plane.NUM_COLUMNS - 1
        min_row = 0
        min_col = 0
        for i, char in enumerate(boarding_pass_raw):
            if i < 7:
                if char == "F":
                    max_row -= trunc((max_row - min_row + 1) / 2)
                elif char == "B":
                    min_row += round((max_row - min_row + 1) / 2)
            else:
                if char == "L":
                    max_col -= trunc((max_col - min_col + 1) / 2)
                elif char == "R":
                    min_col += round((max_col - min_col + 1) / 2)

        assert max_row == min_row
        assert max_col == min_col
        self.row = max_row
        self.column = max_col
        self.seat_id = self.get_set_id(self.row, self.column)


class Plane:
    NUM_ROWS = 128
    NUM_COLUMNS = 8

    def __init__(self, boarding_passes: List[BoardingPass]):
        self.plane_map = [["Free" for _ in range(self.NUM_COLUMNS)] for _ in range(self.NUM_ROWS)]
        self.plane_ids = set()
        self._populate_plane(boarding_passes)

    def _populate_plane(self, boarding_passes: List[BoardingPass]):
        for boarding_pass in boarding_passes:
            self.plane_map[boarding_pass.row][boarding_pass.column] = "Taken"
            self.plane_ids.add(boarding_pass.seat_id)

    def get_valid_free_seat(self) -> int:
        for row in range(self.NUM_ROWS):
            for column in range(self.NUM_COLUMNS):
                seat_id = BoardingPass.get_set_id(row, column)
                if self.plane_map[row][column] == "Free" and {seat_id + 1, seat_id - 1}.issubset(self.plane_ids):
                    return seat_id


def main():
    boarding_passes = list()
    with open("day_5_input.txt") as f:
        for line in f.readlines():
            boarding_passes.append(BoardingPass(line.strip()))

    print(f"Part 1: The highest seat ID is {max(boarding_pass.seat_id for boarding_pass in boarding_passes)}")

    plane = Plane(boarding_passes)
    print(f"Part 2: My seat must be {plane.get_valid_free_seat()}")


if __name__ == "__main__":
    main()
