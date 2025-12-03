def largest_joltage(bank: list[int], n: int) -> int:
    result = []
    start = 0
    for _ in range(n):
        # The farthest we can look ahead while still having enough digits left
        end = len(bank) - (n - len(result)) + 1
        # Pick the largest digit in the allowed range
        max_digit = max(bank[start:end])
        # Move start index to the first occurrence of that digit + 1
        start = bank.index(max_digit, start, end) + 1
        result.append(max_digit)
    return int("".join(str(d) for d in result))


def main():
    part_1, part_2 = 0, 0
    with open("day_3_input.txt") as f:
        for line in f.readlines():
            bank = [int(x) for x in line.strip()]
            part_1 += largest_joltage(bank, n=2)
            part_2 += largest_joltage(bank, n=12)

    print(f"Part 1: {part_1}")
    print(f"Part 2: {part_2}")


if __name__ == "__main__":
    main()
