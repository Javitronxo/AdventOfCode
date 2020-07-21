def get_length_decompressed_file(input_str: str, v2: bool = False) -> int:
    next_char = 0
    decompressed_length = 0
    for i in range(len(input_str)):
        if i < next_char:
            continue
        elif input_str[i] == '(':
            closing_marker = input_str.index(')', i)
            parts = [int(x) for x in input_str[i + 1:closing_marker].split('x')]
            next_char = closing_marker + 1 + parts[0]
            target_str = input_str[closing_marker + 1:next_char]
            if v2:
                decompressed_length += get_length_decompressed_file(target_str, v2=True) * parts[1]
            else:
                decompressed_length += len(target_str * parts[1])
        else:
            decompressed_length += 1
    return decompressed_length


def main():
    input_str = open('day_9_input.txt').read()
    print(f"Part 1: The decompressed length of the file is {get_length_decompressed_file(input_str)}")
    print(f"Part 2: The decompressed length of the file is {get_length_decompressed_file(input_str, v2=True)}")


if __name__ == '__main__':
    main()
