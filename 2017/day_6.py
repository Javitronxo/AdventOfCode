def main():
    with open("day_6_input.txt") as f:
        memory_bank = [int(x) for x in f.read().split()]

    redistributions = 0
    combinations = list()
    while tuple(memory_bank) not in combinations:
        combinations.append(tuple(memory_bank))
        max_number = max(memory_bank)
        max_number_index = memory_bank.index(max_number)
        memory_bank[max_number_index] = 0
        for i in range(max_number):
            index = (max_number_index + 1 + i) % len(memory_bank)
            memory_bank[index] += 1
        redistributions += 1

    print(f"Part 1: {redistributions}")
    print(f"Part 2: {redistributions - combinations.index(tuple(memory_bank))}")


if __name__ == "__main__":
    main()
