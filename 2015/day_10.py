def look_and_say(input_value: str) -> str:
    prev_char = input_value[0]
    output_str = ''
    multiplier = 0
    for char in input_value:
        if char == prev_char:
            multiplier += 1
        else:
            output_str += str(multiplier) + prev_char
            prev_char = char
            multiplier = 1
    output_str += str(multiplier) + prev_char
    return output_str


def main():
    input_str = open('day_10_input.txt').read()
    iterations = 50
    for i in range(iterations):
        input_str = look_and_say(input_str)
        if i == (40 - 1):  # Part 1: Result for 40 iterations
            print('The length of the result for %d iterations is %d' % ((i + 1), len(input_str)))
    print('The length of the result for %d iterations is %d' % (iterations, len(input_str)))


if __name__ == '__main__':
    main()
