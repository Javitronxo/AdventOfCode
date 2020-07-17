from typing import List, Tuple


class Instruction:
    def __init__(self, input_str: str):
        self.name = None
        self.register = None
        self.offset = None
        self._parse_instruction(input_str)

    def _parse_instruction(self, input_str: str):
        parts = input_str.strip().split()
        for i in range(len(parts)):
            if i == 0:
                self.name = parts[i]
                continue
            try:
                self.offset = int(parts[i])
            except ValueError:
                self.register = parts[i].split(',')[0]


class Register:
    def __init__(self, name: str, value: int = 0):
        self.name = name
        self.current_value = value

    def apply_instruction(self, instruction: Instruction) -> int:
        if instruction.name == 'hlf':
            self.current_value //= 2
            return 1
        elif instruction.name == 'tpl':
            self.current_value *= 3
            return 1
        elif instruction.name == 'inc':
            self.current_value += 1
            return 1
        elif instruction.name == 'jmp':
            return instruction.offset
        elif instruction.name == 'jie' and self.current_value % 2 == 0:
            return instruction.offset
        elif instruction.name == 'jio' and self.current_value == 1:
            return instruction.offset
        return 1


def run_program(instructions: List[Instruction], initial_offset: int = 0) -> Tuple[Register, Register]:
    register_a = Register(name='a', value=initial_offset)
    register_b = Register(name='b')

    i = 0
    while i < len(instructions):
        instruction = instructions[i]
        target_register = register_a if instruction.register == 'a' else register_b
        offset = target_register.apply_instruction(instruction)
        i += offset

    return register_a, register_b


def main():
    instructions = list()
    with open('day_23_input.txt') as f_in:
        for line in f_in.readlines():
            instruction = Instruction(line)
            instructions.append(instruction)

    register_a, register_b = run_program(instructions)
    print(f"Part 1: At the end of the execution we have a value of {register_b.current_value} in register B")

    register_a, register_b = run_program(instructions, initial_offset=1)
    print(f"Part 2: At the end of the execution we have a value of {register_b.current_value} in register B")


if __name__ == '__main__':
    main()
