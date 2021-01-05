from dataclasses import dataclass
from typing import List, Tuple, Union


@dataclass
class Register:
    value: int = 0


class Computer:
    def __init__(self, offset_a: int = 0, offset_b: int = 0, offset_c: int = 0, offset_d: int = 0):
        self.registers = {
            "a": Register(offset_a),
            "b": Register(offset_b),
            "c": Register(offset_c),
            "d": Register(offset_d),
        }

    def execute(self, instruction: str) -> Tuple[int, Union[int, None]]:
        """Execute the instruction and return the offset for the next one."""
        parts = instruction.strip().split()
        if parts[0] == "cpy":
            try:
                try:
                    self.registers[parts[2]].value = self.registers[parts[1]].value
                except KeyError:
                    self.registers[parts[2]].value = int(parts[1])
            except KeyError:
                pass
        elif parts[0] == "inc":
            self.registers[parts[1]].value += 1
        elif parts[0] == "dec":
            self.registers[parts[1]].value -= 1
        elif parts[0] == "jnz":
            try:
                x = self.registers[parts[1]].value
            except KeyError:
                x = int(parts[1])
            if x != 0:
                try:
                    x = self.registers[parts[2]].value
                except KeyError:
                    x = int(parts[2])
                return x, None
        elif parts[0] == "tgl":
            offset = self.registers[parts[1]].value
            return 1, offset
        elif parts[0] == "mul":
            self.registers[parts[1]].value = self.registers[parts[2]].value * self.registers[parts[3]].value
        elif parts[0] == "nop":
            pass
        return 1, None

    @staticmethod
    def toggle_instruction(instruction: str) -> str:
        parts = instruction.strip().split()
        if len(parts) == 2:
            if parts[0] == "inc":
                return instruction.replace("inc", "dec")
            else:
                return instruction.replace(parts[0], "inc")
        elif len(parts) == 3:
            if parts[0] == "jnz":
                return instruction.replace("jnz", "cpy")
            else:
                return instruction.replace(parts[0], "jnz")


def run_program(instructions: List[str], offset_a: int = 0, offset_b: int = 0, offset_c: int = 0, offset_d: int = 0) -> int:
    computer = Computer(offset_a=offset_a, offset_b=offset_b, offset_c=offset_c, offset_d=offset_d)
    i = 0
    while i < len(instructions):
        i_offset, toggle_offset = computer.execute(instructions[i])
        if toggle_offset is not None:
            try:
                instructions[i + toggle_offset] = Computer.toggle_instruction(instructions[i + toggle_offset])
            except IndexError:
                pass
        i += i_offset
    return computer.registers["a"].value
