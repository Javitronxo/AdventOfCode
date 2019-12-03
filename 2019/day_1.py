# https://adventofcode.com/2019/day/1
import math


def fuel_required(mass):
    """
    Fuel required including fuel itself
    :param mass:
    :return:
    """
    fuel = math.trunc(mass / 3) - 2
    if fuel > 0:
        fuel_for_fuel = fuel_required(fuel)
        if fuel_for_fuel > 0:
            fuel += fuel_for_fuel
    return fuel


def main():
    """Main function"""
    first_part_result, second_part_result = 0, 0
    with open('day_1_input.txt') as f_in:
        for line in f_in.readlines():
            mass = int(line.strip())
            first_partial_result = math.trunc(mass / 3) - 2
            first_part_result += first_partial_result
            second_partial_result = fuel_required(mass)
            second_part_result += second_partial_result
    print("First part result: {}\nSecond part result: {}".format(first_part_result, second_part_result))


if __name__ == '__main__':
    main()
