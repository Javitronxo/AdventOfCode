import re
from functools import reduce
from itertools import combinations_with_replacement, permutations, zip_longest


class Ingredient:
    def __init__(self, name: str, capacity: int, durability: int, flavor: int, texture: int, calories: int):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def set_teaspoons(self, t: int) -> list:
        return [t * self.capacity, t * self.durability, t * self.flavor, t * self.texture, t * self.calories]


def get_combinations(total_sum: int, length: int) -> set:
    all_combinations = list()
    for c in combinations_with_replacement(range(total_sum + 1), length):
        if sum(c) == total_sum:
            for p in permutations(c):
                all_combinations.append(p)
    return set(all_combinations)


def get_maximum_score(total_teaspoons: int, all_ingredients: list, calories_per_cookie: int = None) -> int:
    max_score = 0
    for teaspoons_combination in get_combinations(total_teaspoons, len(all_ingredients)):
        # Get the property scores
        ingredient_scores = list()
        for teaspoons, ingredient in zip_longest(teaspoons_combination, all_ingredients):
            ingredient_scores.append(ingredient.set_teaspoons(teaspoons))
        properties_scores = [sum(x) for x in zip(*ingredient_scores)]

        # Apply calories count if set
        if calories_per_cookie and properties_scores[-1] != calories_per_cookie:
            continue
        properties_scores.pop(-1)

        # Get the score and compare with the current maximum
        properties_scores.sort()
        if properties_scores[0] < 0:
            continue
        score = reduce((lambda x, y: x * y), properties_scores)
        if score > max_score:
            max_score = score

    return max_score


def main():
    line_pattern = r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)'
    all_ingredients = list()
    with open('day_15_input.txt') as f_in:
        for line in f_in.readlines():
            name, capacity, durability, flavor, texture, calories = re.findall(line_pattern, line)[0]
            ingredient = Ingredient(name, int(capacity), int(durability), int(flavor), int(texture), int(calories))
            all_ingredients.append(ingredient)

    total_teaspoons = 100
    max_score = get_maximum_score(total_teaspoons, all_ingredients)
    print('Total score of the highest-scoring cookie we can make is %d' % max_score)
    max_score = get_maximum_score(total_teaspoons, all_ingredients, calories_per_cookie=500)
    print('Total score of the highest-scoring cookie we can make is %d' % max_score)


if __name__ == '__main__':
    main()
