from __future__ import annotations

import re
from typing import List

TARGET_BAG = "shiny gold"


class Bag:
    def __init__(self, name: str, contains: List[str]):
        self.name = name
        self.contains = list()
        self._parse_contains(contains)

    def _parse_contains(self, contains_list: List[str]):
        for bag in contains_list:
            self.contains.append(re.findall(r"(\d+) (\w+ \w+)", bag)[0])

    def can_contain(self, target_bag: str, bags_descriptions: List[Bag]) -> bool:
        for number, name in self.contains:
            if name == target_bag:
                return True
            else:
                bag = [bag for bag in bags_descriptions if bag.name == name][0]
                if bag.can_contain(target_bag, bags_descriptions):
                    return True
        return False

    def get_num_required_bags(self, bags_descriptions: List[Bag]) -> int:
        num_bags = 0
        for number, name in self.contains:
            bag = [bag for bag in bags_descriptions if bag.name == name][0]
            num_bags += int(number) + int(number) * bag.get_num_required_bags(bags_descriptions)
        return num_bags


def main():
    bags_descriptions = list()
    with open("day_7_input.txt") as f:
        for line in f.readlines():
            input_bag = re.findall(r"^\w+ \w+", line)[0]
            required_bags = re.findall(r"\d+ \w+ \w+", line)
            bags_descriptions.append(Bag(input_bag, required_bags))

    num_bags = sum(bag.can_contain(TARGET_BAG, bags_descriptions) for bag in bags_descriptions)
    print(f"Part 1: {num_bags} bags can contain my {TARGET_BAG} bag")

    shiny_gold_bag = [bag for bag in bags_descriptions if bag.name == TARGET_BAG][0]
    print(f"Part 2: {shiny_gold_bag.get_num_required_bags(bags_descriptions)} bags are required in my {TARGET_BAG} bag")


if __name__ == "__main__":
    main()
