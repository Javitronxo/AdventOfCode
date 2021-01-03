import re
from collections import deque


class Instruction:
    PATTERNS = [
        r"swap letter (\w) with letter (\w)",
        r"swap position (\d+) with position (\d+)",
        r"move position (\d+) to position (\d+)",
        r"rotate based on position of letter (\w)",
        r"rotate (\w+) (\d+) steps?",
        r"reverse positions (\d+) through (\d+)",
    ]

    def __init__(self, instruction_str: str):
        self.instruction_str = instruction_str
        self.operation = self.get_operation()
        self.pattern = self.PATTERNS[self.operation]

    def get_operation(self) -> int:
        for i, pattern in enumerate(self.PATTERNS):
            if re.match(pattern, self.instruction_str):
                return i

    def swap(self, input_str: str, by_position: bool = False) -> str:
        new_str = str()
        first, second = re.search(self.pattern, self.instruction_str).groups()
        if by_position:
            first = input_str[int(first)]
            second = input_str[int(second)]
        for char in input_str:
            if char == first:
                new_str += second
            elif char == second:
                new_str += first
            else:
                new_str += char
        return new_str

    def reverse(self, input_str: str) -> str:
        first, second = re.search(self.pattern, self.instruction_str).groups()
        return input_str[: int(first)] + input_str[int(first) : int(second) + 1][::-1] + input_str[int(second) + 1 :]

    def rotate(self, input_str: str, reverse: bool = False) -> str:
        input_list = deque(list(input_str))
        first, second = re.search(self.pattern, self.instruction_str).groups()
        if first == "right":
            rotation = int(second) if not reverse else -1 * int(second)
        else:
            rotation = -1 * int(second) if not reverse else int(second)
        input_list.rotate(rotation)
        return "".join(input_list)

    def rotate_by_position(self, input_str: str, reverse: bool = False) -> str:
        input_list = deque(list(input_str))
        first = re.search(self.pattern, self.instruction_str).groups()[0]
        index = input_str.index(first)
        if reverse:
            rotations = {0: 7, 1: -1, 2: 2, 3: -2, 4: 1, 5: -3, 6: 0, 7: 4}  # Reversed engineered rotations
            input_list.rotate(rotations[index])
        else:
            rotations = index + 1
            if index >= 4:
                rotations += 1
            input_list.rotate(rotations)
        return "".join(input_list)

    def move(self, input_str: str, reverse: bool = False):
        input_list = list(input_str)
        first, second = re.search(self.pattern, self.instruction_str).groups()
        if reverse:
            char = input_list.pop(int(second))
            input_list.insert(int(first), char)
        else:
            char = input_list.pop(int(first))
            input_list.insert(int(second), char)
        return "".join(input_list)

    def apply(self, input_str: str, reverse: bool = False) -> str:
        if self.operation == 0:  # "swap letter (\w) with letter (\w)"
            new_str = self.swap(input_str)
        elif self.operation == 1:  # "swap position (\d+) with position (\d+)"
            new_str = self.swap(input_str, by_position=True)
        elif self.operation == 2:  # "move position (\d+) to position (\d+)"
            new_str = self.move(input_str, reverse=reverse)
        elif self.operation == 3:  # "rotate based on position of letter (\w)"
            new_str = self.rotate_by_position(input_str, reverse=reverse)
        elif self.operation == 4:  # "rotate (\w+) (\d+) steps"
            new_str = self.rotate(input_str, reverse=reverse)
        elif self.operation == 5:  # "reverse positions (\d+) through (\d+)"
            new_str = self.reverse(input_str)
        else:
            raise ValueError("Unrecognized operation")
        return new_str


def main():
    with open("day_21_input.txt") as f:
        puzzle_input = f.read().splitlines()

    password = "abcdefgh"
    for line in puzzle_input:
        instruction = Instruction(line)
        password = instruction.apply(password)
    print(f"Part 1: {password}")

    password = "fbgdceah"
    for line in reversed(puzzle_input):
        instruction = Instruction(line)
        password = instruction.apply(password, reverse=True)
    print(f"Part 2: {password}")


if __name__ == "__main__":
    main()
