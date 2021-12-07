def main():
    with open("day_7_input.txt") as f:
        puzzle_input = [int(x) for x in f.read().split(",")]

    median = puzzle_input[len(puzzle_input) // 2]
    mean = int(sum(puzzle_input) / len(puzzle_input))

    print(f"Part 1: {sum(abs(n - median) for n in puzzle_input)}")
    print(f"Part 2: {sum(sum(i for i in range(1, abs(n - mean) + 1)) for n in puzzle_input)}")


if __name__ == "__main__":
    main()
