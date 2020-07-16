import re
from collections import defaultdict


def main():
    line_pattern = r'(\w+) => (\w+)'
    replacements = defaultdict(list)
    molecule = None
    with open('day_19_input.txt') as f_in:
        for line in f_in.readlines():
            r = re.findall(line_pattern, line)
            if r:
                replacements[r[0][0]].append(r[0][1])
            else:
                molecule = line.strip()

    combinations = set()
    for original, replacements in replacements.items():
        occurrences = molecule.count(original)
        for replacement in replacements:
            prev_index = 0
            for _ in range(occurrences):
                index = molecule.index(original, prev_index)
                new_molecule = molecule[:index] + replacement + molecule[index + len(original):]
                combinations.add(new_molecule)
                prev_index = index + 1
    print(f"We got {len(combinations)} different combinations")

    # Reasoning: https://www.reddit.com/r/adventofcode/comments/3xflz8/day_19_solutions/cy4etju
    parenthesis = ['Rn', 'Ar']
    comma = 'Y'
    num_non_terminals = len([char for char in molecule if char.isupper()])
    steps = num_non_terminals - 2 * molecule.count(parenthesis[0]) - 2 * molecule.count(comma) - 1
    print(f"We get the molecule after {steps} steps")


if __name__ == '__main__':
    main()
