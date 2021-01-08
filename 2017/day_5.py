from typing import List


def apply_instructions(instructions: List[int], part_two: bool = False) -> int:
    steps = 0
    pointer = 0
    while pointer < len(instructions):
        offset = instructions[pointer]
        adjust = -1 if part_two and offset > 2 else 1
        instructions[pointer] += adjust
        pointer += offset
        steps += 1
    return steps


def main():
    with open("day_5_input.txt") as f:
        instructions = [int(line) for line in f.read().splitlines()]

    print(f"Part 1: {apply_instructions(instructions[:])}")
    print(f"Part 2: {apply_instructions(instructions, part_two=True)}")


if __name__ == "__main__":
    main()
