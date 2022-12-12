from dataclasses import dataclass, field
from typing import List


@dataclass
class Register:
    value: int = 1


@dataclass
class Sprite:
    values: List[int] = field(default_factory=list)

    def __post_init__(self):
        self.values = [0, 1, 2]

    def move(self, value: int) -> None:
        for i in range(len(self.values)):
            self.values[i] += value


def main():
    with open("day10_input.txt") as f:
        instructions = f.readlines()

    register = Register()
    sprite = Sprite()
    op_cycles = {"noop": 1, "addx": 2}
    cycle = 1
    part_one_values = list()
    screen = [["." for _ in range(40)] for _ in range(6)]

    while len(instructions):
        instruction = instructions.pop(0)
        parts = instruction.split()
        for i in range(op_cycles[parts[0]]):
            # Print the pixel
            row, col = divmod(cycle - 1, 40)
            if col in sprite.values:
                screen[row][col] = "#"
            cycle += 1
            if i == 1:  # Only addx operation takes 2 cycles
                register.value += int(parts[1])
                sprite.move(int(parts[1]))
            if (cycle - 20) % 40 == 0:
                part_one_values.append(register.value * cycle)

    print(f"Part 1: {sum(part_one_values)}")
    print(f"Part 2:")
    for line in screen:
        print("".join(line))


if __name__ == "__main__":
    main()
