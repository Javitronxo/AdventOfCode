import re


class Grid:
    def __init__(self, grid_length: int):
        self.grid = None
        self.grid_length = grid_length
        self.initialize_grid(grid_length)

    def initialize_grid(self, grid_length: int):
        self.grid = list()
        for _ in range(grid_length):
            self.grid.append([0] * grid_length)

    def apply_instruction(self, instruction: str):
        """Used for part 1"""
        instruction_pattern = r'(turn |toggle)(\w+)? (\d+),(\d+) through (\d+),(\d+)'
        order, state, x0, y0, x1, y1 = re.findall(instruction_pattern, instruction)[0]
        for x in range(int(x0), int(x1) + 1):
            for y in range(int(y0), int(y1) + 1):
                if order == 'toggle':
                    self.grid[x][y] = (self.grid[x][y] + 1) % 2
                elif state == 'on':
                    self.grid[x][y] = 1
                elif state == 'off':
                    self.grid[x][y] = 0

    def apply_right_instruction(self, instruction: str):
        """Used for part 2"""
        instruction_pattern = r'(turn |toggle)(\w+)? (\d+),(\d+) through (\d+),(\d+)'
        order, state, x0, y0, x1, y1 = re.findall(instruction_pattern, instruction)[0]
        for x in range(int(x0), int(x1) + 1):
            for y in range(int(y0), int(y1) + 1):
                if order == 'toggle':
                    self.grid[x][y] += 2
                elif state == 'on':
                    self.grid[x][y] += 1
                elif state == 'off':
                    self.grid[x][y] -= 1 if self.grid[x][y] != 0 else 0

    def get_lights_on(self) -> int:
        lights_on = 0
        for i in range(self.grid_length):
            lights_on += self.grid[i].count(1)
        return lights_on

    def get_total_brightness(self) -> int:
        total_brightness = 0
        for i in range(self.grid_length):
            total_brightness += sum(self.grid[i])
        return total_brightness


def main():
    wrong_grid = Grid(1000)
    right_grid = Grid(1000)
    with open('day_6_input.txt') as f_in:
        for instruction in f_in.readlines():
            wrong_grid.apply_instruction(instruction)
            right_grid.apply_right_instruction(instruction)
    print('We got %d lights on first grid' % wrong_grid.get_lights_on())
    print('We got %d brightness on second grid' % right_grid.get_total_brightness())


if __name__ == '__main__':
    main()
