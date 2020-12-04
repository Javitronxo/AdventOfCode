import re


def main():
    valid_passwords_part_1 = 0
    valid_passwords_part_2 = 0

    with open("day_2_input.txt") as f:
        for line in f.readlines():
            line_pattern = r"(\d+)-(\d+) (\w): (\w+)"

            a, b, letter, password = re.findall(line_pattern, line)[0]
            if int(a) <= password.count(letter) <= int(b):
                valid_passwords_part_1 += 1
            if (password[int(a) - 1] + password[int(b) - 1]).count(letter) == 1:
                valid_passwords_part_2 += 1

    print(f"Part 1: We have {valid_passwords_part_1} passwords")
    print(f"Part 2: We have {valid_passwords_part_2} passwords")


if __name__ == "__main__":
    main()
