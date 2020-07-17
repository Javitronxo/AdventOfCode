import re
from typing import Dict, List
from collections import defaultdict


def generate_infinite_paper(end_row: int, end_column: int) -> Dict[int, List[int]]:
    step = 0
    final_step = end_row + end_column
    paper = defaultdict(list)

    current_cell = 20151125
    while step < final_step:
        for i in range(step + 1):
            row = step - i
            paper[row].append(current_cell)
            current_cell = (current_cell * 252533) % 33554393
        step += 1

    return paper


def main():
    with open('day_25_input.txt') as f_in:
        input_str = f_in.read()
    row, column = re.search(r'row (\d+), column (\d+)', input_str).groups()
    row, column = int(row), int(column)

    paper = generate_infinite_paper(row, column)
    print(f"The code we give to the machine is {paper[row - 1][column - 1]}")


if __name__ == '__main__':
    main()
