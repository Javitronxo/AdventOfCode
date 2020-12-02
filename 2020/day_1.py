def main():
    with open('day_1_input.txt') as f:
        input_list = [int(x) for x in f.readlines()]

    def part_1():
        for i, a in enumerate(input_list):
            for j, b in enumerate(input_list[i:]):
                if a + b == 2020:
                    return a * b
    print(f"Part 1: {part_1()}")

    def part_2():
        for i, a in enumerate(input_list):
            for j, b in enumerate(input_list[i:]):
                for k, c in enumerate(input_list[i + 1:]):
                    if a + b + c == 2020:
                        return a * b * c
    print(f"Part 2: {part_2()}")


if __name__ == '__main__':
    main()
