# https://adventofcode.com/2019/day/12
from collections import defaultdict

import lib.utils as utils
from lib.intcode_processor_2019 import IntCodeProcessor


class ArcadeMachine:
    def __init__(self, memory):
        self.program = IntCodeProcessor(memory)
        self.panel = defaultdict(int)
        self.score = 0
        self.paddle_x = 0
        self.ball_x = 0

    def run(self):
        self.program.run()

        while self.program.status != "COMPLETED" or len(self.program.outputs):
            try:
                x = self.program.outputs.pop(0)
                y = self.program.outputs.pop(0)
            except IndexError:
                x, y = None, None

            if x == -1 and y == 0:
                self.score = self.program.outputs.pop(0)

            elif x is not None and y is not None:
                tile_id = self.program.outputs.pop(0)
                self.panel[(x, y)] = tile_id
                if tile_id == 3:
                    self.paddle_x = x
                elif tile_id == 4:
                    self.ball_x = x

            elif self.program.status == "WAITING":
                if self.ball_x > self.paddle_x:
                    self.program.add_input(1)
                elif self.ball_x < self.paddle_x:
                    self.program.add_input(-1)
                else:
                    self.program.add_input(0)


def main():
    program = utils.read_file_to_int_dict('day_13_input.txt')

    arcade_machine = ArcadeMachine(program)
    arcade_machine.run()
    result_first_part = len([tile_id for tile_id in arcade_machine.panel.values() if tile_id == 2])
    print("First part result: {}".format(result_first_part))

    arcade_machine = ArcadeMachine(program)
    arcade_machine.program.memory[0] = 2
    arcade_machine.run()
    result_second_part = arcade_machine.score
    print("Second part result: {}".format(result_second_part))


if __name__ == '__main__':
    main()
