import math
import re
from copy import deepcopy
from dataclasses import dataclass, field
from typing import List


@dataclass
class Monkey:
    number: int
    items: List[int] = field(default_factory=list)
    items_inspected: int = 0
    operation: str = ""
    divisible_by: int = -1
    if_true: int = -1
    if_false: int = -1

    def apply_operation(self, item: int) -> int:
        try:
            factor = int(re.findall("\d+", self.operation)[0])
        except IndexError:
            factor = item
        if re.search("\+", self.operation):
            return factor + item
        elif re.search("\*", self.operation):
            return factor * item
        else:
            raise ArithmeticError(f"Could not recognize operation in: {self.operation}")


def get_monkey_business(monkeys: List[Monkey], rounds: int, super_worried: bool) -> int:
    mod_factor = math.prod([monkey.divisible_by for monkey in monkeys])
    for _ in range(rounds):
        for turn in range(len(monkeys)):
            monkey = monkeys[turn]
            while len(monkey.items):
                item = monkey.items.pop(0)
                new_value = monkey.apply_operation(item)
                if not super_worried:
                    new_value = new_value // 3
                new_value %= mod_factor
                if new_value % monkey.divisible_by == 0:
                    monkeys[monkey.if_true].items.append(new_value)
                else:
                    monkeys[monkey.if_false].items.append(new_value)
                monkey.items_inspected += 1
    sorted_items = sorted([monkey.items_inspected for monkey in monkeys], reverse=True)
    return sorted_items[0] * sorted_items[1]


def main():
    monkeys_part_one = list()
    with open("day11_input.txt") as f:
        for line in f.readlines():
            if re.search("^Monkey \d+:", line):
                monkey = Monkey(int(re.search("^Monkey (\d+):", line).groups(1)[0]))
            elif re.search("Starting items:", line):
                monkey.items = [int(x) for x in re.findall("\d+", line)]
            elif re.search("Operation:", line):
                monkey.operation = re.sub("Operation: ", "", line.strip())
            elif re.search("Test:", line):
                monkey.divisible_by = int(re.findall("\d+", line)[0])
            elif re.search("If true:", line):
                monkey.if_true = int(re.findall("\d+", line)[0])
            elif re.search("If false:", line):
                monkey.if_false = int(re.findall("\d+", line)[0])
                monkeys_part_one.append(monkey)
    monkeys_part_two = deepcopy(monkeys_part_one)

    print(f"Part 1: {get_monkey_business(monkeys_part_one, rounds=20, super_worried=False)}")
    print(f"Part 2: {get_monkey_business(monkeys_part_two, rounds=10000, super_worried=True)}")


if __name__ == "__main__":
    main()
