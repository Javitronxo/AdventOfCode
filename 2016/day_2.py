from typing import List

CODE_PAD_1 = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
]

CODE_PAD_2 = [
    [None, None, '1', None, None],
    [None, '2', '3', '4', None],
    ['5', '6', '7', '8', '9'],
    [None, 'A', 'B', 'C', None],
    [None, None, 'D', None, None],
]


def get_code(current_position: List[int], code_pad: List[List[str]], instructions: List[str]) -> str:
    code = str()
    for instruction in instructions:
        for step in instruction:
            if step == 'L':
                move = [0, -1]
            elif step == 'R':
                move = [0, 1]
            elif step == 'U':
                move = [-1, 0]
            elif step == 'D':
                move = [1, 0]
            else:
                raise ValueError(f"Unrecognized step: {step}")

            next_position = [max(current_position[0] + move[0], 0), max(current_position[1] + move[1], 0)]
            next_position = [min(next_position[0], len(code_pad) - 1), min(next_position[1], len(code_pad) - 1)]
            if code_pad[next_position[0]][next_position[1]] is not None:
                current_position = next_position

        code += code_pad[current_position[0]][current_position[1]]

    return code


def main():
    instructions = list()
    with open('day_2_input.txt') as f_in:
        for line in f_in.readlines():
            instruction = line.strip()
            instructions.append(instruction)

    initial_position = [1, 1]  # Number '5' in code pad
    print(f"Part 1: The code for the bathroom is: {get_code(initial_position, CODE_PAD_1, instructions)}")
    initial_position = [2, 0]  # Number '5' in code pad
    print(f"Part 2: The code for the bathroom is: {get_code(initial_position, CODE_PAD_2, instructions)}")


if __name__ == '__main__':
    main()
