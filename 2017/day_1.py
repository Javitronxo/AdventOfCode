def main():
    with open("day_1_input.txt") as f:
        puzzle_input = f.read().strip()

    answer = sum(
        int(char)
        for i, char in enumerate(puzzle_input)
        if i == (len(puzzle_input) - 1) and char == puzzle_input[0] or char == puzzle_input[i + 1]
    )
    print(f"Part 1: {answer}")

    answer = sum(
        int(puzzle_input[i]) * 2
        for i in range(len(puzzle_input) // 2)
        if int(puzzle_input[i]) == int(puzzle_input[i + len(puzzle_input) // 2])
    )
    print(f"Part 2: {answer}")


if __name__ == "__main__":
    main()
