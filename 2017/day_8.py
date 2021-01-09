from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Register:
    value: int = 0


def main():
    registers = defaultdict(Register)
    max_value = 0
    with open("day_8_input.txt") as f:
        for line in f.read().splitlines():
            instruction, condition = line.split(" if ")
            r, op, offset = condition.split()
            if eval(f"{registers[r].value} {op} {offset}"):
                r, op, offset = instruction.split()
                if op == "inc":
                    registers[r].value += int(offset)
                elif op == "dec":
                    registers[r].value -= int(offset)
                else:
                    raise ValueError(f"Unrecognized operation: {op}")
                max_value = max(max_value, registers[r].value)

    print(f"Part 1: {max(register.value for register in registers.values())}")
    print(f"Part 2: {max_value}")


if __name__ == "__main__":
    main()
