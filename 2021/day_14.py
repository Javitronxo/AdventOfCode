from collections import defaultdict
from copy import deepcopy
from math import ceil
from typing import Dict


def get_score(polymer: Dict[str, int]) -> int:
    counter = defaultdict(int)
    for key, value in polymer.items():
        counter[key[0]] += value
        counter[key[1]] += value
    return ceil(max(counter.values()) / 2) - ceil(min(counter.values()) / 2)


def main():
    polymer, reactions = defaultdict(int), dict()
    with open("day_14_input.txt") as f:
        for i, line in enumerate(f.readlines()):
            if i == 0:
                for j in range(len(line.strip()) - 1):
                    polymer[line[j] + line[j + 1]] += 1
            elif not len(line.strip()):
                continue
            else:
                left, right = line.strip().split(" -> ")
                reactions[left] = right

    num_steps_one, num_steps_two = 10, 40
    for i in range(num_steps_two):
        if i == num_steps_one:
            print(f"Part 1: {get_score(polymer)}")
        new_polymer = defaultdict(int)
        for key, value in polymer.items():
            try:
                new_char = reactions[key]
                new_polymer[key[0] + new_char] += value
                new_polymer[new_char + key[1]] += value
            except KeyError:
                new_polymer[key] += value
        polymer = deepcopy(new_polymer)
    print(f"Part 2: {get_score(polymer)}")


if __name__ == "__main__":
    main()
