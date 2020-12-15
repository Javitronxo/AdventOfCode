from itertools import permutations


def main():
    with open("day_9_input.txt") as f:
        input_list = [int(x) for x in f.read().splitlines()]

    target_number = None
    for i in range(25, len(input_list)):
        preamble = input_list[(i - 25) : i]
        valid_number = False
        for p in permutations(preamble, 2):
            if (p[0] + p[1] == input_list[i]) and (p[0] != p[1]):
                valid_number = True
                break
        if not valid_number:
            target_number = input_list[i]
            print(f"Part 1: The first number that does not have the property is {target_number}")
            break

    sum_list = list()
    i = 0
    j = 0
    while True:
        number = input_list[i]
        if sum(sum_list) + number == target_number:
            sum_list.append(number)
            break
        elif sum(sum_list) + number < target_number:
            sum_list.append(number)
            i += 1
        else:
            j += 1
            i = j
            sum_list = list()

    print(f"Part 2: The encryption weakness is {min(sum_list) + max(sum_list)}")


if __name__ == "__main__":
    main()
