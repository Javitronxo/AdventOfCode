ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def is_valid_password(password: str) -> bool:
    # Passwords may not contain the letters i, o, or l
    invalid_chars = ['i', 'o', 'l']
    if True in [char in password for char in invalid_chars]:
        return False

    # Passwords must contain at least two different, non-overlapping pairs of letters
    pairs_of_letters = 0
    positions_pairs_of_letters = list()
    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and \
                i not in positions_pairs_of_letters and (i + 1) not in positions_pairs_of_letters:
            pairs_of_letters += 1
            positions_pairs_of_letters.extend([i, i + 1])
    if pairs_of_letters < 2:
        return False

    # Passwords must include one increasing straight of at least three letters
    for i in range(len(password) - 2):
        if ALPHABET.index(password[i]) == (ALPHABET.index(password[i + 1]) - 1) == (
                ALPHABET.index(password[i + 2]) - 2):
            return True

    return False


def increment_password(password: str) -> str:
    reversed_password = password[::-1]
    new_password = ''
    for i in range(len(reversed_password)):
        try:
            new_char = ALPHABET[ALPHABET.index(reversed_password[i]) + 1]
            new_password += new_char + reversed_password[i + 1:]
            break
        except IndexError:
            new_char = 'a'
            new_password += new_char
    return new_password[::-1]


def main():
    password = open('day_11_input.txt').read()

    for _ in range(2):
        password = increment_password(password)
        while not is_valid_password(password):
            password = increment_password(password)
        print("Next Santa's password is %s" % password)


if __name__ == '__main__':
    main()
