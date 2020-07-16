import math
from typing import List, Tuple


def get_divisors(n: int, m: int) -> Tuple[List[int], List[int]]:
    divisors = list()
    divisors_limited = list()
    i = 1
    while i <= math.sqrt(n):
        if n % i == 0:
            divisors.append(i)
            if i * m >= n:
                divisors_limited.append(i)
            if n / i != i:
                divisors.append(int(n / i))
                if int(n / i) * m >= n:
                    divisors_limited.append(int(n / i))
        i += 1
    return sorted(divisors), sorted(divisors_limited)


def main():
    puzzle_input = int(open('day_20_input.txt').read())

    part_1, part_2 = False, False
    house = 1
    while not (part_1 and part_2):
        divisors, divisors_limited = get_divisors(house, 50)
        if not part_1 and sum(divisors) * 10 >= puzzle_input:
            print(f"Part 1: The lowest house number of the house to get at least {puzzle_input} presents is: {house}")
            part_1 = True
        if not part_2 and sum(divisors_limited) * 11 >= puzzle_input:
            print(f"Part 2: The lowest house number of the house to get at least {puzzle_input} presents is: {house}")
            part_2 = True
        house += 1


if __name__ == '__main__':
    main()
