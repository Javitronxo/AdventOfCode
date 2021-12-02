def main():
    with open("day_1_input.txt") as f:
        numbers = [int(line.strip()) for line in f.read().splitlines()]
    print(f"Part 1: {sum(1 for i in range(len(numbers) - 1) if numbers[i + 1] > numbers[i])}")
    print(f"Part 2: {sum(1 for i in range(len(numbers) - 3) if numbers[i + 3] > numbers[i])}")


if __name__ == "__main__":
    main()
