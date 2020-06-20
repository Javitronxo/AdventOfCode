import hashlib


def has_md5_trailing_zeroes(input_str: str, n_zeroes: int = 5) -> bool:
    md5 = hashlib.md5(input_str.encode()).hexdigest()
    return md5[:n_zeroes] == '0' * n_zeroes


def find_md5(input_str: str, n_zeroes: int = 5) -> int:
    i = 1
    while True:
        if has_md5_trailing_zeroes(input_str + str(i), n_zeroes):
            return i
        i += 1


def main():
    with open('day_4_input.txt') as f_in:
        input_str = f_in.read()
    print('Lowest positive number that produces 5 zeroes hash is %d' % find_md5(input_str))
    print('Lowest positive number that produces 6 zeroes hash is %d' % find_md5(input_str, 6))


if __name__ == '__main__':
    main()
