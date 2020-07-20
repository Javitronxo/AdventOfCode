OPEN_MARKER = '('
CLOSE_MARKER = ')'


def decompress_file(input_str: str) -> str:
    decompressed_str = str()
    next_char = 0
    for i in range(len(input_str)):
        if i < next_char:
            continue
        elif input_str[i] == OPEN_MARKER:
            closing_marker = input_str.index(CLOSE_MARKER, i)
            parts = [int(x) for x in input_str[i + 1:closing_marker].split('x')]
            next_char = closing_marker + 1 + parts[0]
            decompressed_str += input_str[closing_marker + 1:next_char] * parts[1]
        else:
            decompressed_str += input_str[i]
    return decompressed_str


def get_length_decompress_file_v2(input_str: str) -> int:
    """Same function structure as Part 1, with the addition of the recursive call to get the extended length.

    This time we only want to get the length and not the actual file, following the problem recommendation:
        Unfortunately, the computer you brought probably doesn't have enough memory to actually decompress the file;
        you'll have to come up with another way to get its decompressed length.
    """
    next_char = 0
    decompressed_length = 0
    for i in range(len(input_str)):
        if i < next_char:
            continue
        elif input_str[i] == OPEN_MARKER:
            closing_marker = input_str.index(CLOSE_MARKER, i)
            parts = [int(x) for x in input_str[i + 1:closing_marker].split('x')]
            next_char = closing_marker + 1 + parts[0]
            decompressed_length += get_length_decompress_file_v2(input_str[closing_marker + 1:next_char]) * parts[1]
        else:
            decompressed_length += 1
    return decompressed_length


def main():
    input_str = open('day_9_input.txt').read()
    print(f"Part 1: The decompressed length of the file is {len(decompress_file(input_str))}")
    print(f"Part 2: The decompressed length of the file is {get_length_decompress_file_v2(input_str)}")


if __name__ == '__main__':
    main()
