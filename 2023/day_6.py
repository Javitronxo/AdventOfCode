import re
from functools import reduce


def ways_to_win(time: int, distance: int) -> int:
    return sum([1 for holding_time in range(time) if holding_time * (time - holding_time) > distance])


def main():
    with open("day_6_input.txt") as f:
        lines = f.readlines()

    part_one = list()
    times_part_one = [int(i) for i in re.findall(r"\d+", lines[0])]
    distances_part_one = [int(i) for i in re.findall(r"\d+", lines[1])]
    for time, distance in zip(times_part_one, distances_part_one):
        part_one.append(ways_to_win(time, distance))
    print(f"Part 1: {reduce(lambda x, y: x*y, part_one)}")

    time_part_two = int("".join([str(i) for i in times_part_one]))
    distance_part_two = int("".join([str(i) for i in distances_part_one]))
    print(f"Part 2: {ways_to_win(time_part_two, distance_part_two)}")


if __name__ == "__main__":
    main()
