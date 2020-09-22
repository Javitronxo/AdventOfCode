
class Register:
    def __init__(self, value: int=0):
        self.value = value


class Computer:
    def __init__(self, offset_a: int=0, offset_b: int=0, offset_c: int=0, offset_d: int=0):
        self.registers = {
            'a': Register(offset_a),
            'b': Register(offset_b),
            'c': Register(offset_c),
            'd': Register(offset_d),
        }

    def execute(self, instruction: str) -> int:
        """
        Execute the instruction and return the offset for the next one
        """
        parts = instruction.strip().split()
        if parts[0] == 'cpy':
            try:
                self.registers[parts[2]].value = self.registers[parts[1]].value
            except KeyError:
                self.registers[parts[2]].value = int(parts[1])
        elif parts[0] == 'inc':
            self.registers[parts[1]].value += 1
        elif parts[0] == 'dec':
            self.registers[parts[1]].value -= 1
        elif parts[0] == 'jnz':
            try:
                x = self.registers[parts[1]].value
            except KeyError:
                x = int(parts[1])
            if x != 0:
                return int(parts[2])
        return 1


def main():
    with open('day_12_input.txt') as f_in:
        instructions = f_in.readlines()

    computer = Computer()
    i = 0
    while i < len(instructions):
        i += computer.execute(instructions[i])
    print(f"Part 1: Value in register A is: {computer.registers['a'].value}")

    computer = Computer(offset_c=1)
    i = 0
    while i < len(instructions):
        i += computer.execute(instructions[i])
    print(f"Part 2: Value in register A is: {computer.registers['a'].value}")


if __name__ == '__main__':
    main()
