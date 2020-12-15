from collections import defaultdict
from typing import List


def play_game(input_list: List[int], target_position: int) -> int:
    number = None
    answers = defaultdict(list)
    for i, number in enumerate(input_list):
        answers[number].append(i)
    for i in range(len(input_list), target_position):
        number = 0 if len(answers[number]) == 1 else (answers[number][-1] - answers[number][-2])
        answers[number].append(i)
    return number


def main():
    with open("day_15_input.txt") as f:
        input_lines = [int(x) for x in f.read().split(",")]
    print(f"Part 1: {play_game(input_lines, target_position=2020)}")
    print(f"Part 1: {play_game(input_lines, target_position=30000000)}")


if __name__ == "__main__":
    main()
