from typing import Tuple, Union


def get_floor(input_str: str, first_time_level: int = None) -> Tuple[int, Union[None, int]]:
    level = 0
    position_first_time_level = None
    for i in range(len(input_str)):
        if input_str[i] == '(':
            level += 1
        elif input_str[i] == ')':
            level -= 1
        if first_time_level and level == first_time_level:
            position_first_time_level = i + 1
            first_time_level = None
    return level, position_first_time_level


def main():
    with open('day_1_input.txt') as f_in:
        input_str = f_in.read()
    level, position_first_time_level = get_floor(input_str, first_time_level=-1)
    print('Santa is in level %d' % level)
    print('First time in basement is on %d position' % position_first_time_level)


if __name__ == '__main__':
    main()
