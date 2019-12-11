# https://adventofcode.com/2019/day/11
from collections import defaultdict
import math

import lib.utils as utils
from lib.intcode_processor_2019 import IntCodeProcessor


class PaintingRobot:
    def __init__(self, instructions):
        self.program = IntCodeProcessor(instructions)
        self.panel = defaultdict(str)

    def run(self, input_code):
        point = (0, 0)
        direction = 0

        self.program.add_input(input_code)
        while self.program.status != "COMPLETED":
            color, turn = self.program.outputs[-2:]
            self.panel[point] = '#' if color else '.'

            direction = direction + (math.pi / 2) if turn else direction + (3 * math.pi / 2)
            step = (round(math.sin(direction), 6), round(math.cos(direction), 6))
            point = (point[0] + step[0], point[1] + step[1])

            input_point = 0 if self.panel[point] in ['', '.'] else 1
            self.program.add_input(input_point)

    def render_panel(self):
        max_x = max(x for x, y in list(self.panel.keys()))
        min_x = min(x for x, y in list(self.panel.keys()))
        max_y = max(y for x, y in list(self.panel.keys()))
        min_y = min(y for x, y in list(self.panel.keys()))
        grid = list()
        for x in range(int(abs(min_x) + max_x) + 1):
            grid.append('')
            for y in range(int(abs(min_y) + max_y) + 1):
                grid[x] += self.panel[(x + min_x, y + min_y)]
        return grid


def main():
    input_program = utils.read_file_to_int_dict('day_11_input.txt')

    painting_robot = PaintingRobot(input_program)
    painting_robot.run(0)
    result_first_part = len(painting_robot.panel)
    print("First part result: {}".format(result_first_part))

    painting_robot = PaintingRobot(input_program)
    painting_robot.run(1)
    result_second_part = painting_robot.render_panel()
    print("Second part result:\n{}".format('\n'.join(result_second_part)))


if __name__ == '__main__':
    main()
