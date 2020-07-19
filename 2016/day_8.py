import re
from collections import deque
from typing import Sequence


class Screen:
    def __init__(self, width: int = 50, height: int = 6):
        self.grid = list()
        self.width = width
        self.height = height
        self._initialize_grid()

    def _initialize_grid(self):
        for i in range(self.height):
            self.grid.append(deque('.' * self.width))

    def apply_instruction(self, instruction: str):
        rotate_pattern = r'rotate (\w+) \w=(\d+) by (\d+)'
        rect_pattern = r'rect (\d+)x(\d+)'
        if re.search(rotate_pattern, instruction):
            rotate_info = re.search(rotate_pattern, instruction).groups()
            self.rotate(rotate_info)
        elif re.search(rect_pattern, instruction):
            rect_info = re.search(rect_pattern, instruction).groups()
            self.rect(rect_info)
        else:
            raise ValueError(f"Could not parse instruction: {instruction}")

    def rotate(self, rotate_info: Sequence[str]):
        target = int(rotate_info[1])
        value = int(rotate_info[2])
        if rotate_info[0] == 'column':
            new_column = deque([x[target] for x in self.grid])
            new_column.rotate(value)
            for i in range(self.height):
                self.grid[i][target] = new_column[i]
        elif rotate_info[0] == 'row':
            self.grid[target].rotate(value)
        else:
            raise ValueError(f"Unknown rotation value: {rotate_info[0]}")

    def rect(self, rect_info: Sequence[str]):
        a = int(rect_info[0])
        b = int(rect_info[1])
        for i in range(b):
            for j in range(a):
                self.grid[i][j] = '#'

    def get_number_pixels_on(self) -> int:
        pixels_on = 0
        for row in self.grid:
            pixels_on += row.count('#')
        return pixels_on

    def print(self):
        for row in self.grid:
            print(" ".join(row))


def main():
    screen = Screen()

    with open('day_8_input.txt') as f_in:
        for instruction in f_in.readlines():
            screen.apply_instruction(instruction)
    print(f"Part 1: We will have {screen.get_number_pixels_on()} pixels on")

    screen.print()
    # Part 2: Read output code


if __name__ == '__main__':
    main()
