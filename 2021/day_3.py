import collections
from typing import List


def get_number(numbers: List[str], oxygen: bool) -> int:
    for i in range(len(numbers[0])):
        new_numbers = list()
        counter = {"0": 0, "1": 0}
        for number in numbers:
            counter[number[i]] += 1
        most_common = "0" if counter["0"] > counter["1"] else "1"
        less_common = "0" if counter["0"] <= counter["1"] else "1"
        for number in numbers:
            if (oxygen and number[i] == most_common) or (not oxygen and number[i] == less_common):
                new_numbers.append(number)
        numbers = new_numbers
        if len(numbers) == 1:
            break
    assert len(numbers) == 1
    return int(numbers.pop(), 2)


def main():
    with open("day_3_input.txt") as f:
        puzzle_input = f.read().splitlines()

    counter = dict()
    for line in puzzle_input:
        for i, char in enumerate(line):
            try:
                counter[i][char] += 1
            except KeyError:
                counter[i] = collections.defaultdict(int)
                counter[i][char] += 1

    epsilon_rate = str()
    gamma_rate = str()
    for key, values in counter.items():
        if values["0"] > values["1"]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"
    print(f"Part 1: {int(gamma_rate, 2) * int(epsilon_rate, 2)}")

    oxygen_number = get_number(puzzle_input, oxygen=True)
    c02_number = get_number(puzzle_input, oxygen=False)
    print(f"Part 2: {oxygen_number * c02_number}")


if __name__ == '__main__':
    main()
