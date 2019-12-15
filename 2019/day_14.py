# https://adventofcode.com/2019/day/14
import math


class Refinery:
    def __init__(self, recipes):
        self.recipes = recipes
        self.distances = self.calculate_distances()

    def calculate_distances(self):
        distance = {'ORE': 0}
        while len(distance) <= len(self.recipes.keys()):
            for material in self.recipes.keys():
                if material in distance or \
                        not all([i in distance for i in self.recipes[material]['ingredients'].keys()]):
                    continue
                distance[material] = max([distance[i] for i in self.recipes[material]['ingredients'].keys()]) + 1
        return distance

    def required_ore(self, fuel):
        needed = {'FUEL': fuel}
        while len(needed) > 1 or 'ORE' not in needed:
            material = max(needed, key=lambda x: self.distances[x])
            quantity = needed[material]
            del needed[material]
            if material == 'ORE':
                needed[material] = quantity
                continue
            base_quantity, ingredients = self.recipes[material].values()
            for a, b in ingredients.items():
                if a not in needed:
                    needed[a] = 0
                needed[a] += math.ceil(quantity / base_quantity) * b
        return needed['ORE']

    def search_fuel_target(self, ore):
        one_unit = self.required_ore(1)
        target = ore // one_unit
        used_ore = self.required_ore(target)
        while True:
            target += (ore - used_ore) // one_unit + 1
            used_ore = self.required_ore(target)
            if used_ore > ore:
                break
        return target - 1


def read_input_file(input_file):
    recipes = {}
    with open(input_file) as f:
        for line in f.readlines():
            left, right = line.strip().split(' => ')
            output = right.split()
            recipes[output[1]] = {
                'quantity': int(output[0]),
                'ingredients': {item[1]: int(item[0]) for item in [item.split() for item in left.split(', ')]}
            }
    return recipes


def main():
    recipes = read_input_file('day_14_input.txt')

    refinery = Refinery(recipes)
    result_first_part = refinery.required_ore(1)
    print("First part result: {}".format(result_first_part))
    result_second_part = refinery.search_fuel_target(1000000000000)
    print("Second part result: {}".format(result_second_part))


if __name__ == '__main__':
    main()
