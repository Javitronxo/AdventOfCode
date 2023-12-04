mapping = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def main():
    with open("day_1_input.txt") as f:
        values_one = list()
        values_two = list()
        for line in f.readlines():
            ints_one = list()
            ints_two = list()
            for i, char in enumerate(stripped_line := line.strip()):
                try:
                    ints_one.append(int(char))
                    ints_two.append(int(char))
                except ValueError:
                    for key, value in mapping.items():
                        if key == "".join(stripped_line[i : i + len(key)]):
                            ints_two.append(value)
            values_one.append(int(f"{ints_one[0]}{ints_one[-1]}"))
            values_two.append(int(f"{ints_two[0]}{ints_two[-1]}"))
    print(f"Part 1: {sum(values_one)}")
    print(f"Part 2: {sum(values_two)}")


if __name__ == "__main__":
    main()
