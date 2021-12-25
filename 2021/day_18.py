import collections
import itertools
from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    value: int
    depth: int


def add_numbers(number_one: List[Node], number_two: List[Node]) -> List[Node]:
    new_number = [
        Node(node.value, node.depth + 1)
        for node in number_one + number_two
    ]
    while any(node.depth > 4 for node in new_number) or any(node.value > 9 for node in new_number):
        # Explode
        while any(node.depth > 4 for node in new_number):
            for i in range(len(new_number)):
                if new_number[i].depth > 4:
                    try:
                        if i - 1 >= 0:
                            new_number[i - 1].value += new_number[i].value
                    except IndexError:
                        pass
                    try:
                        new_number[i + 2].value += new_number[i + 1].value
                    except IndexError:
                        pass
                    new_number[i].value = 0
                    new_number[i].depth -= 1
                    new_number.pop(i + 1)
                    break
        # Split
        while any(node.value > 9 for node in new_number):
            for i in range(len(new_number)):
                if new_number[i].value > 9:
                    left_value = new_number[i].value // 2
                    right_value = new_number[i].value - left_value
                    new_number[i].value = left_value
                    new_number[i].depth += 1
                    new_node = Node(right_value, new_number[i].depth)
                    new_number.insert(i + 1, new_node)
                    break
            # We might need to explode before splitting again
            break
    return new_number


def get_magnitude(number: List[Node]) -> int:
    while len(number) > 1:
        max_depth = max(node.depth for node in number)
        for i in range(len(number)):
            if number[i].depth == max_depth:
                magnitude = number[i].value * 3 + number[i + 1].value * 2
                number[i] = Node(magnitude, max_depth - 1)
                number.pop(i + 1)
                break
    return number[0].value


def main():
    fish_numbers = collections.deque()
    with open("day_18_input.txt") as f:
        for line in f.readlines():
            depth = 0
            number = list()
            for char in line:
                if char == "[":
                    depth += 1
                elif char == "]":
                    depth -= 1
                elif char.isdigit():
                    number.append(Node(value=int(char), depth=depth))
                else:
                    continue
            fish_numbers.append(number)
    permutations = itertools.permutations(fish_numbers, 2)

    current_number = fish_numbers.popleft()
    while fish_numbers:
        current_number = add_numbers(current_number, fish_numbers.popleft())
    print(f"Part 1: {get_magnitude(current_number)}")

    max_magnitude = -1
    for p in permutations:
        number = add_numbers(p[0], p[1])
        max_magnitude = max(max_magnitude, get_magnitude(number))
    print(f"Part 2: {max_magnitude}")


if __name__ == "__main__":
    main()
