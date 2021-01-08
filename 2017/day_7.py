from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List


@dataclass
class Program:
    name: str
    number: int
    supporting: List[Program] = List
    is_supported: bool = False

    @property
    def weight(self) -> int:
        weight = self.number
        for program in self.supporting:
            weight += program.weight
        return weight


def main():
    programs = list()
    with open("day_7_input.txt") as f:
        for line in f.read().splitlines():
            parts = line.split(" -> ")
            name, number = re.search(r"(\w+) \((\d+)\)", parts[0]).groups()
            program = Program(name, int(number))
            supporting = None if len(parts) == 1 else parts[1].split(", ")
            programs.append((program, supporting))

    for program, supporting in programs:
        supporting_programs = list() if supporting is None else [p for p, s in programs if p.name in supporting]
        program.supporting = supporting_programs
        for p in supporting_programs:
            p.is_supported = True

    bottom_programs = [p for p, _ in programs if not p.is_supported]
    assert len(bottom_programs) == 1
    bottom_program = bottom_programs[0]
    print(f"Part 1: {bottom_program.name}")

    current = bottom_program
    weights = [p.weight for p in current.supporting]
    adjustment = None
    while max(weights) != min(weights):
        for i, program in enumerate(current.supporting):
            if (
                current.supporting[i].weight != current.supporting[i - 1].weight
                and current.supporting[i].weight != current.supporting[i - 2].weight
            ):
                adjustment = current.supporting[i - 1].weight - current.supporting[i].weight
                current = current.supporting[i]
                weights = [p.weight for p in current.supporting]
                break

    answer = current.number + adjustment
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    main()
