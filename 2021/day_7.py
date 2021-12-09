def main():
    with open("day_7_input.txt") as f:
        puzzle_input = [int(x) for x in f.read().split(",")]

    puzzle_input.sort()
    median = puzzle_input[len(puzzle_input) // 2]
    fuel_one = sum(abs(n - median) for n in puzzle_input)
    print(f"Part 1: {fuel_one}")

    mean = int(sum(puzzle_input) / len(puzzle_input))
    fuel_two = sum((x := abs(n - mean)) * (x + 1) // 2 for n in puzzle_input)
    print(f"Part 2: {fuel_two}")


if __name__ == "__main__":
    main()
