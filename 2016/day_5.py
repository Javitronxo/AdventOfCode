from lib.utils import get_md5_hash


def main():
    puzzle_input = open("day_5_input.txt").read()

    password_1 = str()
    password_2 = [None] * 8
    i = 0
    while len(password_1) < 8 or None in password_2:
        candidate_hash = get_md5_hash(puzzle_input + str(i))
        if candidate_hash.startswith("00000"):
            # Check password for Part 1
            if len(password_1) < 8:
                password_1 += candidate_hash[5]
            # Check password for Part 2
            try:
                if password_2[int(candidate_hash[5])] is None:
                    password_2[int(candidate_hash[5])] = candidate_hash[6]
            except (ValueError, IndexError):
                pass
        i += 1

    print(f"Part 1: The password is {password_1}")
    print(f"Part 2: The password is {''.join(password_2)}")


if __name__ == "__main__":
    main()
