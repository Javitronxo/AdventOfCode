import re
from typing import List


class Building:
    def __init__(self):
        self.floors = list()
        self.current_floor = 0

    def check_elements_floor(self, elements):
        elements_floor = self.floors[self.current_floor].elements
        if not len(elements) or len(elements) > 2:
            print("The elevator needs one or two elements to work.")
            return False
        if set(elements).intersection(elements_floor) == set(elements):
            return True
        else:
            print("One or more of the elements were not found in this floor.")
            return False

    def add_floor(self, floor):
        self.floors.append(floor)

    def is_completed(self) -> bool:
        return len(self.floors[-1]) and not any(self.floors[:-1])

    def print_layout(self):
        layout = "\n"
        for i in reversed(range(len(self.floors))):
            layout += f"F{i + 1}\t{'E' if self.current_floor == i else '.'}\t{str(self.floors[i])}\n"
        print(layout)


class Floor:
    def __init__(self, chips: List[str], generators: List[str]):
        self.chips = chips
        self.generators = generators

    @property
    def elements(self):
        return self.chips + self.generators

    def __str__(self):
        return '\t'.join(self.elements)

    def __len__(self):
        return len(self.elements)

    def remove(self, elements):
        for element in elements:
            if element.endswith('M'):
                self.chips.remove(element)
            elif element.endswith('G'):
                self.generators.remove(element)

    def add(self, elements):
        for element in elements:
            if element.endswith('M'):
                self.chips.append(element)
            elif element.endswith('G'):
                self.generators.append(element)

    def is_safe(self, elements) -> bool:
        generators = [generator[:-1] for generator in self.generators]
        chips = [chip[:-1] for chip in self.chips]
        for element in elements:
            if element.endswith('M'):
                chips.append(element[:-1])
            elif element.endswith('G'):
                generators.append(element[:-1])
        if not len(generators):
            return True

        chips_without_generator = set(chips).difference(generators)
        generators_without_chip = set(generators).difference(chips)
        if len(generators_without_chip) and len(chips_without_generator):
            return False
        else:
            return True


def main():
    building = Building()
    with open('day_11_input.txt') as f_in:
        for i, line in enumerate(f_in.readlines()):
            chips = [chip + 'M' for chip in re.findall(r'(\w+)-compatible microchip', line)]
            generators = [generator + 'G' for generator in re.findall(r'(\w+) generator', line)]
            floor = Floor(chips, generators)
            building.add_floor(floor)

    num_steps = 0

    # Solve the puzzle interactively
    while not building.is_completed():
        building.print_layout()

        # Load elevator
        while True:
            elements = input('What elements do you want to add in the elevator? ').split()
            if building.check_elements_floor(elements):
                break

        while True:
            direction = int(input('Do you want to move up (1)? Or down(2)? '))
            if direction == 1:
                if building.current_floor == len(building.floors):
                    print('We are already in the top floor')
                    continue
                next_floor = building.floors[building.current_floor + 1]
                is_safe = next_floor.is_safe(elements)
                break
            elif direction == 2:
                if building.current_floor == 0:
                    print('We are already in the ground floor')
                    continue
                next_floor = building.floors[building.current_floor - 1]
                is_safe = next_floor.is_safe(elements)
                break
            else:
                print('Could not recognize the instruction.')

        if not is_safe:
            print('That is not a safe move, please try again.')
            continue

        # Update the building status
        building.floors[building.current_floor].remove(elements)
        if direction == 1:
            building.current_floor += 1
        else:
            building.current_floor -= 1
        building.floors[building.current_floor].add(elements)

        num_steps += 1

    print(f"Part 1: Minimum number of steps required is {num_steps}")  # 47
    # Part 2: 47 + 24 -> 7 more moves per floor for 2 more pairs


if __name__ == '__main__':
    main()
