import math


def solve_part_1() -> int:
    sheet = {}
    with open("day_6_input.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            for j, char in enumerate(line.split()):
                sheet[(i, j)] = char
                max_j = j
            max_i = i

    result = 0
    for j in range(max_j + 1):
        col = 0 if (operation := sheet[(max_i, j)]) == "+" else 1
        for i in range(max_i):
            if operation == "+":
                col += int(sheet[(i, j)])
            else:
                col *= int(sheet[(i, j)])
        result += col

    return result


def rotate_text_90_ccw(text: str) -> str:
    lines = text.split("\n")
    max_len = max(len(line) for line in lines)
    padded_lines = [line.ljust(max_len) for line in lines]
    rotated = []
    for col in range(max_len - 1, -1, -1):
        rotated_line = "".join(padded_lines[row][col] for row in range(len(padded_lines)))
        rotated.append(rotated_line)
    return "\n".join(rotated)


def solve_part_2():
    with open("day_6_input.txt", "r") as f:
        input_text = f.read()
    rotated_text = rotate_text_90_ccw(input_text)

    result = 0
    nums = []
    for row in rotated_text.split("\n"):
        if row.endswith("+"):
            nums.append(int(row[:-1]))
            result += sum(nums)
        elif row.endswith("*"):
            nums.append(int(row[:-1]))
            result += math.prod(nums)
        else:
            try:
                nums.append(int(row))
            except ValueError:
                nums = []

    return result


def main():
    print(f"Part 1: {solve_part_1()}")
    print(f"Part 2: {solve_part_2()}")


if __name__ == "__main__":
    main()
