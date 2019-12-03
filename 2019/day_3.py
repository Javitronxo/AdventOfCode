# https://adventofcode.com/2019/day/3


def read_file(file_name):
    wires = list()
    with open(file_name) as f_in:
        for line in f_in.readlines():
            wire = line.strip().split(',')
            wires.append(wire)
    return wires


def get_manhattan_distance(point_1, point_2):
    return sum(abs(d_1 - d_2) for d_1, d_2 in zip(point_1, point_2))


def populate_grid(grid, intersections_info, wire, wire_id):
    pointer = [0, 0]
    num_steps = 0
    for step in wire:
        direction = step[0]
        length = int(step[1:])

        for l in range(1, length + 1):
            x, y = None, None
            if direction == 'D':
                x = pointer[0]
                y = pointer[1] - l
            elif direction == 'U':
                x = pointer[0]
                y = pointer[1] + l
            elif direction == 'L':
                x = pointer[0] - l
                y = pointer[1]
            elif direction == 'R':
                x = pointer[0] + l
                y = pointer[1]

            # Populate the grid
            grid.setdefault(x, dict())
            grid[x].setdefault(y, '.')
            if grid[x][y] == '.':
                grid[x][y] = wire_id
            elif grid[x][y] == wire_id:
                pass
            else:
                grid[x][y] = 'X'
                # Save the info for part 2
                cross_point = (x, y)
                num_steps_cross_point = num_steps + l
                intersections_info.setdefault(cross_point, dict())
                intersections_info[cross_point][wire_id] = num_steps_cross_point

        num_steps += length

        # Update the pointer for the next step
        if direction == 'D':
            pointer[1] -= length
        elif direction == 'U':
            pointer[1] += length
        elif direction == 'L':
            pointer[0] -= length
        elif direction == 'R':
            pointer[0] += length

    return grid, intersections_info


def main(file_name):
    wires = read_file(file_name)
    grid = dict()
    grid[0] = dict()
    grid[0][0] = 'o'
    intersections_info = dict()

    wire_ids = ['A', 'B']
    for wire, wire_id in zip(wires, wire_ids):
        grid, intersections_info = populate_grid(grid, intersections_info, wire, wire_id)
    _, intersections_info = populate_grid(grid, intersections_info, wires[0], wire_ids[0])

    minimum_distance = None
    for cross_point in intersections_info.keys():
        distance_to_center = get_manhattan_distance((cross_point[0], cross_point[1]), (0, 0))
        if (minimum_distance is None) or (distance_to_center < minimum_distance):
            minimum_distance = distance_to_center

    min_steps = None
    for _, intersection_steps in intersections_info.items():
        sum_steps = sum(intersection_steps[wire_id] for wire_id in wire_ids)
        if (min_steps is None) or (sum_steps < min_steps):
            min_steps = sum_steps

    return minimum_distance, min_steps


if __name__ == '__main__':
    input_file_name = 'day_3_input.txt'
    result_first_part, result_second_part = main(input_file_name)
    print("First part result: {}".format(result_first_part))
    print("Second part result: {}".format(result_second_part))
