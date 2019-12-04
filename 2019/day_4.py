# https://adventofcode.com/2019/day/4


def verify_password_rules(num):
    matching_groups = dict()
    number = str(num)
    right_length = True if len(number) == 6 else False
    is_increasing = True
    for i in range(len(number)):
        matching_groups.setdefault(number[i], 0)
        matching_groups[number[i]] += 1
        try:
            if int(number[i]) > int(number[i + 1]):
                is_increasing = False
        except IndexError:
            continue

    has_adjacent = max(matching_groups.values()) > 1
    candidate_first_part = has_adjacent and is_increasing and right_length
    candidate_second_part = candidate_first_part and 2 in matching_groups.values()
    return candidate_first_part, candidate_second_part


def main():
    with open('day_4_input.txt') as f_in:
        file_content = f_in.read()
    parts = file_content.strip().split('-')
    range_start = int(parts[0])
    range_end = int(parts[1])

    candidates_first_part = list()
    candidates_second_part = list()
    for i in range(range_start, range_end):
        candidate_first_part, candidate_second_part = verify_password_rules(i)
        if candidate_first_part:
            candidates_first_part.append(i)
        if candidate_second_part:
            candidates_second_part.append(i)
    print("First part result: {}".format(len(candidates_first_part)))
    print("Second part result: {}".format(len(candidates_second_part)))


if __name__ == '__main__':
    main()
