import string


def main():
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    total_priority_one = 0
    total_priority_two = 0
    with open("day_3_input.txt") as f:
        group = list()
        for i, line in enumerate(f.readlines()):
            compartment_1 = line[: len(line) // 2]
            compartment_2 = line[len(line) // 2 :]
            repeated = [char for char in compartment_1 if char in compartment_2][0]
            total_priority_one += alphabet.index(repeated) + 1
            group.append(line)
            if (i + 1) % 3 == 0:
                repeated = [char for char in group[0] if char in group[1] and char in group[2]][0]
                total_priority_two += alphabet.index(repeated) + 1
                group = list()

    print(f"Part 1: {total_priority_one}")
    print(f"Part 2: {total_priority_two}")


if __name__ == "__main__":
    main()
