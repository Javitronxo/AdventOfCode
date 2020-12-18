import re


def evaluate_part_one(expression: str) -> int:
    """Solve the expression from left to right regardless of operators"""
    answer = 0
    operator = None
    for elem in expression.split():
        if elem.isdigit():
            if operator is None:
                answer = int(elem)
            elif operator == "+":
                answer += int(elem)
            elif operator == "*":
                answer *= int(elem)
        else:
            operator = elem
    return answer


def evaluate_part_two(expression: str) -> int:
    """Solve the expression giving preference to additions over multiplications"""
    while "+" in expression:
        expression_list = expression.split()
        i = expression_list.index("+")
        new_expression = str()
        for j, char in enumerate(expression_list):
            if j in [i, i - 1]:
                pass
            elif j == i + 1:
                new_expression += str(eval(f"{expression_list[i - 1]} + {expression_list[i + 1]}")) + " "
            else:
                new_expression += char + " "
        expression = new_expression.strip()
    return eval(expression)


def parse_expression(expression: str, part: int) -> int:
    def evaluate_expression(e: str) -> int:
        return evaluate_part_one(e) if part == 1 else evaluate_part_two(e)

    while re.search(r"[()]", expression):
        for sub_expression in re.findall(r"\([\d+* ]+\)", expression):
            expression = expression.replace(sub_expression, str(evaluate_expression(sub_expression[1:-1])))
    return evaluate_expression(expression)


def main():
    with open("day_18_input.txt") as f:
        input_lines = f.read().splitlines()

    print(f"Part 1: {sum(parse_expression(expression, part=1) for expression in input_lines)}")
    print(f"Part 2: {sum(parse_expression(expression, part=2) for expression in input_lines)}")


if __name__ == "__main__":
    main()
