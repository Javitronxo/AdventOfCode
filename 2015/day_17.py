from itertools import combinations


def main():
    with open('day_17_input.txt') as f_in:
        containers = [int(n) for n in f_in.read().split('\n')]
    containers.sort()
    total_liters = 150
    all_combinations = list()
    min_len = len(containers) + 1
    for i in range(1, len(containers) + 1):
        for combination in combinations(containers, i):
            if sum(combination) == total_liters:
                all_combinations.append(combination)
                if len(combination) < min_len:
                    min_len = len(combination)
    print(f"We have {len(all_combinations)} different combinations")

    minimum_combinations = [c for c in all_combinations if len(c) == min_len]
    print(f"There are {len(minimum_combinations)} ways to fit with minimum containers")


if __name__ == '__main__':
    main()
