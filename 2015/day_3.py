from collections import defaultdict


def deliver_gifts(instructions: str) -> dict:
    current_position = [0, 0]
    gifts_delivered = defaultdict(int)
    gifts_delivered[(0, 0)] = 1
    for direction in instructions:
        if direction == '^':
            current_position[0] += 1
        elif direction == 'v':
            current_position[0] -= 1
        if direction == '>':
            current_position[1] += 1
        if direction == '<':
            current_position[1] -= 1
        gifts_delivered[tuple(current_position)] += 1
    return gifts_delivered


def main():
    with open('day_3_input.txt') as f_in:
        input_str = f_in.read()

    gifts_delivered = deliver_gifts(input_str)
    print('Santa delivered gifts to %d houses' % len(gifts_delivered))

    santa_directions = input_str[0::2]
    gifts_delivered_by_santa = deliver_gifts(santa_directions)
    robot_directions = input_str[1::2]
    gifts_delivered_by_robot = deliver_gifts(robot_directions)
    gifts_delivered = list(gifts_delivered_by_santa.keys()) + [house for house in gifts_delivered_by_robot.keys()
                                                               if house not in gifts_delivered_by_santa.keys()]
    print('Santa and the robot delivered gifts to %d houses' % len(gifts_delivered))


if __name__ == '__main__':
    main()
