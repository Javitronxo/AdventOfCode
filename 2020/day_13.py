"""
This puzzle is based on:
    https://en.wikipedia.org/wiki/Chinese_remainder_theorem
Reddit told me after I waited for a long long time burning my computer...
"""
import sys
from typing import Tuple


def find_bus_cadence(bus: int, cadence: int, start_time: int, offset: int) -> Tuple[int, int]:
    timestamp = start_time
    while (timestamp - offset) % bus != 0:
        timestamp += cadence
    new_cadence = timestamp + cadence
    while (new_cadence - offset) % bus != 0:
        new_cadence += cadence
    return timestamp, new_cadence - timestamp


def main():
    with open("day_13_input.txt") as f:
        input_lines = f.read().splitlines()
    my_time = int(input_lines[0])
    bus_lines = [int(b) if b.isdigit() else None for b in input_lines[1].split(",")]

    min_wait = sys.maxsize
    bus_id = None
    for bus_line in bus_lines:
        if bus_line is None:
            continue
        minutes = bus_line - (my_time % bus_line)
        if minutes < min_wait:
            min_wait = minutes
            bus_id = bus_line
    print(f"Part 1: {min_wait * bus_id}")

    bus_lines = bus_lines[::-1]
    offset = 0
    cadence = bus_lines[0]
    timestamp = bus_lines[0]
    for bus in bus_lines[1:]:
        offset += 1
        if bus is None:
            continue
        timestamp, cadence = find_bus_cadence(bus, cadence, timestamp, offset)
    timestamp -= offset
    print(f"Part 2: {timestamp}")


if __name__ == "__main__":
    main()
