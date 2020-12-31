from typing import List


def get_distance(point: List[int]) -> int:
    return abs(point[0]) + abs(point[1])


def main():
    with open("day_1_input.txt") as f_in:
        instructions = f_in.read().split(", ")

    current_location = [0, 0]
    visited_locations = [current_location]
    direction = 0

    for instruction in instructions:
        turn = instruction[0]
        steps = int(instruction[1:])

        if turn == "R":
            direction += 90
        elif turn == "L":
            direction += 270
        else:
            raise ValueError(f"Unrecognized turn {turn}")

        # Let's keep it simple and use 0, 90, 180 and 270 as possible directions
        if direction >= 360:
            direction -= 360

        if direction == 0:
            walked_locations = [[current_location[0], current_location[1] + i] for i in range(1, steps + 1)]
        elif direction == 90:
            walked_locations = [[current_location[0] + i, current_location[1]] for i in range(1, steps + 1)]
        elif direction == 180:
            walked_locations = [[current_location[0], current_location[1] - i] for i in range(1, steps + 1)]
        elif direction == 270:
            walked_locations = [[current_location[0] - i, current_location[1]] for i in range(1, steps + 1)]
        else:
            raise ValueError(f"Unrecognized direction {direction}")
        current_location = walked_locations[-1]
        visited_locations.extend(walked_locations)

    print(f"Part 1: We have to move {get_distance(current_location)} blocks away")
    first_double_location = [location for location in visited_locations if visited_locations.count(location) > 1][0]
    print(f"Part 2: We have to move {get_distance(first_double_location)} blocks away")


if __name__ == "__main__":
    main()
