from typing import Tuple


def remove_garbage(input_str: str) -> Tuple[str, int]:
    open_garbage = False
    ignore_next = False
    new_str = str()
    cancelled_chars = 0
    for char in input_str:
        if ignore_next:
            ignore_next = False
        elif char == "!":
            ignore_next = True
        elif char == ">" and open_garbage:
            open_garbage = False
        elif open_garbage:
            cancelled_chars += 1
        elif char == "<":
            open_garbage = True
        else:
            new_str += char
    return new_str, cancelled_chars


def main():
    with open("day_9_input.txt") as f:
        puzzle_input = f.read().strip()

    no_garbage_str, cancelled_chars = remove_garbage(puzzle_input)
    score = 0
    depth = 0
    for char in no_garbage_str:
        if char == "{":
            depth += 1
        elif char == "}":
            score += depth
            depth -= 1

    print(f"Part 1: {score}")
    print(f"Part 2: {cancelled_chars}")


if __name__ == "__main__":
    main()
