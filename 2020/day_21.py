def main():
    with open("day_21_input.txt") as f:
        input_lines = f.read().splitlines()

    all_ingredients = set()
    allergens_dict = dict()
    for line in input_lines:
        ingredients = set(line.split(" (")[0].split())
        all_ingredients.update(ingredients)

        allergens = line.split("contains ")[1][:-1].split(", ")
        for allergen in allergens:
            if allergen not in allergens_dict:
                allergens_dict[allergen] = ingredients
            else:
                allergens_dict[allergen] = allergens_dict[allergen].intersection(ingredients)

    non_allergen = set()
    for ingredient in all_ingredients:
        if not any(ingredient in allergens for allergens in allergens_dict.values()):
            non_allergen.add(ingredient)

    answer = sum(1 for ingredient in non_allergen for line in input_lines if ingredient in line.split())
    print(f"Part 1: {answer}")

    while any(len(ingredients) != 1 for ingredients in allergens_dict.values()):
        for allergen, ingredients in allergens_dict.items():
            if len(ingredients) == 1:
                continue
            for other_allergen, other_ingredients in allergens_dict.items():
                if other_allergen == allergen:
                    continue
                if len(other_ingredients) == 1:
                    allergens_dict[allergen] = allergens_dict[allergen].difference(allergens_dict[other_allergen])

    answer = str()
    for allergen in sorted(allergens_dict.keys()):
        answer += allergens_dict[allergen].pop() + ","
    answer = answer[:-1]
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    main()
