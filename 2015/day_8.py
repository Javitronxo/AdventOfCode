import re


def main():
    memory_chars_total = 0
    literal_chars_total = 0
    encoded_chars_total = 0
    with open('day_8_input.txt') as f_in:
        for line in f_in.readlines():
            line = line.strip()

            literal_chars = len(line)
            literal_chars_total += literal_chars

            memory_line = re.sub(r'\\x[0-9a-f]{2}', 'X', line)
            memory_line = re.sub(r'\\"|\\\\', 'X', memory_line)
            memory_chars = len(memory_line) - 2
            memory_chars_total += memory_chars

            encoded_line = re.sub(r'\\x[0-9a-f]{2}', 'XXXXX', line)
            encoded_line = re.sub(r'\\"|\\\\', 'XXXX', encoded_line)
            encoded_chars = len(encoded_line) + 4
            encoded_chars_total += encoded_chars

            print(line, literal_chars, memory_chars)
    print('Number of literal characters minus memory characters is %d' % (literal_chars_total - memory_chars_total))
    print('Number of encoded characters minus literal characters is %d' % (encoded_chars_total - literal_chars_total))


if __name__ == '__main__':
    main()
