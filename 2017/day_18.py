from dataclasses import dataclass
from queue import LifoQueue
from typing import Union


@dataclass
class Register:
    value: int = 0


def execute(instruction: str, registers, queue_one, queue_two=None):
    def get(value: Union[int, str]) -> int:
        try:
            res = int(value)
        except ValueError:
            res = registers[value].value
        return res

    fields = instruction.split()
    op = fields[0]
    offset = 1
    freq = None
    if op == "snd":
        queue_one.put(get(fields[1]))
    elif op == "set":
        registers[fields[1]].value = get(fields[2])
    elif op == "add":
        registers[fields[1]].value += get(fields[2])
    elif op == "mul":
        registers[fields[1]].value *= get(fields[2])
    elif op == "mod":
        registers[fields[1]].value = registers[fields[1]].value % get(fields[2])
    elif op == "rcv":
        if get(fields[1]):
            freq = queue_one.get()
    elif op == "jgz":
        if get(fields[1]):
            offset = get(fields[2])
    else:
        raise ValueError(f"Unrecognized operation: {op}")
    return offset, freq


def main():
    with open("day_18_input.txt") as f:
        instructions = f.read().splitlines()

    # Initialize registers and make copies for part two
    registers = dict()
    for instruction in instructions:
        register = instruction.split()[1]
        if not isinstance(register, int) and register not in registers:
            registers[register] = Register()

    i = 0
    queue = LifoQueue()
    freq = None
    while i < len(instructions):
        offset, freq = execute(instructions[i], registers, queue, queue)
        if freq:
            break
        i += offset
    print(f"Part 1: {freq}")


if __name__ == "__main__":
    main()
