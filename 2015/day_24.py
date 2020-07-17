import itertools
from functools import reduce
from sys import maxsize
from typing import List, Tuple


def get_quantum_entanglement(packages: Tuple[int]) -> int:
    return reduce((lambda x, y: x * y), packages)


def get_groups(all_packages: List[int], target_weight: int) -> List[Tuple[int]]:
    group_candidates = list()
    for r in range(1, len(all_packages) - 1):
        for combination in itertools.combinations(all_packages, r):
            if sum(combination) == target_weight:
                group_candidates.append(combination)
        if len(group_candidates):
            break
    return group_candidates


def main():
    with open('day_24_input.txt') as f_in:
        all_packages = [int(x) for x in f_in.read().split('\n')]

    compartments = [3, 4]
    for i, n_compartments in enumerate(compartments):
        # The packages need to be split into three groups of exactly the same weight
        total_weight = sum(all_packages)
        group_weight = total_weight // n_compartments

        # The first group needs as few packages as possible
        group_1_candidates = get_groups(all_packages, group_weight)

        # The first group has the smallest quantum entanglement
        min_quantum_entanglement = maxsize
        for group in group_1_candidates:
            min_quantum_entanglement = min(min_quantum_entanglement, get_quantum_entanglement(group))

        print(f"Part {i}: The quantum entanglement of the first group of packages is {min_quantum_entanglement}")


if __name__ == '__main__':
    main()
