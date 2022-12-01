def main():
    calories = list()
    with open("day_1_input.txt") as f:
        calories_by_elf = 0
        for line in f.readlines():
            try:
                calories_by_elf += int(line)
            except ValueError:
                calories.append(calories_by_elf)
                calories_by_elf = 0
    print(f"Part 1: {max(calories)}")
    print(f"Part 2: {sum(sorted(calories, reverse=True)[:3])}")


if __name__ == "__main__":
    main()
