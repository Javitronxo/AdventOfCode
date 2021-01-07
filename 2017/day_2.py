def main():
    checksum_one = 0
    checksum_two_addends = list()
    with open("day_2_input.txt") as f:
        for line in f.read().splitlines():
            line_ints = [int(x) for x in line.split("\t")]
            checksum_one += max(line_ints) - min(line_ints)
            checksum_two_addends.extend(
                [x // y for i, x in enumerate(line_ints) for j, y in enumerate(line_ints) if i != j and x % y == 0]
            )

    print(f"Part 1: {checksum_one}")
    print(f"Part 2: {sum(checksum_two_addends)}")


if __name__ == "__main__":
    main()
