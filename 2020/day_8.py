from copy import deepcopy
from typing import List, Tuple


class Register:
    def __init__(self):
        self.accumulator = 0

    @staticmethod
    def parse_instruction(instruction: str) -> Tuple[str, int]:
        operation, offset_str = instruction.split()
        return operation, int(offset_str)

    def execute(self, instruction: str) -> int:
        operation, offset = self.parse_instruction(instruction)
        if operation == "acc":
            self.accumulator += int(offset)
            return 1
        elif operation == "jmp":
            return int(offset)
        elif operation == "nop":
            return 1
        else:
            raise ValueError(f"Unsupported operation: {operation}")


def run_all(instructions: List[str]) -> Tuple[int, int]:
    register = Register()
    i = 0
    visited_instructions = list()
    while i < len(instructions):
        visited_instructions.append(i)
        i += register.execute(instructions[i])
        if i in visited_instructions:
            return register.accumulator, 1  # Good result for part 1
    return register.accumulator, 2  # Good result for part 2


def main():
    with open("day_8_input.txt") as f:
        instructions = f.read().splitlines()

    print(f"Part 1: The value is in the accumulator is {run_all(instructions)[0]}")

    # Brute force, feeling lazy...
    for i, instruction in enumerate(instructions):
        operation, _ = Register.parse_instruction(instruction)
        if operation in ["nop", "jmp"]:
            new_instructions = deepcopy(instructions)
            new_instructions[i] = (
                instructions[i].replace("nop", "jpm") if operation == "nop" else instructions[i].replace("jmp", "nop")
            )
            result = run_all(new_instructions)
            if result[1] == 2:
                print(f"Part 2: The value is in the accumulator is {result[0]}")
                break


if __name__ == "__main__":
    main()
