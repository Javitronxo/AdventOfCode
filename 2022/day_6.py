def main():
    with open("day6_input.txt") as f:
        signal = f.read().strip()

    part_one, part_two = None, None
    for i, char in enumerate(signal):
        if part_one is None and len(set(signal[i : i + 4])) == 4:
            part_one = i + 4
        if part_two is None and len(set(signal[i : i + 14])) == 14:
            part_two = i + 14

    print(f"Part 1: {part_one}")
    print(f"Part 2: {part_two}")


if __name__ == "__main__":
    main()
